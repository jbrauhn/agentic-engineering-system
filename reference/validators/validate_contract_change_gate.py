#!/usr/bin/env python3
import json
import sys
from pathlib import Path


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_fixture(fixture):
    loop_id = fixture["initial"]["loop"]["id"]
    active_scopes = {
        scope_id
        for scope_id, scope in fixture["initial"].get("increments", {}).items()
        if not scope.get("terminal_disposition")
    }
    gates = {}

    for step in fixture.get("steps", []):
        if step.get("action") == "set_gate" and step.get("gate") == "G5_CONTRACT_CHANGE":
            gates[step.get("scope")] = step

        if step.get("action") != "contract_change_approved":
            continue

        proposal = step.get("proposal")
        gate = gates.get(loop_id)
        if not gate:
            return "CONTRACT_CHANGE_NOT_APPROVED"
        if gate.get("status") == "UNKNOWN":
            return "UNKNOWN_GATE"
        if gate.get("status") != "SATISFIED":
            return "UNSATISFIED_GATE"
        if not gate.get("record"):
            return "GATE_WITHOUT_AUTHORITY_RECORD"
        if not gate.get("human_decision"):
            return "CONTRACT_CHANGE_NOT_HUMAN_APPROVED"
        if gate.get("target_proposal") != proposal:
            return "STALE_CONTRACT_CHANGE_GATE"

        effectivity = step.get("effectivity") or {}
        if set(effectivity) != active_scopes:
            return "AMBIGUOUS_CONTRACT_EFFECTIVITY"

        new_revision = step.get("new_contract_revision")
        for scope_id in active_scopes:
            determination = effectivity[scope_id]
            if not determination.get("determination_record"):
                return "AMBIGUOUS_CONTRACT_EFFECTIVITY"
            classification = determination.get("classification")
            prior_revision = fixture["initial"]["increments"][scope_id].get("contract_revision")
            if classification == "UNAFFECTED":
                if determination.get("governing_contract_revision") != prior_revision:
                    return "BAD_UNAFFECTED_EFFECTIVITY"
            elif classification == "AFFECTED":
                if determination.get("governing_contract_revision") != new_revision:
                    return "BAD_AFFECTED_EFFECTIVITY"
                if determination.get("action") not in {"REPLAN", "BLOCK"}:
                    return "AFFECTED_SCOPE_ACTION_REQUIRED"
            else:
                return "BAD_EFFECTIVITY_CLASSIFICATION"

    return None


def main():
    protocol = load(sys.argv[1])
    fixtures = load(sys.argv[2])

    if "G5_CONTRACT_CHANGE" not in protocol.get("gates", {}):
        print("FAIL: protocol missing G5_CONTRACT_CHANGE")
        return 1

    failures = []
    for fixture in fixtures.get("scenarios", []):
        error = validate_fixture(fixture)
        got = "FAIL" if error else "PASS"
        expected = fixture.get("expect")
        expected_error = fixture.get("expected_error")
        ok = got == expected and (expected != "FAIL" or expected_error == error)
        status = "PASS" if ok else "FAIL"
        print(
            f"{status}: {fixture['id']} expected={expected}"
            + (f"/{expected_error}" if expected_error else "")
            + f" got={got}"
            + (f"/{error}" if error else "")
        )
        if not ok:
            failures.append(fixture["id"])

    if failures:
        print("G5/effectivity integrity FAILED:", ", ".join(failures))
        return 1

    print(f"G5/effectivity integrity PASSED: {len(fixtures.get('scenarios', []))} fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
