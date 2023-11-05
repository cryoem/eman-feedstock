#!/usr/bin/python


import requests
from pathlib import Path
import subprocess as sp


tags = [t['name'] for t in requests.get('https://api.github.com/repos/cryoem/eman2/tags').json()]
print(f"Received GitHub tags:\n{tags}")

tags = sorted([t for t in tags if t.startswith('v')], reverse=True)
print(f"Version tags (sorted: latest to oldest):\n{tags}")

tag = tags[0]
version = tag[1:]

print(f"Latest tag:\n{tag}")
print(f"Latest version:\n{version}")

# Update recipe with latest version
recipe = 'recipe'/ Path('meta.yaml')
recipe_new = 'recipe'/ Path('meta.yaml.new')

with open(recipe, mode='r') as fin, open((recipe_new), mode='w') as fout:
	for line in fin:
		words = line.split()
		if ' '.join(words[1:4]) == 'set version =':
			print(line)
			print(words)
			words[4] = f'"{version}"'
			print(words)
			l = ' '.join(words) + '\n'
			print(l)
			fout.write(l)

		else:
			fout.write(line)

recipe_new.rename(recipe)

# Run subcommands: git operations
for cmd in (
            'git config --global user.email "eman.github@gmail.com"',
            'git config --global user.name "eman-bot"',
            'git add recipe/meta.yaml',
            f'git commit -m {tag}',
            'git push origin master',
           ):
	cmd = cmd.split()
	print(f'> {" ".join(cmd)}')
	proc = sp.run(cmd, capture_output=True, check=False)
	print(proc.stdout)
	if proc.returncode != 0:
		print(f'stderr:\n{proc.stderr=}')
