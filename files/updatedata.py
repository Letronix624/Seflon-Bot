import json
import os
from typing import Generic
pydir = os.path.dirname(os.path.realpath(__file__))
def cls(): os.system("cls")
os.system("title Profile Setup")
print("Hello and welcome to my Discord bot called: Seflon Minecraft Server Discord Link.")
input("----------ENTER----------                    1/6")
cls()
print("This is the first setup of the bot. This setup will let the bot know how the server is called, what id the bot has, what channel the bot should be linked to, where the server is located, how much RAM you would like your server to use and if you would like the minecraft server to show the GUI.")
input("----------ENTER----------                    2/6")
cls()
print("You can use this Setup to update this Information again and again.")
input("----------ENTER----------                    3/6")
cls()
print("To access this Setup you must either open updatedata.py or delete data.json.")
input("----------ENTER----------                    4/6")
cls()
print("If you want to change the information the boring way you could edit data.json directly.")
input("----------ENTER----------                    5/6")
cls()
print("This program will start asking you now. Be sure to put in the right information or the program will fail.")
input("----------ENTER----------                    6/6")
cls()
profilesbefore = True
for badatnames in os.listdir(pydir + "\profiles"):
    if badatnames.endswith(".json"):
        profilesbefore = False
if profilesbefore:
    print("You haven't created any profiles before. Press enter to create a new profile.")
    input()
