

import discord
import json
import asyncio
import Classes as cl

#Open config.json for data access
with open('/home/pi/Destiny2LFGDiscordBot/resources/config.json') as f:
	config = json.load(f)


client = discord.Client()
testingChannel = 591362273885552660
playerDict = dict()



#on_ready Function
#Inputs: none
#Returns: none
#Description: This function alerts that the bot is now online and ready for commands
async def deletePrevious(botMessage):
	await asyncio.sleep(5)
	await botMessage.delete()

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name = "Looking For Groups"))
	#Update with most recent !lfg request
	print('We have logged in as {0.user}'.format(client))



#on_message Function
#Inputs: message object
#Returns: none
#Description: When a message is sent, checks for commands and executes them.

@client.event
async def on_message(message):



	if message.author == client.user:
		return

	if message.content.startswith('!'): #check if command format
		msgChannel = message.channel
		if msgChannel.type == "text":
			await asyncio.sleep(2)
			await message.delete()

			#Search for users with associated tags
			#format: !lfg {tag}
		if message.content.startswith('!lfg'):
			await message.channel.send("Not implemented yet")

			#Remove a user's tags
		elif message.content.startswith('!clear'):
			await message.channel.send("Not implemented yet")

			#Remove a tag
			#format: !remove {tag}
		elif message.content.startswith('!remove'):
			await message.channel.send("Not implemented yet")

			#adds a new player to the list
			#format: !register
		elif message.content.startswith('!register'):
			newPlayer = cl.Player(message.author.nick, message.author.id)
			if newPlayer.playerID not in playerDict.keys():
				playerDict[newPlayer.playerID] = newPlayer
				await message.channel.send("Success! You have been registered!")
			else:
				await message.channel.send("You are already a registered player.")

			#Adds a tag to the user
			#format: !add {tag}
		elif message.content.startswith('!add'):
			await message.channel.send("Not implemented yet")

			#test command, prints list of all registered players
		elif message.content.startswith("!printlist"):
			out = ""
			for player in playerDict:
				current = playerDict[player]
				out = out+"\n"+ current.printSelf()+"\n"+current.printTags()
			await message.channel.send(out)


		else:#Catches non valid commands
			if message.author.id == 310488286772723712:
				await message.channel.send('Not a valid command.')




client.run(config.get("token"))
