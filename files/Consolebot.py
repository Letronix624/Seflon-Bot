import threading
import time
import shutil
import os
import json
import sys
from subprocess import Popen, call, PIPE, STDOUT
try:
    import discord
except:
    os.system("py -m pip install discord")
try:
    import discord
except:
    print("Discord module not installed. Install it by typing in \"py -m pip install discord\" in cmd.")
pydir = os.path.dirname(os.path.realpath(__file__))
def cls(): os.system("cls")
try:
    rawestdata = open(pydir + "\data.json", "r")
except:
    print("data.json not found. Setting up a define tool to gain data.")
    time.sleep(1)
    cls()
    print("data.json not found. Setting up a define tool to gain data..")
    time.sleep(1)
    cls()
    print("data.json not found. Setting up a define tool to gain data...")
    time.sleep(1)
    cls()
    import updatedata
    rawestdata = open("E:\Discord\data.json", "r")
data = json.load(rawestdata)
rawestdata.close()
serveractive = False
client = discord.Client()
Servername = data["Server name"]
directory = data['Server directory']
os.system("title Minecraft " + Servername + " Server.")
authcode = data["Auth id"]
gbram = data["Given ram"]
deletionconfirmation = False
xxxsssxxx = True
serverlaunchername = data["Jar name"]
channelcode = data["Console channel"]

mcsession = Popen("java -Xmx" + str(gbram) + "G -Xms" + str(gbram) + "G -jar " + serverlaunchername + " nogui", cwd=directory, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
serveractive = True
def activeserverinfodef():
    while True:
        output = str(mcsession.stdout.readline())[2:-5]
        if output != "" and xxxsssxxx:
            print(output)
            channel = client.get_channel(channelcode)
            client.loop.create_task(channel.send(output))
            mcsession.stdout.flush()
activeserverinfo = threading.Thread(target=activeserverinfodef)
@client.event
async def on_ready():
    try:
        activeserverinfo.start() 
    except:
        return
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Hosting a Minecraft server called: \"" + Servername + "\". For help do server_help"))
    channel = client.get_channel(channelcode)
    await channel.purge(limit=999)
    channel = client.get_channel(channelcode)
    print('logged in. {0.user}'.format(client))
    await channel.send("Connected to console.")
    global xxxsssxxx
    xxxsssxxx = True
    global serveractive
@client.event
async def on_message(message):
    msg = message.content.lower()
    if msg[0] == "/":
        msg = msg[1:]
    channel = client.get_channel(channelcode)
    if message.author == client.user or message.channel != channel:
        return
    elif msg == "stop" or msg == "server_stop":
        xxxsssxxx = False
        global serveractive
        command = 'stop'
        print(message.author, "has stopped the server")
        mcsession.stdin.write(bytes(command + "\r\n", "ascii"))
        mcsession.stdin.flush()
        await channel.send("Closing Server...")
        print("please wait 15 seconds")
        time.sleep(15)
        cls()
        await channel.send("Server closed.. To start it up again type \"server_start\".")
        print("currently inactive")
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Idle. For help do \"server_help\" and to start the server do \"server_start\""))
        serveractive = False
    elif msg == "server_reset":
        await channel.send("Are you really sure you want to reset the World? This will generate a completely new world for this server. This command is very risky. To proceed type \"server_reset_confirm_meant_delete_the_world_already_justdoitalready\" in the chat. Say no to undo this step.")
        global deletionconfirmation
        deletionconfirmation = True
    elif msg == "server_reset_confirm_meant_delete_the_world_already_justdoitalready" and deletionconfirmation:
        await channel.send("World is beeing reset. Please wait...")
        xxxsssxxx = False
        mcsession.stdin.write(bytes("stop" + "\r\n", "ascii"))
        mcsession.stdin.flush()
        time.sleep(10)
        shutil.rmtree(directory + "\world")
        shutil.rmtree(directory + "\world_nether")
        shutil.rmtree(directory + "\world_the_end")
        await channel.send("World got reset. To start up again type \"server_start\".")
        serveractive = False
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Idle. For help do \"server_help\" and to start the server do \"server_start\""))
    elif msg == "no":
        deletionconfirmation = False
    elif msg == "restart" or msg == "server_restart":
        xxxsssxxx = False
        command = 'restart'
        print(message.author, "has restarted the server")
        mcsession.stdin.write(bytes(command + "\r\n", "ascii"))
        mcsession.stdin.flush()
        await channel.send("Restaring Server...")
        print("please wait 15 seconds")
        time.sleep(15)
        cls()
        sys.stdout.flush()
        os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    elif msg == "server_start":
        if serveractive:
            await channel.send("Server is still active.")
        else:
            await channel.send("Starting up...")
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    elif msg == "server_info":
        if serveractive:
            await channel.send("Server is online.")
        else:
            await channel.send("Server is offline. To start type server_start")
    elif msg == "server_help":
        await channel.send("List of all commands: stop/server_stop - stops the server, server_reset - resets the world of the server, server_restart - reboots the server, server_start - starts the server if offline, server_info - answers if the server is online.")
    elif msg == "cls":
        await channel.purge(limit=999)
    else:
        command = message.content
        if command[0] == "/":
            command = command[1:]
        print(message.author, "has issued the command:", command)
        mcsession.stdin.write(bytes(command + "\r\n", "ascii"))
        mcsession.stdin.flush()
activeserverinfo = threading.Thread(target=activeserverinfodef)


client.run(authcode)