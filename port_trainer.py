#! /usr/bin/python3

#import

port_proto_dict = {
	"21": "FTP",
	"22": "SSH, SCP, SFTP",
	"23": "Telnet",
	"25": "SMTP",
	"53": "DNS",
	"67": "DHCP Server",
	"68": "DHCP Client",
	"80": "HTTP",
	"88": "Kerberos",
	"110": "POP3",
	"139": "NetBIOS",
	"143": "IMAP",
	"161": "SNMP",
	"162": "SNMP",
	"443": "HTTPS",
	"465": "Encrypted SMTP",
	"636": "LDAPS",
	"989": "FTPS",
	"990": "FTPS",
	"993": "Secure IMAP",
	"995": "Secure POP3",
	"3269": "LDAPS",
	"3389": "RDP"
}

correct = 0
incorrect = 0

for port, protocol in port_proto_dict.items():
	print('\nPort: '+ str(port))
	answer = input('Protocol? ')
	if (answer.lower() == protocol.lower()):
		print('Correct!')
		correct += 1
	else:
		print('Wrong!')
		print('Correct answer: '+str(port)+': '+str(protocol))
		incorrect += 1

score = round(correct/(correct+incorrect) * 100, 2)

print('\nThanks for practicing!')
print('-> Correct answers: '+ str(correct))
print('-> Incorrect answers: '+ str(incorrect))
print('-> Score: '+str(score)+'%\n')
