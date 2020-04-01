#!/usr/bin/env python3

# quick tool to get nicer filenames
import sys

url = sys.argv[1].split('?')[0].split('/')[-1]
print(url)
