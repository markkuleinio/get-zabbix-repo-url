import re
import sys
import urllib.request


zabbix_version = sys.argv[1]
name_suffix = sys.argv[2]

base_url = f"https://repo.zabbix.com/zabbix/{zabbix_version}/debian/pool/main/z/zabbix-release/"
with urllib.request.urlopen(base_url) as f:
    for line in f.read().decode("utf-8").splitlines():
        if name_suffix in line:
            last_filename = re.search(r">(.*)<", line).group(1)
print(f"{base_url}{last_filename}")
