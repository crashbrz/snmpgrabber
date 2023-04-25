rom pysnmp.hlapi import *
import ipaddress
import argparse

parser = argparse.ArgumentParser(description='Retrieve SNMP system.sysDescr.0 MIB value from a subnet by default.')
parser.add_argument('-c', '--community', required=True, help='SNMP community string.')
parser.add_argument('-i', '--ip', required=True, help='IP address or CIDR notation of the subnet.')
parser.add_argument('-t', '--timeout', type=int, default=1000, help='Timeout value in milliseconds (default 1000).')
parser.add_argument('-o', '--output', help='Output file name.')
parser.add_argument('-m', '--mib', default='1.3.6.1.2.1.1.1.0', help='MIB OID number (Default: system.sysDescr.0 - OID: 1.3.6.1.2.1.1.1.0)')
parser.add_argument('-p', '--port', type=int, default=161, help='SNMP service port (default 161).')
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
        print(ip_address + ':' +  str(errorIndication))
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            print(ip_address + ':' + varBind.prettyPrint())
            return varBind.prettyPrint()

output = ''
for ip in ipaddress.IPv4Network(args.ip):
    # print('Grabbing from: ' + str(ip))
    result = get_sysdescr(str(ip), args.community, args.timeout)
    if result:
        output += str(ip) + ':' + result + '\r\n'

if args.output:
    with open(args.output, 'w') as f:
        f.write(output)
else:
    print(output)
