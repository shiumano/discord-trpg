from discord.ext import commands
import aiohttp
import async_timeout
import importlib
import botsystem
import restart

version = 'd0.1.1'

bot = commands.Bot(command_prefix='r!')

@bot.event
async def on_ready():
    print('Login as {}'.format(bot.user))

@bot.command()
async def update(ctx,module):
    async with aiohttp.ClientSession() as session:
        with async_timeout.timeout(30):
            async with session.get('https://raw.githubusercontent.com/shiumano/discord-trpg/master/{}.py'.format(module)) as response:
                code = await response.text()
    message = ctx.send('{}.py:Downloaded.')
    with open(module+'.py',mode='w') as file:
        file.write(code)

    if module == 'main':
        await message.edit(content=message.content+'\nRestarting...')
        restart.restart_program()
    else:
		importlib.reload(module)

    if module = 'botsystem':
        for command in botsystem.commands:
            bot.add_command(command)

@bot.command()
async def version(ctx):
    await ctx.send('Version\n Base:{}'.format(version))


with open('token') as file:
    bot.run(file.read())