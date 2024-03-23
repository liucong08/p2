# File_name: handle_path
# Date: 2024-03-20
from pathlib import Path

class PollyPath:
    root_path = Path(__file__).parent.parent  # 项目路径
    data_path = root_path / 'testDatas'
    outFiles_path = root_path / 'outFiles'
    reports_path = outFiles_path / 'reports'
    configs_path = root_path / 'configs'

if __name__ == '__main__':
    print(PollyPath.root_path)
    print(PollyPath.data_path)