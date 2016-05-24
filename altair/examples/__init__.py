"""Code for Example Plots"""
import os
import json

JSON_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'json'))


def load_example(filename):
    """Load the JSON dict corresponding to the given filename"""
    if filename not in os.listdir(JSON_DIR):
        raise ValueError("Example='{0}' not valid.".format(filename))

    with open(os.path.join(JSON_DIR, filename)) as f:
        return json.load(f)


def iter_examples():
    """Iterate all example files & their contents

    Iterator returns tuples of (filename, JSON_dict)
    """
    for filename in os.listdir(JSON_DIR):
        yield filename, load_example(filename)
