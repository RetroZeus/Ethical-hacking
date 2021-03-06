import socket
import argparse
import IPy 

def connect_host(ip,port):
	try:
		s = socket.socket()
		s.connect((ip,port)) 
		s.settimeout(3)
		print('Port {} is open'.format(port))
	except:
		print('Port {} is closed'.format(port))

def check_ip(ip):
	try:
		new_ip = IPy.IP(ip)
		return (ip)
	except:
		converted_ip = socket.gethostbyname(ip)
		return converted_ip

parser = argparse.ArgumentParser()
parser.add_argument('-ip','--ipaddress',type=str)
parser.add_argument('-p','--port',type=int)

args = parser.parse_args() 

IPADDRESS = check_ip(args.ipaddress)
PORT = args.port 

connect_host(IPADDRESS,PORT)


# Usage python nmap.py -h > for help menu
# python nmap.py -ip {IP address} -p {Port number} OR python nmap.py --ipaddress {IP Address} --port {port numbber} 
# NOTE : You can use domain names in place of IP addresses to scan a host :)
