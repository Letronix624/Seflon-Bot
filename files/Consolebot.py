import threading
import time
import shutil
import os
import json
import sys
from subprocess import Popen, call, PIPE, STDOUT
try:
    import playsound
except:
    os.system("py -m pip install playsound")
    import playsound
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
    playsound.playsound(pydir + "\notification.mp3")
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
data = json.load(rawestdata)
try:
    if data["Auth id"] == "":
        print("You haven't inserted an Auth id.")
        input()
        quit()
    if data["Console channel"] == "":
        print("You haven't inserted an channel id.")
        input()
        quit()
    if data["Easy controls"]:
        cls()
    if data["Easy controls channel"] == "" and data['Easy controls']:
        print("You haven't inserted an Easy controls channel, even though you set Easy controls on.")
        input()
        quit()
except:
    print("Outdated profile. Please create a new profile. Open \"2. Configure Bot\" or \"updatedata.py\" and create a new profile.")
    input()
    quit()
Easycontrols = data["Easy controls"]
Easycontrolschannel = data["Easy controls channel"]
rawestdata.close()
serveractive = False
client = discord.Client()
Servername = data["Server name"]
directory = data['Server directory']
os.system("title Minecraft " + Servername + " Server.")
authcode = data["Auth id"]
gbram = data["Given ram"]
deletionconfirmation = False
global xxxsssxxx
xxxsssxxx = True
serverlaunchername = data["Jar name"]
channelcode = data["Console channel"]

mcsession = Popen("java -Xmx" + str(gbram) + "G -Xms" + str(gbram) + "G -jar " + serverlaunchername + " nogui", cwd=directory, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
serveractive = True
def notify():
    playsound.playsound(pydir + "\notification.mp3")
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
async def on_ready(): #ONREADY ------------------------------------- ONREADY ---------------------------------------- ONREADY -------------------------------------------- ONREADY
    try:
        activeserverinfo.start() 
    except:
        return
    if Easycontrols:
        serverproperties = open(directory + "\server.properties", "r")
        if "white-list=true" in serverproperties.read():
            whitelist = True
        else:
            whitelist = False
        serverproperties.close()
        serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Name = {}, Server = Online, Whitelist = {}, Given RAM = {}GB".format(Servername, str(whitelist), str(gbram)),color=0x69FF69)
        serverinfo.add_field(name="⛔:", value="Stop Server", inline=True)
        serverinfo.add_field(name="🟡:", value="Restart Server", inline=True)
        channel = client.get_channel(Easycontrolschannel)
        await channel.purge()
        k = await channel.send(embed=serverinfo)
        for emoji in ["⛔", "🟡"]:
            await k.add_reaction(emoji)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="Hosting a Minecraft server called: \"" + Servername + "\". For help do server_help"), afk=False)
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
    global xxxsssxxx
    channel = client.get_channel(channelcode)
    if message.author == client.user or message.channel != channel:
        return
    msg = message.content.lower()
    if msg[0] == "/":
        msg = msg[1:]
    if msg == "stop" or msg == "server_stop":
        xxxsssxxx = False
        global serveractive
        serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Name = {}, Server = Stopping...".format(Servername,),color=0xE0B824)
        channe = client.get_channel(Easycontrolschannel)
        await channe.purge()
        await channe.send(embed=serverinfo)
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
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Idle. For help do \"server_help\" and to start the server do \"server_start\""), afk=True)
        serveractive = False
        serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Server = Offline",color=0xAD1F1F)
        serverinfo.add_field(name="🟢:", value="Start Server", inline=True)
        channe = client.get_channel(Easycontrolschannel)
        await channe.purge()
        k = await channe.send(embed=serverinfo)
        await k.add_reaction("🟢")
    elif msg == "server_reset":
        await channel.send("Are you really sure you want to reset the World? This will generate a completely new world for this server. This command is very risky. To proceed type \"server_reset_confirm_meant_delete_the_world_already_justdoitalready\" in the chat. Say no to undo this step.")
        global deletionconfirmation
        deletionconfirmation = True
    elif msg == "server_reset_confirm_meant_delete_the_world_already_justdoitalready" and deletionconfirmation:
        await channel.send("World is beeing reset. Please wait...")
        xxxsssxxx = False
        serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Name = {}, Server = Stopping...".format(Servername,),color=0xE0B824)
        channe = client.get_channel(Easycontrolschannel)
        await channe.purge()
        await channe.send(embed=serverinfo)
        mcsession.stdin.write(bytes("stop" + "\r\n", "ascii"))
        mcsession.stdin.flush()
        time.sleep(10)
        shutil.rmtree(directory + "\world")
        shutil.rmtree(directory + "\world_nether")
        shutil.rmtree(directory + "\world_the_end")
        await channel.send("World got reset. To start up again type \"server_start\".")
        serveractive = False
        serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Server = Offline",color=0xAD1F1F)
        serverinfo.add_field(name="🟢:", value="Start Server", inline=True)
        channe = client.get_channel(Easycontrolschannel)
        await channe.purge()
        k = await channe.send(embed=serverinfo)
        await k.add_reaction("🟢")
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Idle. For help do \"server_help\" and to start the server do \"server_start\""), afk=True)
    elif msg == "no":
        deletionconfirmation = False
    elif msg == "restart" or msg == "server_restart":
        xxxsssxxx = False
        serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Name = {}, Server = Restarting...".format(Servername,),color=0xE0B824)
        channe = client.get_channel(Easycontrolschannel)
        await channe.purge()
        await channe.send(embed=serverinfo)
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
    elif msg == "server_start" or msg == "start":
        if serveractive:
            await channel.send("Server is still active.")
        else:
            await channel.send("Starting up...")
            notify()
            serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Server = Starting...",color=0xE0B824)
            channe = client.get_channel(Easycontrolschannel)
            await channe.purge()
            await channe.send(embed=serverinfo)
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
    elif msg == "server_info":
        if serveractive:
            await channel.send("Server is online.")
        else:
            await channel.send("Server is offline. To start type server_start")
    elif msg == "server_help":
        await channel.send("List of all commands: stop/server_stop - stops the server, server_reset - resets the world of the server, server_restart - reboots the server, server_start - starts the server if offline, server_info - answers if the server is online.")
    elif msg == "cls":
        await channel.purge()
    else:
        command = message.content
        if command[0] == "/":
            command = command[1:]
        print(message.author, "has issued the command:", command)
        mcsession.stdin.write(bytes(command + "\r\n", "ascii"))
        mcsession.stdin.flush()

