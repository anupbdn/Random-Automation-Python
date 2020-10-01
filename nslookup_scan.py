from nslookup import Nslookup
import csv
domain = "google.com"
dns_query = Nslookup(dns_servers=["1.1.1.1"])
ips_record = dns_query.dns_lookup(domain)
print(domain,"-" ,ips_record.answer[0])

print('******* DNS Resolution*******')

with open("hosts.csv", newline='') as hosts:
        host_dict = csv.DictReader(hosts)
        for row in host_dict:
            domain = row['Hosts']
            dns_query = Nslookup(dns_servers=["1.1.1.1"])
            ips_record = dns_query.dns_lookup(domain)
            print(domain,"-" ,ips_record.answer[0])