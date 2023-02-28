import re
import yaml
import sys

# 初期設定
CONFIGURE_FILES_LIST_FILE = 1
WORKING_DIRECTORY = 2

# 利用中の機材
CATALYST2960S = "catalyst2960s"

# 利用中の機材一覧
DEVICE_TYPE = [CATALYST2960S]


# ネットワーク機器の解析用親クラス
class analyze_network_configure:
    interface_keywords = []
    routing_keywords = []

    def __init__(self, device_type, config_file_path):
        self.device_type = device_type
        self.config_file_path = config_file_path

    def interfaces(self):
        pass

    def routing(self):
        pass

    def array_to_csv(self, array):
        pass


# Cisco Catalyst 2960S
class analyze_catalyst2960s(analyze_network_configure):
    # Github Copilot で自動生成したコード
    # interface_keywords = ["interface", "switchport", "spanning-tree", "description"]
    # routing_keywords = ["ip", "ip route", "ip access-list", "ip prefix-list"]

    def __init__(self, device_type, config_file_path):
        super().__init__(device_type, config_file_path)
        self.interface_keywords = [
            "interface.*",
            ".*description.*",
            ".*switchport.*mode.*",
            ".*switchport.*access.*vlan.*",
            ".*switchport.*trunk.*allowed.*vlan.*",
            ".*switchport.*trunk.*native.*vlan.*",
            ".*ip\s.*",
        ]

    def interfaces(self):
        interface_config_list = []

        with open(self.config_file_path) as file:
            pattern = re.compile(r"interface(.+?\n)\!", re.MULTILINE | re.DOTALL)
            for match in pattern.finditer(file.read()):
                interface_config_list.append(match.group(0))

        for _interface_config in interface_config_list:
            match = []
            for keyword in self.interface_keywords:
                match.append(re.findall(keyword, _interface_config))
        print(match)

    def routing(self):
        pass

    def array_to_csv(self, array):
        pass


# 引数のチェック
args = sys.argv

if len(sys.argv) <= CONFIGURE_FILES_LIST_FILE:
    sys.exit("Error: Please specify the configure files list file.")

if len(sys.argv) <= WORKING_DIRECTORY:
    sys.exit("Error: Please specify the working directory.")

# main function
if __name__ == "__main__":
    working_directory = args[WORKING_DIRECTORY]
    with open(args[CONFIGURE_FILES_LIST_FILE]) as f:
        configure_files_paths = yaml.safe_load(f)

    for device_type in DEVICE_TYPE:
        for config_file_path in configure_files_paths[device_type]:
            print(analyze_catalyst2960s(device_type, f"{working_directory}{config_file_path}").interfaces())
            pass

# regex to find all interface config
# pattern = re.compile(r"interface(.+?\n)\!", re.MULTILINE | re.DOTALL)