@client.event
async def on_reaction_add(reaction, user):
    global xxxsssxxx
    global serveractive
    channel = client.get_channel(Easycontrolschannel)
    if user.bot:
        return 
    if reaction.message.channel == channel:
        if reaction.emoji == "⛔" and serveractive:
            xxxsssxxx = False
            serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Name = {}, Server = Stopping...".format(Servername,),color=0xE0B824)
            channe = client.get_channel(Easycontrolschannel)
            await channe.purge()
            await channe.send(embed=serverinfo)
            command = 'stop'
            print(user.name, "has stopped the server")
            mcsession.stdin.write(bytes(command + "\r\n", "ascii"))
            mcsession.stdin.flush()
            print("please wait 15 seconds")
            time.sleep(15)
            cls()
            await channel.send("Server closed.. To start it up again type \"server_start\".")
            print("currently inactive")
            await client.change_presence(status=discord.Status.idle, activity=discord.Game(name="Idle. For help do \"server_help\" and to start the server do \"server_start\""), afk=True)
            serveractive = False
            serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Server = Offline",color=0xAD1F1F)
            serverinfo.add_field(name="🟢:", value="Start Server", inline=True)
            channe = client.get_channel(Easycontrolschannel)
            await channe.purge()
            k = await channe.send(embed=serverinfo)
            await k.add_reaction("🟢")
        elif reaction.emoji == "🟢" and not serveractive:
            notify()
            serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Server = Starting...",color=0xE0B824)
            channe = client.get_channel(Easycontrolschannel)
            await channe.purge()
            await channe.send(embed=serverinfo)
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        elif reaction.emoji == "🟡" and serveractive:
            xxxsssxxx = False
            serverinfo = discord.Embed(title="Easy Controls Panel, Server Status", description="Name = {}, Server = Restarting...".format(Servername,),color=0xE0B824)
            channe = client.get_channel(Easycontrolschannel)
            await channe.purge()
            await channe.send(embed=serverinfo)
            command = 'restart'
            print(user.name, "has restarted the server")
            mcsession.stdin.write(bytes(command + "\r\n", "ascii"))
            mcsession.stdin.flush()
            print("please wait 15 seconds")
            time.sleep(15)
            cls()
            sys.stdout.flush()
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        else:
            await reaction.message.remove_reaction(reaction.emoji, user)
activeserverinfo = threading.Thread(target=activeserverinfodef)
client.run(authcode)