import discord, asyncio
token = "Njg1ODA2NDQwMjI0NjUzMzQx.XmOX8Q.wX2eVWuzEmW1gPx2mLeM44UdAJY"
client = discord.Client() #긴거 대신함

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("아듀로 도움 하면 도와줌"))
    print("준비 되었다")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot: #채팅친 놈이 봇이면 구문 종료
        return None

    if message.content == "아듀로 안녕":
        await message.channel.send("안녕")
        #channel을 author로 바꾸면 DM으로 감

    if message.content == "아듀로 정체":
        await message.channel.send("우주에서 온 이상한 사람")

    if message.content == "아듀로":
        await message.author.send("why?")

    if message.content == "아듀로 뭐라도 해봐":
        await message.channel.send("나는 인공지능이 아니란다^^")

    if message.content == "아듀로 고마워":
        await message.channel.send("당신의 칭찬에 찬사를!")
    
    if message.content == "아듀로 도움":
        embed = discord.Embed(title="아드유로 봇 명령어들", description="이용법은 '아듀로 (명령어)'야. 적다고? 곧 추가할거야 아드유로가 일을 해야할텐데...", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="대화", value="고마워, 뭐라도 해봐, 심영, 정체, 안녕", inline=False)
        embed.add_field(name="이미지", value="김두한, 물리치료사, 심영, 햄스터", inline=False)
        embed.set_footer(text="자주 봐두면 좋아!")
        await message.channel.send("도움이 필요하신가요?", embed=embed)

    if message.content == "아듀로 김두한":
        embed = discord.Embed(title="김두한.", description="1972의 사나이", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685873878723067915/1541313521858.jpg")
        embed.set_footer(text="다함께 폭사하자.")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)

    if message.content == "아듀로 물리치료사":
        embed = discord.Embed(title="마사지사양반.", description="자자 이리로 왓", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874384295952427/1518347904432.gif")
        embed.set_footer(text="그래도 의사니까 안심하자.")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)

    if message.content == "아듀로 심영":
        embed = discord.Embed(title="심영이.", description="국민 고자", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874314138222640/JPEG_20180922_092147.jpg")
        embed.set_footer(text="폭8이다!.")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)

    if message.content == "아듀로 햄스터":
        embed = discord.Embed(title="햄스터?", description="정체불명", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874094411087988/hamster.jpg")
        embed.set_footer(text="나는 그냥 햄스터다 인간들아")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)

client.run("Njg1ODA2NDQwMjI0NjUzMzQx.XmOX8Q.wX2eVWuzEmW1gPx2mLeM44UdAJY")
