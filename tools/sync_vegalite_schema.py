"""
Script for syncing Altair with Vegalite
"""
import os
from altair_tools.syncing import sync_schema, path_within_altair


sync_schema(vegalite_version='v1.2.1',
            schema_path=path_within_altair('v1', 'schema'))
sync_schema(vegalite_version='v2.0.0-beta.11',
            schema_path=path_within_altair('v2', 'schema'))
