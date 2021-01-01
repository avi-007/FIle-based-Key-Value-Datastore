from threading import *
import time

data_store={}	#dictionary where we store data

#create method
#to use this syntax will be "create(key_name,value,ttl=0)", ttl is optional argument as create can be invoked by passing two arguments

def create(key,value,ttl=0):
	if key in data_store:
		print("Error: Key already exists")	#error displayed if key is already present
	else:
		if(key.isalpha()):
			if(len(data_store)<(1024*1024*1024) and value<=(16*1024*1024)):   #constraint to check if file size is less than 1 GB and json object value is less than 16kB
				if(len(key)<=32):   #constraint to check the key length to be 32 chars
					if ttl==0:
						entry=[value,ttl]
					else:
						entry=[value,time.time()+ttl]
					data_store[key]=entry
			else:
				print("Error: Memory limit exceeded")   #error displayed if file size is greater than 1 GB and json object value is less than 16kB
		else:
			print("Error: Key name is invalid, it must contain only alphabets")   #error displayed if key is special character or number

#read method
#syntax for use is read(key_name)

def read(key):
	if key not in data_store:
		print("Error: Key does not exist")	#error displayed if key is not present in data_store
	else:
		a=data_store[key]
		if(a[1]!=0):   #check if ttl value is not 0
			if(time.time()<a[1]):	#comparing current time with the expiry time
				string=str(key)+":"+str(a[0])
				return string
			else:
				print("Error: Time-to-live(TTL) of ",key," is expired")	 #error displayed if ttl value expires
		else:
			string=str(key)+":"+str(a[0])
			return string

#delete method
#syntax for use is delete(key_name)

def delete(key):
	if key not in data_store:
		print("Error: Key does not exist")   #error displayed if key is not present in data_store
	else:
		a=data_store[key]
		if(a[1]!=0):	#check if ttl value is not 0
			if(time.time()<a[1]):	#comparing current time with the expiry time 
				del data_store[key]
				print("Key is successfully deleted") 
			else:
				print("Error: Time-to-live(TTL) of ",key," is expired")	 #error displayed if ttl value expires"
		else:
			del data_store[key]
			print("Key is successfully deleted")