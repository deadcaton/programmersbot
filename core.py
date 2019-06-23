import discord
import asyncio
from config import Configuration
from router import Router


client = discord.Client()
router = Router()


print('--- Start ---\n')


@client.event
async def on_message(message):
    channel = message.channel

    # Checking and output message of command
    response = router.define(message.content)
    if response:
        await channel.send(response)
        print('-- Info:')
        print('- text: ' + message.content)
        print('- author: ' + str(message.author))
        print('- date: ' + str(message.created_at) + '\n')


client.run(Configuration.DISCORD_BOT_TOKEN)