else:
    while True:
        print("You already have created profiles before. Do you want to create a new profile?")
        liveans = input("yes/no >").lower()
        if liveans == "yes" or liveans == "y":
            newprofile = True
            break
        elif liveans == "no" or liveans == "n":
            newprofile = False
            break
        else:
            cls()
            print("Yes or No.")
    if newprofile:
        print("Perfect. Creating new profile. First question:")
    else:
        while True:
            print("Ok. Browsing your profiles..")
            print("what server profile do you want to access? Type in the number:")
            filenumber = 0
            for file in os.listdir(pydir + "\profiles"):
                if ".json" in file:
                    filenumber += 1
                    print(str(filenumber) + ". " + file[:-5])
            while True:
                liveans = input("--->")
                try:
                    print(int(liveans))
                    cls()
                    if int(liveans) > filenumber or int(liveans) < 1:
                        print("You need to put in a number that is in range of the shown files.")
                        print()
                    else:
                        selected = os.listdir(pydir + "\profiles")[int(liveans) - 1]
                        break
                except:
                    print("You need to put in a number.")
                    print()
            cls()
            print("You have selected: " + selected[:-5] + ".")
            print("What do you want to do with this profile?")
            print("0. Quit")
            print("1. Set active.")
            print("2. Change data.")
            print("3. DELETE!")
            while True:
                liveans = input()
                try:
                    print(int(liveans))
                    cls()
                    if int(liveans) > 3 or int(liveans) < 0:
                        print("You need to put in a number that is in range of the shown options.")
                        print()
                    else:
                        break
                except:
                    print("You need to put in a number.")
                    print()
            if liveans == "0":
                quit()
            elif liveans == "1":
                datafile = open(pydir + "\data.json", "w")
                override = open(pydir + "\profiles\\" + selected, "r")
                datafile.write(override.read())
                override.close()
                datafile.close()
                print("You have successfully changed to " + selected[:-5])
                input("Enter to leave.")
                quit()
            elif liveans == "2":
                override = open(pydir + "\profiles\\" + selected, "r")
                data = json.load(override)
                override.close()
                Servername = data["Server name"]
                Authid = data["Auth id"]
                Consolechannel = data["Console channel"]
                Serverdirectory = data["Server directory"]
                Givenram = data["Given ram"]
                Jarname = data["Jar name"]
                while True:
                    cls()
                    print("1. Server Name -->" + Servername)
                    print("2. Auth ID -->" + Authid)
                    print("3. Console Channel ID -->" + str(Consolechannel))
                    print("4. Server Directory -->" + Serverdirectory)
                    print("5. Given RAM -->" + str(Givenram) + "GB")
                    print()
                    print("What data do you want to change? Enter 1 to 6 to change. If done enter nothing and press enter.")
                    change = input()
                    if change == "1":
                        cls()
                        print("Server Name --> Currently changing...")
                        print("Auth ID -->" + Authid)
                        print("Console Channel ID -->" + str(Consolechannel))
                        print("Server Directory -->" + Serverdirectory)
                        print("Given RAM -->" + str(Givenram) + "GB")
                        print()
                        print("How is your server called? This name will be visible in the activity status of the bot and title the window.")
                        os.remove(pydir + "\profiles\\" + selected)
                        Servername = input("--->")
                    elif change == "2":
                        cls()
                        print("Server Name -->" + Servername)
                        print("Auth ID --> Currently changing")
                        print("Console Channel ID -->" + str(Consolechannel))
                        print("Server Directory -->" + Serverdirectory)
                        print("Given RAM -->" + str(Givenram) + "GB")
                        print()
                        print("What is the Auth ID of the bot you will be using for this?")
                        print("If you still have no bot go to discord.com/developers and login as your Discord account. Then press New Application and call the bot how you want. I called mine \"Server\", because this generic name seems the most fitting. Create and edit your bot to be as you like. After that step you must go to the left and press OAuth2 and go to the URL Generator. You have to check bot and scroll down to press either Administrator(easiest) or if you don't trust my bot press Read Messages/View Channels, Send Messages, Manage Messages, Embed Links, Attach Files, Read Message History and Add Reactions. After that you must go further down and enter the link seen. Then you must select the server you want your bot in. After he got in the server you need the Auth ID you want to put in right below. You can get it by pressing Bot on the left menu still on discord.com/developers and then copying the token. Put the Auth Token right in here and press enter. Be sure to put in the right one.")
                        Authid = input("--->")
                    elif change == "3":
                        cls()
                        while True:
                            print("Server Name -->" + Servername)
                            print("Auth ID -->" + Authid)
                            print("Console Channel ID --> Currently changing...")
                            print("Server Directory -->" + Serverdirectory)
                            print("Given RAM -->" + str(Givenram) + "GB")
                            print()
                            print("What channel of your Discord server do you want to be the console? Be sure to make this console only AND ONLY visible to people you trust. If you don't do that untrusted people could change the settings close the server or straight up reset the whole world.")
                            print("To get this ID you must enter the Discord settings, go to Advanced and turn on Developer mode. After that you must right click the console channel and press \"Copy ID\".")
                            Consolechannel = input("--->")
                            try:
                                print(int(Consolechannel))
                                break
                            except:
                                cls()
                                print("This ID is made only out of numbers. You may have done something wrong.")
                    elif change == "4":
                        cls()
                        while True:
                            print("Server Name -->" + Servername)
                            print("Auth ID -->" + Authid)
                            print("Console Channel ID -->" + str(Consolechannel))
                            print("Server Directory --> Currently changing...")
                            print("Given RAM -->" + str(Givenram) + "GB")
                            print()
                            print("In what directory have you saved the server?")
                            print("You only have to put in something like this for me: \"E:\\Minecraft\\letronix\"")
                            print("----------------------------------------------------Drive  Folder  Folder containing the server")
                            print("You can get this data like this: open your folder containing your server and press the empty part of the bar that tells you your directory. When pressed copy the text and put it here.")
                            Serverdirectory = input("--->")
                            try:
                                for file in os.listdir(Serverdirectory):
                                    if ".jar" in file:
                                        Jarname = file
                                break
                            except:
                                cls()
                                print("This is not a valid directory. No jar file found.")
                    elif change == "5":
                        cls()
                        while True:
                            print("Server Name -->" + Servername)
                            print("Auth ID -->" + Authid)
                            print("Console Channel ID -->" + str(Consolechannel))
                            print("Server Directory -->" + Serverdirectory)
                            print("Given RAM --> Currently changing...")
                            print()
                            print("How much RAM would you like to give your server in GB? Whole numbers only.")
                            Givenram = input("--->")
                            try:
                                print(int(Givenram))
                                break
                            except:
                                cls()
                                print("You need to enter whole numbers. You cannot have", Givenram, "GB ram.")
                    else:
                        cls()
                        break
                    data = {
                        "Server name": Servername,
                        "Auth id": Authid,
                        "Console channel": int(Consolechannel),
                        "Server directory": Serverdirectory,
                        "Given ram": int(Givenram),
                        "Jar name": Jarname
                    }
                    datajson = json.dumps(data, indent=4)
                    datafile = open(pydir + "\profiles\\" + Servername + ".json", "w")
                    datafile.write(datajson)
                    datafile.close()
                    cls()
                    print("You have successfully changed the data on your profile.")
            elif liveans == "3":
                cls()
                while True:
                    print("Deleting this doesn't delete the server. Deleting this just deletes this profile setting.")
                    print("Do you reallt want to delete this Profile?")
                    print("You have selected: " + selected[:-5] + ".")
                    print()
                    deleteconfirmation = input("yes/no >").lower()
                    if deleteconfirmation == "yes" or deleteconfirmation == "y":
                        os.remove(pydir + "\profiles\\" + selected)
                        print("You have deleted this profile.")
                        input("Enter to continue")
                        cls()
                        break
                    elif deleteconfirmation == "no":
                        print("File hasn't been deleted.")
                        input("Enter to continue")
                        cls()
                        break
