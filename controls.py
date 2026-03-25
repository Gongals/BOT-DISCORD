import discord, random

coin_sides = ['heads', 'tails']
insults = ['idiot', 'clown', 'slowpoke', 'weirdo', 'noob']
responses = ['Yes', 'No', 'Maybe', 'I have no information']


def setup(bot):

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')
    
    @bot.command()
    async def call(ctx, to: discord.User = None):
        if to is None:
            await ctx.send(f'{ctx.author.mention}, give me a user')
        else:
            await ctx.send(f'{ctx.author.mention} called {to.mention}')

    @bot.command()
    async def coinflip(ctx):
        res = random.choice(coin_sides)
        await ctx.send(f'You got: {res}')

    @bot.command()
    async def rate(ctx, to: discord.User = None):
        res_insult = random.choice(insults)
        target = to if to is not None else ctx.author
        await ctx.send(f'{target.mention} is {res_insult}')

    @bot.command()
    async def say(ctx, *, arg: str = ''):
        if arg == '':
            await ctx.send(f'You didn t write anything after the command `!say ...` ||{ctx.author.mention}||')
        else:
            await ctx.send(arg)
    
    @bot.command()
    async def ball(ctx, *, arg: str = ''):
        res_response = random.choice(responses)
        if arg == '':
            await ctx.send('You didn t ask a question. Use:\n```!ball your question```')
        else: 
            await ctx.send(f'Question: {arg}\nAnswer: {res_response}')