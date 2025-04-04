# ### Built-in deps
from typing import Any, Dict

# ### Third-party deps
import yaml

# ### Local deps


def read_yaml_file(file_path) -> Dict[str, Any]:
    with open(file_path) as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)
