#!/usr/bin/python


import os
from pathlib import Path
import subprocess as sp


version = os.environ['new_version']

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

		elif ' '.join(words[1:4]) == 'set build =' and len(words) == 6:
			print(line)
			print(words)
			words[4] = '0'
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
            f'git commit -m v{version}',
            'git push origin master',
           ):
	cmd = cmd.split()
	print(f'> {" ".join(cmd)}')
	proc = sp.run(cmd, capture_output=True, check=False)
	print(proc.stdout)
	if proc.returncode != 0:
		print(f'stderr:\n{proc.stderr=}')
