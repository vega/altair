"""Code for Example Plots"""


def load_example(name):
    import os
    import json

    JSON_DIR = os.path.join(os.path.dirname(__file__), 'json')
    if name not in os.listdir(JSON_DIR):
        raise ValueError("Example='{0}' not valid.".format(name))

    with open(os.path.join(JSON_DIR, name)) as f:
        schema = json.load(f)

    return schema
