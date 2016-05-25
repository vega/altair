import os
import json

SCHEMA_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'vega-lite-schema.json')

def load_schema():
    """Load the VegaLite Schema as a Python dictionary"""
    with open(SCHEMA_FILE) as f:
        return json.load(f)
