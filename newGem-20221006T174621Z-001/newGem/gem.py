import discord
import asyncio
import csv
import os
import string
import random
from discord.ext import commands
from discord.utils import get
intents = discord.Intents.default()
client = discord.Client(intents=intents)

def sanitise(word):
      legalLetters=string.ascii_letters
      combine=""
      for x in range(0,len(word)):
            if word[x] in legalLetters:
                  combine+=word[x]
      return(combine)

def userDataStorage(wantData,sender,recipient,command):
      senderName=sanitise(sender)
      recipientName=sanitise(recipient)
      dataFile= os.path.join(command_path,"{}.csv".format(command))
      file_exists = os.path.isfile(dataFile)
      if file_exists:
        print ("File found")
        pass
      else:
            print("CSV Datagram not found. 404")
            with open(dataFile, 'w', newline='') as csvfile:
                  gemwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                  gemwriter.writerow('')
      data=""
      with open(dataFile, 'w', newline='') as csvfile:
                  gemwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                  gemwriter.writerow(str(recipientName))
                  gemwriter.writerow(str(senderName))

      with open(dataFile, newline='') as csvfile:
            gemreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in gemreader:
                  data+=(', '.join(row))
                  
      if wantData==True:
            return(data)
      else:
            return

def commandStructure(message,messageAuthor,gifs,singular,titleFormat,helpData,dupeData):
          hasPing=False
          isSingle=False
          gSeg=message.split(" ")
          if  len(gSeg)<2:
                isSingle=True
                if singular=="False":
                      print("trigger")
                      error=embedVar = discord.Embed(title=("{} needs a recipient".format(message)),color=0xff0000)
                      return(error)
          #dupeStopper goes here
          print("debug - {}".format(len(gSeg)))
          commandReciever=gSeg[1]
          if ("@") in message and ("!") in message:
                hasPing=True
                pingToID(commandReciever)
          commandTitle=str((titleFormat.format(messageAuthor,commandReciever)))
          gif=("{}".format(gifs[random.randint(0,len(gifs)-1)]))
          embedVar = discord.Embed(title=commandTitle,color=0xe0115f)
          #commandCounter goes here
          embedVar.set_footer(text="{}".format(userDataStorage(True,messageAuthor,commandReciever,gSeg[0])))
          embedVar.set_image(url=gif)
          return(embedVar)

command_path=  r'C:\\Users\\User\\OneDrive\\Desktop\\RecentGEM\\newGem'
def isMainCommand(query):
      finder= os.path.join(command_path,"{}.txt".format(query.split(" ")[0]))
      file_exists = os.path.isfile(finder)
      if file_exists:
        print ("File found")
        pass
      else:
        print("NotMainCMD")
        return(False,False)
    
      f=open((finder), "r")
      commandData=(str(f.read()))
      f.close()
      commandData=(commandData.split("\n"))
      titleFormat=commandData[0]
      canSingle=commandData[1]
      helpInfo=commandData[2]
      dupeState=commandData[3]
      gifs=commandData[4:]
      return(True,titleFormat,canSingle,helpInfo,dupeState,gifs)
      f.close()

@client.event
async def on_ready():
    print('{0.user} selected, launching\n'.format(client))
    guild_count=0
    ServCount = ("")
    for guild in client.guilds:
        currentSelect = str(guild.id)
        ServCount += str("{} ".format(currentSelect))
        guild_count = guild_count + 1
    print("{0} servers: {1}\n".format(guild_count,ServCount))

@client.event
async def on_message(message):
      globalLower = str.lower(message.content[4:])
      channel= client.get_channel(852220515783016479)
      if message.author == client.user or str.lower(message.content[0:3])!="gem":
            return

      mainCommand=isMainCommand(globalLower)
      if mainCommand[0]:
            #print("debug - {}".format(mainCommand[5]))
            await message.channel.send(embed=commandStructure(globalLower,message.author.name,mainCommand[5],mainCommand[2],mainCommand[1],mainCommand[3],mainCommand[4]))










client.run("MTAyNjI0MDExMDM2ODQwNzY2Mg.GaLtFH.1P0SLwJ9KV4re37H8TfZetqbf88MNptH4GzbYE")
