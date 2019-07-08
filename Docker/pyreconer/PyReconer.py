import subprocess
import sys

# Tool locations
amass_binary = "amass/amass"
aquatone_binary = "aquatone/aquatone"
chromium_binary = "chrome-linux/chrome"
nmap_binary = "nmap"
nmap_scan_to_csv = "Nmap-Scan-to-CSV/nmap_xml_parser.py"
python_binary = "python"

# Output files
amass_output = "output/amass_results.txt"
nmap_output = "output/nmap_results"
nmap_output_csv = "output/nmap_results.csv"
nmap_output_xml = "output/nmap_results.xml"
aquatone_output = "output/"


def banner():
    print("#######################")
    print("##     PyReconer     ##")
    print("##  by: sneakerhax   ##")
    print("#######################")


def usage():
    print("python3 PyReconer.py <target>")


def amass_dns_active(amass_targets, amass_output):
    print("[+] Running amass on " + amass_targets)
    amass = subprocess.Popen([amass_binary, 'enum', '-o', amass_output, '-d', amass_targets], stdout=subprocess.PIPE)
    out, err = amass.communicate()
    print(out.decode('utf-8'))


def nmap_top_ports(nmap_targets, nmap_output):
    print("[+] Running nmap on " + amass_output)
    nmap = subprocess.Popen([nmap_binary, '--top-ports', "1000", '-Pn', '--open', '--reason', '-iL', nmap_targets, '-oA', nmap_output], stdout=subprocess.PIPE)
    out, err = nmap.communicate()
    print(out.decode('utf-8'))


def nmap_convert_csv():
    print("[+] Converting Nmap XML to CSV ")
    nmap = subprocess.Popen([python_binary, nmap_scan_to_csv, '-f', nmap_output_xml, '-csv', nmap_output_csv], stdout=subprocess.PIPE)
    out, err = nmap.communicate()
    print(out.decode('utf-8'))


def aquatone_screen_grab():
    print("[+] Running aquatone on " + nmap_output_xml)
    aquatone_nmap_file = subprocess.Popen(['cat', nmap_output_xml], stdout=subprocess.PIPE)
    aquatone_run = subprocess.Popen([aquatone_binary, '-nmap', '--chrome-path', chromium_binary, '-out', aquatone_output], stdin=aquatone_nmap_file.stdout, stdout=subprocess.PIPE)
    out, err = aquatone_run.communicate()
    print(out.decode('utf-8'))


def main():
    if len(sys.argv) == 2:
        banner()
        target = sys.argv[1]
        amass_dns_active(target, amass_output)
        nmap_top_ports(amass_output, nmap_output)
        nmap_convert_csv()
        aquatone_screen_grab()
    else:
        banner()
        usage()


if __name__ == "__main__":
    main()
