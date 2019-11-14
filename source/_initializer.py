"""
_initializer.py

an initializer for constants

"""

import os, sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# get basic setting from settings.json
with open(f'{BASE_DIR}/json/settings.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# make directory for log and search history
os.makedirs(f'{BASE_DIR}/log/', exist_ok=True)
os.makedirs(f'{BASE_DIR}/log/index/', exist_ok=True)
os.makedirs(f'{BASE_DIR}/log/count/', exist_ok=True)
os.makedirs(f'{BASE_DIR}/log/search_history/', exist_ok=True)
