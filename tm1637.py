from mfrc522 import SimpleMFRC522
import time
import RPi.GPIO as gp
try:
	reader=SimpleMFRC522()
	name=input("Enter name : ")
	password=input("Enter pass : ")
	idata=name+"%"+password
	print("hold your card")
	reader.write(idata)
	print("Write Successful")
	time.sleep(5)
	print("hold your card to check data")
	data=reader.read()
	udata=data[1].split("%")
	print("Hello ",udata[0])
	print("Your data has been successfully written.")
except:
	pass
finally:
	gp.cleanup()



'''
from tm1637 import TM1637
import time
from datetime import datetime
from mfrc522 import SimpleMFRC522

user_login=SimpleMFRC522()
text1=TM1637(clk=27,dio=17)
text2=TM1637(clk=23,dio=24)
reader=SimpleMFRC522()

users={"kalpaj":"123456","tejas":"20042004","pratham":"prathsam","kamlesh":"dfd"}
print("hold your card to check data")
keys=users.keys()
data=reader.read()
udata=data[1].split("%")
if(udata[0] in keys):
	text1.show("ciao")
	text2.show("user")
	print("Ciao user",udata[0])	
	time.sleep(5)
else:
	print("Invalid user!!")	
	text1.show("err")
	time.sleep(5)
text1.write([0,0,0,0])
text2.write([0,0,0,0])
'''
