from discord.ext import commands
import aiohttp
import async_timeout
import importlib
import restart

version = 'd0.1.1'

bot = commands.Bot(command_prefix='r!')

@bot.event
async def on_ready():
    print('Login as {}'.format(bot.user))

@bot.command()
async def update(ctx,filename):
    async with aiohttp.ClientSession() as session:
        with async_timeout.timeout(30):
            async with session.get('https://raw.githubusercontent.com/shiumano/discord-trpg/master/{}'.format(filename)) as response:
                code = await response.text()
    with open(filename,mode='w') as file:
        file.write(code)

    if file == 'main.py':
        restart.restart_program()
		

@bot.command()
async def version(ctx):
    await ctx.send('Version\n Base:{}'.format(version))


with open('token') as file:
    bot.run(file.read())