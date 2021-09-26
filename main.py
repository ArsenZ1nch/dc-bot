import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(f"{message.author}: {message.content}")

    if message.content.startswith('!'):
        await message.channel.send('k')
        # arc = await client.fetch_user(710840471827644446)
        arc = await client.fetch_user(int(message.content[1]))
        while True:
            for _ in range(5):
                await arc.send('https://tenor.com/view/spam-gif-18321446')
            for _ in range(5):
                await arc.send('amogus')
            for _ in range(5):
                await arc.send('https://c.tenor.com/11DOBMQ6FcUAAAAM/no-spamming.gif')

client.run('ODkxNTY1Mjc5ODUzODEzNzkw.YVAM3w.F-KDL63VGbZDilMDHIMGYWEoBus')
