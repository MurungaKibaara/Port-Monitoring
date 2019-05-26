import nmap

def real_scan(domain):
        try:
            open_ports = []
            nm = nmap.PortScanner()
            results = nm.scan(domain)
            
            hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
            for host, status in hosts_list:
                if status == "up":
                    protocols = nm[host].all_protocols()
                    for protocol in protocols:
                        ports = nm[host][protocol]
                        for port in ports:
                            if ports[port]['state'] == 'open':
                                open_ports.append(port)
            return open_ports
        except:
            print('problem')
            return [] 

real_scan('localhost')