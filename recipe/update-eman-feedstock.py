#!/usr/bin/python


import requests
from pathlib import Path


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
			words[4] = f'"{version}"'
			l = ' '.join(words) + '\n'
			fout.write(l)

		else:
			fout.write(line)

recipe_new.rename(recipe)
