import json
import requests
import subprocess
import sys

domain_list = []

# Censys.io access
censys_API_ID = "<censys_API_ID>"
censys_secret = "<censys_secret>"
censys_basic_auth = (censys_API_ID, censys_secret)

# Amass binary and output file
amass_binary = "amass"
amass_output = "amass_dns.txt"

# Sonar fdns file and output file
# Download link: https://opendata.rapid7.com/sonar.fdns_v2/2019-06-21-1561158121-fdns_cname.json.gz
sonar_fdns_data = "2019-06-21-1561158121-fdns_cname.json.gz"
sonar_output = "sonar_output.txt"


def usage():
    print("[*] Usage - python3 PyDNSRecon.py <target>")


def banner():
    print("    ____        ____  _   _______ ____")
    print("   / __ \__  __/ __ \/ | / / ___// __ \___  _________  ____")
    print("  / /_/ / / / / / / /  |/ /\__ \/ /_/ / _ \/ ___/ __ \/ __ \\")
    print(" / ____/ /_/ / /_/ / /|  /___/ / _, _/  __/ /__/ /_/ / / / /")
    print("/_/    \__, /_____/_/ |_//____/_/ |_|\___/\___/\____/_/ /_/")
    print("      /____/")
    print("")
    print("by: sneakerhax")
    print("")


def censys_cert_search(censys_target, domain_list):
    print("[+] Running Censys.io certificate search on " + str(censys_target))
    censys_url = "https://censys.io/api/v1/search/certificates"
    payload = "{\n    \"query\": \"" + censys_target + "\",\n    \"fields\": [\"parsed.subject.common_name\"]\n}"
    headers = {'Content-Type': "application/json", 'Host': "censys.io"}
    response = requests.request("POST", censys_url, data=payload, headers=headers, auth=censys_basic_auth)
    json_response = response.json()
    for result in json_response['results']:
        if censys_target in result['parsed.subject.common_name'][0]:
            domain_list.append(result['parsed.subject.common_name'][0])


def amass_dns_active(amass_target, amass_output, domain_list):
    print("[+] Running Amass on " + amass_target)
    amass = subprocess.Popen([amass_binary, '-d', amass_target, '-o', amass_output], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    amass.communicate()
    with open(amass_output, 'r') as amass_open:
        for result in amass_open:
            domain_list.append(result)


def sonar_zgrep_search(sonar_target, sonary_output, sonar_fdns_data, domain_list):
    print("[+] Running Zgrep on Sonar fdns data for " + sonar_target)
    with open(sonar_output, "w") as out:
        zgrep = subprocess.Popen(['zgrep', '-a', '-w', sonar_target, sonar_fdns_data], stdout=out)
        zgrep.communicate()
        with open(sonar_output, "r") as sonar:
            for result in sonar:
                json_string = json.loads(result)
                if sonar_target in json_string['name']:
                    domain_list.append(json_string['name'])


def crtsh_cert_search(crtsh_target, domain_list):
    print("[+] Running crt.sh search for " + crtsh_target)
    crtsh_search = f"https://crt.sh/?q={crtsh_target}&output=json"
    response = requests.get(crtsh_search).json()
    for result in response:
        if "\n" in result['name_value']:
            split_items = result['name_value'].split('\n')
            for item in split_items:
                domain_list.append((item.rstrip()))
        else:
            domain_list.append((result['name_value'].rstrip()))


def main():
    if len(sys.argv) == 2:
        banner()
        target = sys.argv[1]
        censys_cert_search(target, domain_list)
        amass_dns_active(target, amass_output, domain_list)
        sonar_zgrep_search(target, sonar_output, sonar_fdns_data, domain_list)
        crtsh_cert_search(target, domain_list)
        unique_domains = set(domain_list)
        print("[+] Printing " + str(len(unique_domains)) + " discovered DNS records")
        for domain in unique_domains:
            print(domain.rstrip())
    else:
        banner()
        usage()


if __name__ == '__main__':
    main()
