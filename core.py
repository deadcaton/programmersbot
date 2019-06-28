import discord
from config import Configuration
from commands import Commands


class MyClient(discord.Client):
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if channel.id == 576700534225109012:
                lastMessId = channel.last_message_id
                async for message in channel.history(limit=10):
                    if message.id == lastMessId:
                        return await member.send(str(message.content))


commands = Commands()
client = MyClient()


print('--- Start ---')

@client.event
async def on_message(message):
    channel = message.channel

    # Checking and output message of command
    response = commands.define(message.content)
    if response:
        await channel.send(response)

        member = message.author
        print('-- Info:')
        print('- text: ' + message.content)
        print('- authorId: ' + str(member.id))
        print('- authorNickName: ' + str(member))
        print('- date: ' + str(message.created_at) + '\n')

client.run(Configuration.DISCORD_BOT_TOKEN)