"""
Script for syncing Altair with Vegalite
"""
import os
from altair_tools.syncing import sync_datasets, path_within_altair

sync_datasets(datasets_version='v1.8.0',
              destination=path_within_altair('datasets'))
