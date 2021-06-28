from discord.ext import commands

version = 'a0.0.1'

bot = commands.Bot(command_prefix='r!')

@bot.event
async def on_ready():
    print('Login as {}'.format(bot.user))

@bot.command()
async def version(ctx):
    await ctx.send('version:{}'.format(version)})


with open('../token') as file:
    bot.run(file.read())