print("How is your server called? This name will be visible in the activity status of the bot and title the window.")
Servername = input("--->")
cls()
print("Server name -->" + Servername)
print()
print("What is the Auth ID of the bot you will be using for this?")
print("If you still have no bot go to discord.com/developers and login as your Discord account. Then press New Application and call the bot how you want. I called mine \"Server\", because this generic name seems the most fitting. Create and edit your bot to be as you like. After that step you must go to the left and press OAuth2 and go to the URL Generator. You have to check bot and scroll down to press either Administrator(easiest) or if you don't trust my bot press Read Messages/View Channels, Send Messages, Manage Messages, Embed Links, Attach Files, Read Message History and Add Reactions. After that you must go further down and enter the link seen. Then you must select the server you want your bot in. After he got in the server you need the Auth ID you want to put in right below. You can get it by pressing Bot on the left menu still on discord.com/developers and then copying the token. Put the Auth Token right in here and press enter. Be sure to put in the right one.")
Authid = input("--->")
cls()
while True:
    print("Server name -->" + Servername)
    print("Auth ID -->" + Authid)
    print()
    print("What channel of your Discord server do you want to be the console? Be sure to make this console only AND ONLY visible to people you trust. If you don't do that untrusted people could change the settings close the server or straight up reset the whole world.")
    print("To get this ID you must enter the Discord settings, go to Advanced and turn on Developer mode. After that you must right click the console channel and press \"Copy ID\".")
    Consolechannel = input("--->")
    try:
        print(int(Consolechannel))
        break
    except:
        cls()
        print("This ID is made only out of numbers. You may have done something wrong.")
cls()
while True:
    print("Server Name -->" + Servername)
    print("Auth ID -->" + Authid)
    print("Console Channel ID -->" + str(Consolechannel))
    print()
    print("In what directory have you saved the server?")
    print("You only have to put in something like this for me: \"E:\\Minecraft\\letronix\"")
    print("----------------------------------------------------Drive  Folder  Folder containing the server")
    print("You can get this data like this: open your folder containing your server and press the empty part of the bar that tells you your directory. When pressed copy the text and put it here.")
    Serverdirectory = input("--->")
    try:
        for file in os.listdir(Serverdirectory):
            if ".jar" in file:
                Jarname = file
        break
    except:
        cls()
        print("This is not a valid directory. No jar file found.")
cls()
while True:
    print("Server Name -->" + Servername)
    print("Auth ID -->" + Authid)
    print("Console Channel ID -->" + str(Consolechannel))
    print("Server Directory -->" + Serverdirectory)
    print()
    print("How much RAM would you like to give your server in GB? Whole numbers only.")
    Givenram = input("--->")
    try:
        print(int(Givenram))
        break
    except:
        cls()
        print("You need to enter whole numbers. You cannot have", Givenram, "GB ram.")
