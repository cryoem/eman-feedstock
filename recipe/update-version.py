#!/usr/bin/python


import requests


tags = [t['name'] for t in requests.get('https://api.github.com/repos/cryoem/eman2/tags').json()]
print(f"Received GitHub tags:\n{tags}")

tags = sorted([t for t in tags if t.startswith('v')], reverse=True)
print(f"Version tags (sorted: latest to oldest):\n{tags}")

tag = tags[0]
version = tag[1:]

print(f"Latest tag:\n{tag}")
print(f"Latest version:\n{version}")
