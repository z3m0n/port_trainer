# port_trainer
Simple python script to help with port memorization for Security+ SYO-501 certification exam.

## INSTALL & RUN
	###### INSTALL
	- clone this repo or copy code to local machine
	- install dependecies with `pip3 install -r requirements.txt`
	
	###### RUN	
	- make port_trainer.py executable and run with `./port_trainer.py`
	- or, `python3 port_trainer.py`

### Future changes:
- make game loop to keep playing
- give escape sequence to end loop and start over / exit (currently only CTRL+c)
- randomize question order
- ask questions with protocol and prompt for port number
- store incorrect answers and give option to review
- score ranges to display messages
	- 100 - Perfect! You're ready for the exam!
	- 90 - 99 - Well Done!
	- 75 - 89 - Good, but not great...
	- 65 - 74 - Not failing, but you need to study.
	- < 65 - Terrible! Go study!

## Release Info:
- Last modified: 11/24/2020
##### Created with :heart: by flowenol
