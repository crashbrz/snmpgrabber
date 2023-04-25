![License](https://img.shields.io/badge/license-sushiware-red)
![Issues open](https://img.shields.io/github/issues/crashbrz/snmpgrabber)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/crashbrz/snmpgrabber)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/crashbrz/snmpgrabber)
![GitHub last commit](https://img.shields.io/github/last-commit/crashbrz/snmpgrabber)

# IP Ranger 
SNMPGrabber is a tool that allows the pentester to connect to SNMP servers from a specified IP Range using a community string and retrieve the system.sysDescr.0 MIB value by default. This tool 
is designed to make the Gathering of evidence and Proof of Concept (PoC) easier by automating the process of collecting SNMP data from a large number of devices.

With SNMPGrabber, users can easily specify the IP range to scan and the SNMP community string for authentication. In addition to this, users can also set the timeout value and specify a custom SNMP port if necessary.

By default, SNMPGrabber retrieves the system.sysDescr.0 MIB value, which provides information about the system's hardware and software configuration. However, users can also specify a custom OID to collect data from a different MIB.

Once the data has been collected, users can save the results to a file or view them in the terminal. This makes it easy to analyze, filter and sort the data.

Usage example:
```
┌──(crash㉿Anubis)-[~]
└─$ python3 snmpgrabber.py -c public -i 10.3.3.0/24 -t 500

 ```
- The above command will try to retrieve the OID: 1.3.6.1.2.1.1.1.0 (system.sysDescr.0) for each host in the IP range. 
- Set the timeout to 500 milliseconds (0.5 seconds)
- Use the community "public"

```
┌──(crash㉿Anubis)-[~]
└─$ └─$ python3 snmpgrabber.py -c private -i 10.3.3.0/24 -t 500 -o output-snmp.txt

 ```
- The above command will try to retrieve the OID: 1.3.6.1.2.1.1.1.0 (system.sysDescr.0) for each host in the IP range. 
- Set the timeout to 500 milliseconds (0.5 seconds)
- Use the community "private"
- Save the output to the file output-snmp.txt

### Usage/Help ###
Run snmpgrabber.py -h to see all options. Also, you can contact me (@crashbrz) on Twitter<br>

### Installation ###
Clone the repository in the desired location.<br>

### License ###
SNMPGrabber is licensed under the SushiWare license. Check [docs/license.txt](docs/license.txt) for more information.
 
### Python Version ###
Tested on:<br>
Python 3.10.9
