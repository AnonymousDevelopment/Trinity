from pexpect import pxssh

## Script to Create a Bot Net 

class Bot: 


    # Initilize New client 

def __init__(self, host, user, password):
    self.host = host 
    self.user = user 
    self.password = password 
    self.session = self.ssh()


    # secure shell into client 

def ssh(self):
    try:
        bot = pxssh.pxssh()
        bot.login(self.host, self.user, self.password)
        return bot 
    except Exception as e: 
        print('Connection Failure.')
        print(e)



    # Send commands to Client 

def send_command(self, cmd)
    self.session.sendline(cmd)
    self.session.prompt()
    return self.session.before