while True:
    cls()
    print("1. Server Name -->" + Servername)
    print("2. Auth ID -->" + Authid)
    print("3. Console Channel ID -->" + str(Consolechannel))
    print("4. Server Directory -->" + Serverdirectory)
    print("5. Given RAM -->" + str(Givenram) + "GB")
    print()
    print("Now Check above if you have made any mistakes. Press enter to continue or enter a number from 1 to 6 on what you want to change.")
    change = input()
    if change == "1":
        cls()
        print("Server Name --> Currently changing...")
        print("Auth ID -->" + Authid)
        print("Console Channel ID -->" + str(Consolechannel))
        print("Server Directory -->" + Serverdirectory)
        print("Given RAM -->" + str(Givenram) + "GB")
        print()
        print("How is your server called? This name will be visible in the activity status of the bot and title the window.")
        Servername = input("--->")
    elif change == "2":
        cls()
        print("Server Name -->" + Servername)
        print("Auth ID --> Currently changing")
        print("Console Channel ID -->" + str(Consolechannel))
        print("Server Directory -->" + Serverdirectory)
        print()
        print("What is the Auth ID of the bot you will be using for this?")
        print("If you still have no bot go to discord.com/developers and login as your Discord account. Then press New Application and call the bot how you want. I called mine \"Server\", because this generic name seems the most fitting. Create and edit your bot to be as you like. After that step you must go to the left and press OAuth2 and go to the URL Generator. You have to check bot and scroll down to press either Administrator(easiest) or if you don't trust my bot press Read Messages/View Channels, Send Messages, Manage Messages, Embed Links, Attach Files, Read Message History and Add Reactions. After that you must go further down and enter the link seen. Then you must select the server you want your bot in. After he got in the server you need the Auth ID you want to put in right below. You can get it by pressing Bot on the left menu still on discord.com/developers and then copying the token. Put the Auth Token right in here and press enter. Be sure to put in the right one.")
        Authid = input("--->")
    elif change == "3":
        cls()
        while True:
            print("Server Name -->" + Servername)
            print("Auth ID -->" + Authid)
            print("Console Channel ID --> Currently changing...")
            print("Server Directory -->" + Serverdirectory)
            print("Given RAM -->" + str(Givenram) + "GB")
            print()
            print("What channel of your Discord server do you want to be the console? Be sure to make this console only AND ONLY visible to people you trust. If you don't do that untrusted people could change the settings close the server or straight up reset the whole world.")
            print("To get this ID you must enter the Discord settings, go to Advanced and turn on Developer mode. After that you must right click the console channel and press \"Copy ID\".")
            Consolechannel = input("--->")
            try:
                print(int(Consolechannel))
                break
            except:
                cls()
                print("This ID is made only out of numbers. You may have done something wrong.")
    elif change == "4":
        cls()
        while True:
            print("Server Name -->" + Servername)
            print("Auth ID -->" + Authid)
            print("Console Channel ID -->" + str(Consolechannel))
            print("Server Directory --> Currently changing...")
            print("Given RAM -->" + str(Givenram) + "GB")
            print()
            print("In what directory have you saved the server?")
            print("You only have to put in something like this for me: \"E:\\Minecraft\\letronix\"")
            print("----------------------------------------------------Drive  Folder  Folder containing the server")
            print("You can get this data like this: open your folder containing your server and press the empty part of the bar that tells you your directory. When pressed copy the text and put it here.")
            Serverdirectory = input("--->")
            try:
                for file in os.listdir(Serverdirectory):
                    if ".jar" in file:
                        Jarname = file
                break
            except:
                cls()
                print("This is not a valid directory. No jar file found.")
    elif change == "5":
        cls()
        while True:
            print("Server Name -->" + Servername)
            print("Auth ID -->" + Authid)
            print("Console Channel ID -->" + str(Consolechannel))
            print("Server Directory -->" + Serverdirectory)
            print("Given RAM --> Currently changing...")
            print()
            print("How much RAM would you like to give your server in GB? Whole numbers only.")
            Givenram = input("--->")
            try:
                print(int(Givenram))
                break
            except:
                cls()
                print("You need to enter whole numbers. You cannot have", Givenram, "GB ram.")
    else:
        break
data = {
    "Server name": Servername,
    "Auth id": Authid,
    "Console channel": int(Consolechannel),
    "Server directory": Serverdirectory,
    "Given ram": int(Givenram),
    "Jar name": Jarname
}
datafile = open(pydir + "\data.json", "w")
datajson = json.dumps(data, indent=4)
datafile.write(datajson)
datafile.close()
datafile = open(pydir + "\profiles\\" + Servername + ".json", "w")
datafile.write(datajson)
datafile.close()
cls()
print("Ok we are done here. Now you can hopefully successfully start and it should work. Unless you still have something wrong")
input("----------PRESS ENTER TO END THE PROGRAMM----------")
quit()




