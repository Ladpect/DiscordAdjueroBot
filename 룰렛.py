import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="ad!", case_insensitive=True)

@bot.event
async def on_ready():
  print("Ready!")

@bot.command(pass_context=True)
async def 안녕(ctx):
    await ctx.send("ㅎㅇ")

@bot.command(pass_content=True)
async def 룰렛(ctx):
  num1 = random.randint(0, 10)
  num2 = random.randint(0, 10)
  num3 = random.randint(0, 10)
  if num1 == 0: emo1 = ":zero:"
  if num1 == 1: emo1 = ":one:"
  if num1 == 2: emo1 = ":two:"
  if num1 == 3: emo1 = ":three:"
  if num1 == 4: emo1 = ":four:"
  if num1 == 5: emo1 = ":five:"
  if num1 == 6: emo1 = ":six:"
  if num1 == 7: emo1 = ":seven:"
  if num1 == 8: emo1 = ":eight:"
  if num1 == 9: emo1 = ":nine:"
  if num1 == 10: emo1 = ":keycap_ten:"
  if num2 == 0: emo2 = ":zero:"
  if num2 == 1: emo2 = ":one:"
  if num2 == 2: emo2 = ":two:"
  if num2 == 3: emo2 = ":three:"
  if num2 == 4: emo2 = ":four:"
  if num2 == 5: emo2 = ":five:"
  if num2 == 6: emo2 = ":six:"
  if num2 == 7: emo2 = ":seven:"
  if num2 == 8: emo2 = ":eight:"
  if num2 == 9: emo2 = ":nine:"
  if num2 == 10: emo2 = ":keycap_ten:"
  if num3 == 0: emo3 = ":zero:"
  if num3 == 1: emo3 = ":one:"
  if num3 == 2: emo3 = ":two:"
  if num3 == 3: emo3 = ":three:"
  if num3 == 4: emo3 = ":four:"
  if num3 == 5: emo3 = ":five:"
  if num3 == 6: emo3 = ":six:"
  if num3 == 7: emo3 = ":seven:"
  if num3 == 8: emo3 = ":eight:"
  if num3 == 9: emo3 = ":nine:"
  if num3 == 10: emo3 = ":keycap_ten:"
  embed = discord.Embed(title=":slot_machine:", description=":star:WOW:star:", color=0x4641D9)
  embed.set_author(name="아드유로 봇", icon_url="https://cdn.discordapp.com/attachments/685873675555176492/711115361910521857/21.jpg")
  embed.add_field(name="1", value=emo1, inline=True)
  embed.add_field(name="2", value=emo2, inline=True)
  embed.add_field(name="3", value=emo3, inline=True)
  if num1 == num2 == num3:
      embed.add_field(name="result", value="what the...", inline=False)
      role = discord.utils.get(ctx.guild.roles, name="잭팟 당첨자")
      await ctx.author.add_roles(role)
      await ctx.send(ctx.author.mention + " :tada: 축하드립니다!!! :tada:")
  elif num1 == num2 or num2 == num3 or num1 == num3:
      embed.add_field(name="result", value="OOOF", inline=False)
  else:
      embed.add_field(name="result", value="YEAHHHHHH", inline=False)
  await ctx.send(embed=embed)
