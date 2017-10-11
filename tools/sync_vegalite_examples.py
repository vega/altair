"""
Script for syncing Altair with Vegalite
"""
import os
from altair_tools.syncing import sync_examples, path_within_altair


sync_examples(vegalite_version='v1.2.1',
              destination=path_within_altair('v1', 'examples', 'json'))
sync_examples(vegalite_version='v2.0.0-beta.11',
              destination=path_within_altair('v2', 'examples', 'json'))
