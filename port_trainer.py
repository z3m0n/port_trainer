#! /usr/bin/python3


from os import system, name
from time import sleep

# define clear screen function
def clear_screen():
	# for Windows
	if name == 'nt':
		_ = system('cls')

	# for mac & linux (os.name is 'posix')
	else:
		_ = system('clear')

# define port:protocol dictionary
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

# define variables for correct/incorrect answers
correct = 0
incorrect = 0

# for loop to iterate dictionary by items
for port, protocol in port_proto_dict.items():
	clear_screen()
	print('\nPort: '+ str(port))
	answer = input('Protocol: ')
	if (answer.lower() == protocol.lower()):
		print('Correct!')
		correct += 1
		sleep(0.5) # quick sleep before clear screen
	else:
		print('Wrong!')
		print('Correct answer: '+str(port)+' '+str(protocol))
		incorrect += 1
		sleep(3) # sleep to allow user to see correct answer
# end for loop

clear_screen() # clear screen before displaying results
score = round(correct/(correct+incorrect) * 100, 2) # calculate score

# print results
print('\nThanks for practicing!')
print('-> Correct answers: '+ str(correct))
print('-> Incorrect answers: '+ str(incorrect))
print('-> Score: '+str(score)+'%\n')
