import subprocess
from typing import List
from pprint import pprint
import re

TEXTVALUE = "All User Profile     : "
SECKEY = "    Security key           : "
KEYCONTENT = "    Key Content            : "


def get_wifi_list() -> List[str]:
    """

    :return: list of the wifi names
    """
    cmd_wifi_name = "netsh wlan show profiles"
    result = subprocess.check_output(cmd_wifi_name.split(), shell=True).decode("ibm850")
    wifi_names = [line.replace(TEXTVALUE, "").strip() for line in result.splitlines()
                  if TEXTVALUE in line]
    print(wifi_names)
    return wifi_names


def get_wifi_inf():
    wifi_sec_type = []
    wifi_pass = []
    wifi_auth = []
    for wifi_name in get_wifi_list():
        cmd_wifi_info = ["netsh", "wlan", "show", "profiles", wifi_name, "key=clear"]
        try:
            cmd_wifi_info_exec = subprocess.check_output(cmd_wifi_info, shell=False).decode("ibm850")
            first = True
            for line in cmd_wifi_info_exec.splitlines():
                if SECKEY in line:
                    sec_type = re.sub(SECKEY, "", line)
                    wifi_sec_type.append(sec_type)
                if SECKEY in line and "Absent" in line:
                    wifi_pass.append("--None--")

                if KEYCONTENT in line:
                    pass_w = re.sub(KEYCONTENT, "", line)
                    wifi_pass.append(pass_w)
                if "Authentication" in line and "Open" in line:
                    wifi_auth.append("Open")

                elif "Authentication" in line and first:
                    first = False
                    auth = re.sub(r"    Authentication         : ", "", line)
                    wifi_auth.append(auth)
        except subprocess.CalledProcessError:
            wifi_sec_type.append("--NONE--")
            wifi_pass.append("--NONE--")
            wifi_auth.append(auth)

    return wifi_sec_type, wifi_pass, wifi_auth
