#!/usr/bin/python


import requests
from pathlib import Path
import subprocess as sp


# tags_response = requests.get('https://api.github.com/repos/cryoem/eman2/tags').json()
tags_response = [{'name': 'v2.99.33', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.99.33', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.99.33', 'commit': {'sha': '8a24bb112b5837b69fa6c0696c7ae1b88262a637', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/8a24bb112b5837b69fa6c0696c7ae1b88262a637'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjk5LjMz'},
                 {'name': 'v2.91', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.91', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.91', 'commit': {'sha': '81caed29e2b007820ff478fb6a737c64ca4d9152', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/81caed29e2b007820ff478fb6a737c64ca4d9152'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjkx'},
                 {'name': 'v2.31', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.31', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.31', 'commit': {'sha': '194df9590980c04831c79c79058232c03b8268bb', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/194df9590980c04831c79c79058232c03b8268bb'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjMx'},
                 {'name': 'v2.22', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.22', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.22', 'commit': {'sha': 'f4f3952bdefa462c6d05ecf19a6fa3ca0d7e368b', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/f4f3952bdefa462c6d05ecf19a6fa3ca0d7e368b'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjIy'},
                 {'name': 'v2.21', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.21', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.21', 'commit': {'sha': 'eac9c01bd46953132040318a6344d257853a8819', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/eac9c01bd46953132040318a6344d257853a8819'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjIx'},
                 {'name': 'v2.21a-windows', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.21a-windows', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.21a-windows', 'commit': {'sha': '8d7bd97ccf485b110ba5156c5fa63e7da71165a9', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/8d7bd97ccf485b110ba5156c5fa63e7da71165a9'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjIxYS13aW5kb3dz'},
                 {'name': 'v2.21a', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.21a', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.21a', 'commit': {'sha': 'c573a6e69183c2b223815578647d363d4bdf12be', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/c573a6e69183c2b223815578647d363d4bdf12be'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjIxYQ=='},
                 {'name': 'v2.9', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.9', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.9', 'commit': {'sha': '0e88d0ac6de941fe1e9a2bbbec861d403fa8544e', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/0e88d0ac6de941fe1e9a2bbbec861d403fa8544e'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjk='},
                 {'name': 'v2.3', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.3', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.3', 'commit': {'sha': '6aaac88e2763318efb61ae5a06681e9357f81adf', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/6aaac88e2763318efb61ae5a06681e9357f81adf'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjM='},
                 {'name': 'v2.2', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/v2.2', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/v2.2', 'commit': {'sha': '089c0b11ead517d2ed0ed128c058f7ccf4de5036', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/089c0b11ead517d2ed0ed128c058f7ccf4de5036'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3YyLjI='},
                 {'name': 'python2', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/python2', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/python2', 'commit': {'sha': '61f0c094b16014bad7a7ef4d86f58c17833f5082', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/61f0c094b16014bad7a7ef4d86f58c17833f5082'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzL3B5dGhvbjI='},
                 {'name': 'v2.99.34', 'zipball_url': 'https://api.github.com/repos/cryoem/eman2/zipball/refs/tags/2.99.34', 'tarball_url': 'https://api.github.com/repos/cryoem/eman2/tarball/refs/tags/2.99.34', 'commit': {'sha': 'af645535e9c303c9f97fd1377062a1756c0c9c08', 'url': 'https://api.github.com/repos/cryoem/eman2/commits/af645535e9c303c9f97fd1377062a1756c0c9c08'}, 'node_id': 'MDM6UmVmNDgwNjQ3Njc6cmVmcy90YWdzLzIuOTkuMzQ='}]

print(tags_response)

tags = [t['name'] for t in requests.get('https://api.github.com/repos/cryoem/eman2/tags').json()]
tags = ['v2.99.33', 'v2.99.34', 'v2.91', 'v2.31', 'v2.22', 'v2.21', 'v2.21a-windows', 'v2.21a', 'v2.9', 'v2.3', 'v2.2', 'python2']
print(f"Received GitHub tags:\n{tags}")

tags = sorted([t for t in tags if t.startswith('v')], reverse=True)
print(f"Version tags (sorted: latest to oldest):\n{tags}")

tag = tags[0]
# tag ='v2.99.33'
# tag ='v2.99'
# tag ='v2'
version = tag[1:]

print(f"Latest tag:\n{tag}")
print(f"Latest version:\n{version}")

# Update recipe with latest version
recipe = 'recipe'/ Path('meta.yaml')
recipe_new = 'recipe'/ Path('meta.yaml.new')

with open(recipe, mode='r') as fin, open((recipe_new), mode='w') as fout:
	for line in fin:
		words = line.split()
		# if 'set' in line and 'version' in line:
		if ' '.join(words[1:4]) == 'set version =':
			print(line)
			print(words)
			words[4] = f'"{version}"'
			print(words)
			# words = line.split()
			# l = '{% set version = "' + tag + '" %}'
			l = ' '.join(words) + '\n'
# 			l = line.partition(":")
			print(l)
#
# 			build_num = str(int(l[2].strip()) + 1)
# 			l = l[0] + l[1] + ' ' + build_num + '\n'
#
# 			print(l)
			fout.write(l)

# 			with open('build.num', 'w') as fnum:
# 				fnum.write(build_num)
		else:
			fout.write(line)

recipe_new.rename(recipe)

# Run subcommands: git operations
for cmd in (
            'git status',
            'git branch -a',
            'git branch -D jenkins',
            'git checkout -b jenkins',
            'git add recipe/meta.yaml',
            f'git commit -m {tag}',
           ):
	cmd = cmd.split()
	print(cmd)
	proc = sp.run(cmd, capture_output=True, check=False)
	print(f'{proc.stdout=}')
	print(f'{proc.stderr=}')
