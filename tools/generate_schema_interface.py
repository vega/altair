from altair_tools.generate_interface_v1 import generate_interface_v1
from altair_tools.generate_interface_v2 import generate_interface_v2
from altair_tools.utils import path_within_altair

generate_interface_v1(schema_path=path_within_altair('v1', 'schema'))
generate_interface_v2(schema_path=path_within_altair('v2', 'schema'))
