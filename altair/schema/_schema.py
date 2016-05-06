import os
import json

SCHEMA_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'vega-lite-schema.json')

with open(SCHEMA_FILE) as f:
    SCHEMA = json.load(f)
