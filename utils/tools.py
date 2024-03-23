# File_name: tools
# Date: 2024-03-20
import yaml

from utils.handle_path import PollyPath
from pprint import pprint

def get_yaml_data(yaml_file):
    with open(yaml_file, encoding='utf-8') as f:
        return yaml.safe_load(f)

if __name__ == '__main__':
    # pprint(get_yaml_data(PollyPath.data_path / 'login_fail_data.yaml'))  # 相对路径
    pprint(get_yaml_data(PollyPath.configs_path / 'allelements.yaml'))