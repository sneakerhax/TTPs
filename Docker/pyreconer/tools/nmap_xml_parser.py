#!/usr/bin/env python

__author__ = 'Jake Miller (@LaconicWolf)'
__date__ = '20171220'
__version__ = '0.01'
__description__ = """Parses the XML output from an nmap scan. The user
                  can specify whether the data should be printed,
                  displayed as a list of IP addresses, or output to
                  a csv file. Will append to a csv if the filename
                  already exists.
                  """

import xml.etree.ElementTree as etree
import os
import csv
import argparse
from collections import Counter
from time import sleep

def get_host_data(root):
    """Traverses the xml tree and build lists of scan information
    and returns a list of lists.
    """
    host_data = []
    hosts = root.findall('host')
    for host in hosts:
        addr_info = []

        # Ignore hosts that are not 'up'
        if not host.findall('status')[0].attrib['state'] == 'up':
            continue
        
        # Get IP address and host info. If no hostname, then ''
        ip_address = host.findall('address')[0].attrib['addr']
        host_name_element = host.findall('hostnames')
        try:
            host_name = host_name_element[0].findall('hostname')[0].attrib['name']
        except IndexError:
            host_name = ''
        
        # If we only want the IP addresses from the scan, stop here
        if args.ip_addresses:
            addr_info.extend((ip_address, host_name))
            host_data.append(addr_info)
            continue
        
        # Get the OS information if available, else ''
        try:
            os_element = host.findall('os')
            os_name = os_element[0].findall('osmatch')[0].attrib['name']
        except IndexError:
            os_name = ''
        
        # Get information on ports and services
        try:
            port_element = host.findall('ports')
            ports = port_element[0].findall('port')
            for port in ports:
                port_data = []

                if args.udp_open:
                    # Display both open ports and open}filtered ports
                    if not 'open' in port.findall('state')[0].attrib['state']:
                        continue
                else:
                    # Ignore ports that are not 'open'
                    if not port.findall('state')[0].attrib['state'] == 'open':
                        continue
                
                proto = port.attrib['protocol']
                port_id = port.attrib['portid']
                service = port.findall('service')[0].attrib['name']
                try:
                    product = port.findall('service')[0].attrib['product']
                except (IndexError, KeyError):
                    product = ''      
                try:
                    servicefp = port.findall('service')[0].attrib['servicefp']
                except (IndexError, KeyError):
                    servicefp = ''
                try:
                    script_id = port.findall('script')[0].attrib['id']
                except (IndexError, KeyError):
                    script_id = ''
                try:
                    script_output = port.findall('script')[0].attrib['output']
                except (IndexError, KeyError):
                    script_output = ''

                # Create a list of the port data
                port_data.extend((ip_address, host_name, os_name,
                                  proto, port_id, service, product, 
                                  servicefp, script_id, script_output))
                
                # Add the port data to the host data
                host_data.append(port_data)

        # If no port information, just create a list of host information
        except IndexError:
            addr_info.extend((ip_address, host_name))
            host_data.append(addr_info)
    return host_data

def parse_xml(filename):
    """Given an XML filename, reads and parses the XML file and passes the 
    the root node of type xml.etree.ElementTree.Element to the get_host_data
    function, which will futher parse the data and return a list of lists
    containing the scan data for a host or hosts."""
    try:
        tree = etree.parse(filename)
    except Exception as error:
        print("[-] A an error occurred. The XML may not be well formed. "
              "Please review the error and try again: {}".format(error))
        exit()
    root = tree.getroot()
    scan_data = get_host_data(root)
    return scan_data

def parse_to_csv(data):
    """Given a list of data, adds the items to (or creates) a CSV file."""
    if not os.path.isfile(csv_name):
        csv_file = open(csv_name, 'w', newline='')
        csv_writer = csv.writer(csv_file)
        top_row = [
            'IP', 'Host', 'OS', 'Proto', 'Port',
            'Service', 'Product', 'Service FP',
            'NSE Script ID', 'NSE Script Output', 'Notes'
        ]
        csv_writer.writerow(top_row)
        print('\n[+] The file {} does not exist. New file created!\n'.format(
                csv_name))
    else:
        try:
            csv_file = open(csv_name, 'a', newline='')
        except PermissionError as e:
            print("\n[-] Permission denied to open the file {}. "
                  "Check if the file is open and try again.\n".format(csv_name))
            print("Print data to the terminal:\n")
            if args.debug:
                print(e)
            for item in data:
                print(' '.join(item))
            exit()
        csv_writer = csv.writer(csv_file)
        print('\n[+] {} exists. Appending to file!\n'.format(csv_name))
    for item in data:
        csv_writer.writerow(item)
    csv_file.close()        

def list_ip_addresses(data):
    """Parses the input data to return only the IP address information"""
    ip_list = [item[0] for item in data]
    sorted_set = sorted(set(ip_list))
    addr_list = [ip for ip in sorted_set]
    return addr_list

