#Defining Imports
import fbchat
from getpass import getpass
from fbchat.models import *
#Defining Classes

class FBClient:
    def __init__(self,username,password):
        self.client=fbchat.Client(username,password)
        if (self.client.isLoggedIn()):
            print("User Logged in")
    def friends(self):
        client=self.client.fetchAllUsers()
        for i in client:
            print('Name : {0}  User ID: {1}'.format(i.name,i.uid))

    def searchfriends(self,name):
        client=self.client.fetchAllUsers()
        for i in client:
            if (i.first_name==name or i.last_name==name) or i.name==name :
                print("Person Found")
                print('Name : {0}  User ID: {1} Image: {2}'.format(i.name,i.uid,i.photo))
    def getuid(self,name):
        client=self.client.fetchAllUsers()
        for i in client:
            if (i.first_name==name or i.last_name==name) or i.name==name :
                print("Person Found")
                print('Name : {0}  User ID: {1} '.format(i.name,i.uid))
                if (input("Do you want to Confirm (Y/N):")=="Y"):
                    return i.uid
                        
    def message(self,message,frienduid):
        message_thread=self.client.send(Message( message),frienduid,ThreadType.USER)
        if(message_thread):
            print("Message sent.Waiting For Response.........")
           

    def sendAll(self,message):
        client=self.client.fetchAllUsers()
        for i in client:
            if self.client.send(Message( message),i.uid,ThreadType.USER):
                print('Name : {0}  Send'.format(i.name))
                
    


