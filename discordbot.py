from discord.ext import commands
import aiohttp
import async_timeout
import random
import botsystem
import restart

version = 'a0.0.1'

bot = commands.Bot(command_prefix='r!')

@bot.event
async def on_ready():
    print('Login as {}'.format(bot.user))

@bot.command()
async def update(ctx):
    async with aiohttp.ClientSession() as session:
        with async_timeout.timeout(30):
            async with session.get('https://raw.githubusercontent.com/shiumano/discord-trpg/master/discordbot.py'.format(module)) as response:
                code = await response.text()
    message = ctx.send('Downloaded.')
    with open(__file__,mode='w') as file:
        file.write(code)

    await message.edit(content=message.content+'\nRestarting...')
    restart.restart_program()

@bot.command()
async def version(ctx):
    await ctx.send('Version:{}'.format(version))

@bot.command()
async def dice(ctx,dice):
    arg = dice.split('d')
    if len(arg) != 2:
        await ctx.send('Invalid arg\nUsage:r!dice 1d6')
    else:
        try:
            dice_count = int(arg[0])
            dice_num = int(arg[1])
        except ValueError:
            await ctx.send('Invalid arg\nUsage:r!dice 1d6')
        else:
            result = 0
            for _　in range(dice_count):
                result += random.randint(1,dice_num)
            await ctx.send(result)

with open('token') as file:
    bot.run(file.read())