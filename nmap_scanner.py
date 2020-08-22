import nmap

scanner = nmap.PortScanner()

print('Welcome, this is a simple nmap automation tool')
print('<-------------------------------------------->')

ip_addr = input('Please enter the IP address you ant to scan: ')
print('The IP you entered is ', ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run:
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan\n""")
print('You have selected option ', resp)

if resp =='1':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024' ,'-v -sS')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    try:
        print("Open Ports: ",scanner[ip_addr]['tcp'].keys())
    except:
        #do nothing
        print('-')

elif resp =='2':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024' ,'-v -sU')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    try:
        print("Open Ports: ",scanner[ip_addr]['udp'].keys())
    except:
        #do nothing
        print('-')

elif resp =='3':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024' ,'-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print('IP Status: ', scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    try:
        print("Open Ports: ",scanner[ip_addr]['tcp'].keys())
    except:
        #do nothing
        print('-')

else:
    print('Please enter a valid number.')
