import ipaddress
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pysnmp.hlapi import *
from tqdm import tqdm
import sys

parser = argparse.ArgumentParser(description='Retrieve SNMP system.sysDescr.0 MIB value from a subnet by default.')
parser.add_argument('-c', '--community', required=True, help='SNMP community string.')
parser.add_argument('-i', '--ip', required=True, help='IP address or CIDR notation of the subnet.')
parser.add_argument('-t', '--timeout', type=int, default=1000, help='Timeout value in milliseconds (default 1000).')
parser.add_argument('-o', '--output', help='Output file name.')
parser.add_argument('-m', '--mib', default='1.3.6.1.2.1.1.1.0', help='MIB OID number (Default: system.sysDescr.0 - OID: 1.3.6.1.2.1.1.1.0)')
parser.add_argument('-p', '--port', type=int, default=161, help='SNMP service port (default 161).')
parser.add_argument('--threads', type=int, default=10, help='Number of threads to use (default 10).')
args = parser.parse_args()

def get_sysdescr(ip_address, community, timeout):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community, mpModel=0),
               UdpTransportTarget((ip_address, args.port), timeout=timeout/1000.0, retries=0),
               ContextData(),
               ObjectType(ObjectIdentity(args.mib)))
    )

    if errorIndication:
        return None
    elif errorStatus:
        return None
    else:
        for varBind in varBinds:
            return f"{ip_address}: {varBind.prettyPrint()}"
    return None

def main():
    ip_list = [str(ip) for ip in ipaddress.IPv4Network(args.ip)]

    with ThreadPoolExecutor(max_workers=args.threads) as executor, open(args.output, 'w') as f:
        futures = {executor.submit(get_sysdescr, ip, args.community, args.timeout): ip for ip in ip_list}

        with tqdm(total=len(futures), desc="Scanning IPs", dynamic_ncols=True) as pbar:
            for future in as_completed(futures):
                result = future.result()
                if result:
                    tqdm.write(result)
                    f.write(result + '\n')
                    f.flush()
                pbar.update(1)

if __name__ == "__main__":
    main()
