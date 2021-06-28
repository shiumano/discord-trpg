from discord.ext import commands
import asyncio
import async_timeout
import importlib
import restart

version = 'd0.1.0'

bot = commands.Bot(command_prefix='r!')

@bot.event
async def on_ready():
    print('Login as {}'.format(bot.user))

@bot.command()
async def update(ctx,filename):
    async with asyncio.ClientSession() as session:
        with async_timeout.timeout(30):
            async with session.get('https://raw.githubusercontent.com/shiumano/discord-trpg/master/{}'.format(filename)) as response:
                code = response.text()
    with open(filename,mode='w') as file:
        file.write(code)

    if file == 'main.py':
        restart.rrstart_program()
		

@bot.command()
async def version(ctx):
    await ctx.send('version:{}'.format(version))


with open('../token') as file:
    bot.run(file.read())