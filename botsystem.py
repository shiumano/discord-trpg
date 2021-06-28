import discord
import asyncio
import random

version = 'a0.0.1'

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

commands = [dice]