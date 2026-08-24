#!/usr/bin/env python3
import argparse, hashlib, json, shutil
from pathlib import Path

def sha256(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()

def resolve(root, selectors):
 out=[]
 for s in selectors:
  for p in root.glob(s):
   if p.is_file() and '.git' not in p.parts: out.append(p)
 return sorted(set(out))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--repo',default='.'); ap.add_argument('--output',required=True); a=ap.parse_args()
 repo=Path(a.repo).resolve(); out=Path(a.output).resolve()
 if out.exists(): shutil.rmtree(out)
 out.mkdir(parents=True)
 manifest=json.loads((repo/'canonical_ae_release_manifest.json').read_text())
 roles={repo/'canonical_ae_release_manifest.json':'RELEASE_AUTHORITY'}
 for layer,info in manifest['semantic_layers'].items():
  for p in resolve(repo, info['selectors']):
   if p.name=='reference/fixtures/clean_room_adoption_baseline.json': continue
   roles.setdefault(p,layer)
 for group,info in manifest.get('supporting_content',{}).items():
  for p in resolve(repo, info['selectors']): roles.setdefault(p,'SUPPORTING_'+group)
 inventory=[]
 for src,role in sorted(roles.items(),key=lambda x:str(x[0].relative_to(repo))):
  rel=src.relative_to(repo); dst=out/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,dst)
  inventory.append({'path':str(rel),'role':role,'sha256':sha256(dst),'bytes':dst.stat().st_size})
 inv={
  'release_id':manifest['release_id'],
  'release_version':manifest['release_version'],
  'distribution_revision':manifest.get('distribution_revision',1),
  'integrity_algorithm':'SHA-256',
  'artifacts':inventory
 }
 (out/'RELEASE_INVENTORY.json').write_text(json.dumps(inv,indent=2)+'\n')
 print(f"assembled {len(inventory)} artifacts for {manifest['release_id']} distribution revision {inv['distribution_revision']} at {out}")
if __name__=='__main__': main()