def print_web_ports(data):
    """Examines the port information and prints out the IP and port 
    info in URL format (https://ipaddr:port/).
    """

    # http and https port numbers came from experience as well as
    # searching for http on th following website:
    # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    http_port_list = ['80', '280', '81', '591', '593', '2080', '2480', '3080', 
                      '4080', '4567', '5080', '5104', '5800', '6080',
                      '7001', '7080', '7777', '8000', '8008', '8042', '8080',
                      '8081', '8082', '8088', '8180', '8222', '8280', '8281',
                      '8530', '8887', '9000', '9080', '9090', '16080']                    
    https_port_list = ['832', '981', '1311', '7002', '7021', '7023', '7025',
                       '7777', '8333', '8531', '8888']
    for item in data:
        ip = item[0]
        port = item[4]
        if port.endswith('43') and port != "143" or port in https_port_list:
            print("https://{}:{}".format(ip, port))
        elif port in http_port_list:
            print("http://{}:{}".format(ip, port))
        else:
            continue    
    
def least_common_ports(data, n):
    """Examines the port index from data and prints the least common ports."""
    c = Counter()
    for item in data:
        try:
            port = item[4]
            c.update([port])
        except IndexError as e:
            if args.debug:
                print(e)
            continue
    print("{0:8} {1:15}\n".format('PORT', 'OCCURENCES'))
    for p in c.most_common()[:-n-1:-1]:
        print("{0:5} {1:8}".format(p[0], p[1]))

def most_common_ports(data, n):
    """Examines the port index from data and prints the most common ports."""
    c = Counter()
    for item in data:
        try:
            port = item[4]
            c.update([port])
        except IndexError as e:
            if args.debug:
                print(e)
            continue
    print("{0:8} {1:15}\n".format('PORT', 'OCCURENCES'))
    for p in c.most_common(n):
        print("{0:5} {1:8}".format(p[0], p[1]))

def print_filtered_port(data, filtered_port):
    """Examines the port index from data and see if it matches the 
    filtered_port. If it matches, print the IP address.
    """
    for item in data:
        try:
            port = item[4]
        except IndexError as e:
            if args.debug:
                print(e)
            continue
        if port == filtered_port:
            print(item[0])

def print_data(data):
    """Prints the data to the terminal."""
    for item in data:
        print(' '.join(item))

def main():
    """Main function of the script."""
    for filename in args.filename:

        # Checks the file path
        if not os.path.exists(filename):
            parser.print_help()
            print("\n[-] The file {} cannot be found or you do not have "
                  "permission to open the file.".format(filename))
            continue

        if not args.skip_entity_check:
            # Read the file and check for entities
            with open(filename) as fh:
                contents = fh.read()
                if '<!entity' in contents.lower():
                    print("[-] Error! This program does not permit XML "
                          "entities. Ignoring {}".format(filename))
                    print("[*] Use -s (--skip_entity_check) to ignore this "
                          "check for XML entities.")
                    continue
        data = parse_xml(filename)
        if not data:
            print("[*] Zero hosts identitified as 'Up' or with 'open' ports. "
                  "Use the -u option to display ports that are 'open|filtered'. "
                  "Exiting.")
            exit()
        if args.csv:
            parse_to_csv(data)
        if args.ip_addresses:
            addrs = list_ip_addresses(data)
            for addr in addrs:
                print(addr)
        if args.print_all:
            print_data(data)
        if args.filter_by_port:
            print_filtered_port(data, args.filter_by_port)
        if args.print_web_ports:
            print_web_ports(data)
        if args.least_common_ports:
            print("\n{} LEAST COMMON PORTS".format(filename.upper()))
            least_common_ports(data, args.least_common_ports)
        if args.most_common_ports:
            print("\n{} MOST COMMON PORTS".format(filename.upper()))
            most_common_ports(data, args.most_common_ports)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",
                        help="Display error information",
                        action="store_true")
    parser.add_argument("-s", "--skip_entity_check",
                        help="Skip the check for XML entities",
                        action="store_true")
    parser.add_argument("-p", "--print_all",
                        help="Display scan information to the screen", 
                        action="store_true")
    parser.add_argument("-pw", "--print_web_ports",
                        help="Display IP addresses/ports in URL format "
                             "(http://ipaddr:port)",
                        action="store_true")
    parser.add_argument("-ip", "--ip_addresses",
                        help="Display a list of ip addresses",
                        action="store_true")
    parser.add_argument("-csv", "--csv",
                        nargs='?', const='scan.csv',
                        help="Specify the name of a csv file to write to. "
                             "If the file already exists it will be appended")
    parser.add_argument("-f", "--filename",
                        nargs='*',
                        help="Specify a file containing the output of an nmap "
                             "scan in xml format.")
    parser.add_argument("-lc","--least_common_ports",
                        type=int, 
                        help="Displays the least common open ports.")
    parser.add_argument("-mc", "--most_common_ports",
                        type=int, 
                        help="Displays the most common open ports.")
    parser.add_argument("-fp", "--filter_by_port", 
                        help="Displays the IP addresses that are listenting on "
                             "a specified port")
    parser.add_argument("-u", "--udp_open", 
                        help="Displays the UDP ports identified as "
                             "open|filtered",
                        action="store_true")
    args = parser.parse_args()

    if not args.filename:
        parser.print_help()
        print("\n[-] Please specify an input file to parse. "
              "Use -f <nmap_scan.xml> to specify the file\n")
        exit()
    if not args.ip_addresses and not args.csv and not args.print_all \
                and not args.print_web_ports and not args.least_common_ports \
                and not args.most_common_ports and not args.filter_by_port:
        parser.print_help()
        print("\n[-] Please choose an output option. Use -csv, -ip, or -p\n")
        exit()
    csv_name = args.csv
    main()