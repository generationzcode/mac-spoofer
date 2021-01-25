import optparse
import subprocess
import re
try:
	def get_mac(interface):
		ifconfig_out = subprocess.check_output(['ifconfig',interface])
		search_res = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',str(ifconfig_out))
		return search_res.group(0)
	parser = optparse.OptionParser()
	parser.add_option('-i','--interface',dest='interface',help='Interface to change mac address')
	parser.add_option('-m','--mac',dest='new_mac', help='new mac to be assigned')
	(option, args) = parser.parse_args()
	print("your current mac address is "+get_mac(option.interface))
	def change_mac(interface, new_mac):
		subprocess.call(['ifconfig',interface,'down'])
		subprocess.call(['ifconfig',interface,'hw','ether',new_mac])
		subprocess.call(['ifconfig', interface, 'up'])
	change_mac(option.interface,option.new_mac)
	print('[+] new mac address is '+option.new_mac)
except:
	print('[-] Something went wrong. An error...')

