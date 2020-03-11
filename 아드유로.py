import discord, asyncio
import os

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
        embed.add_field(name="대화", value="고마워, 뭐라도 해봐, 정체, 안녕, 따라해 (할말), 주사위 (숫자), ", inline=False)
        embed.add_field(name="이미지", value="김두한, 물리치료사, 심영, 햄스터, ", inline=False)
        embed.add_field(name="기타", value="DM (유저ID) (할말), 추가 예정", inline=False)
        embed.set_footer(text="자주 봐두면 좋아!")
        await message.channel.send("도움이 필요하신가요?", embed=embed)
        
    if message.content == "아듀로 도움pro":
        embed = discord.Embed(title="아드유로 봇 명령어들", description="이용법은 '아듀로 (명령어)'야. 적다고? 곧 추가할거야 아드유로가 일을 해야할텐데...", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="관리", value="뮤트죄수(임명/해제) (유저ID)", inline=False)
        embed.add_field(name="대화", value="고마워, 뭐라도 해봐, 정체, 안녕, 따라해 (할말), 주사위 (숫자), 잘했어", inline=False)
        embed.add_field(name="이미지", value="김두한, 물리치료사, 심영, 햄스터, 둘기이마트", inline=False)
        embed.add_field(name="기타", value="채널확성기 (채널ID) (할말), DM (유저ID) (할말)", inline=False)
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
        
    if message.content == "아듀로 둘기이마트":
        embed = discord.Embed(title="둘기는 이마트를 좋아해", description="난나난나나나나", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/686185101700104215/KakaoTalk_20200308_200354653.jpg")
        embed.set_footer(text="이마트는 둘기를 싫어합니다")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)
        
    if message.content.startswith("아듀로 채널확성기"):
        channel = message.content[10:29] #채널 아이디는 18자, ?번째 글자와 ?번째 글자 사이에 그거 
        msg = message.content[29:] #할말 보내는거
        await client.get_channel(int(channel)).send(msg) #채널 그게 정수값으로 해서 그채널 보내게 함
        
    if message.content.startswith("아듀로 DM"):
        author = message.guild.get_member(int(message.content[7:26])) #유저 아이디
        msg = message.content[26:] #유저에게 할말
        await author.send(msg)
        
    if message.content.startswith("아듀로 뮤트죄수임명"):
        author = message.guild.get_member(int(message.content[11:30])) #유저 아이디
        role = discord.utils.get(message.guild.roles, name="죄수") #죄수 임명 변수
        await author.add_roles(role)#죄수 임명

    if message.content.startswith("아듀로 뮤트죄수해제"):
        author = message.guild.get_member(int(message.content[11:30])) #유저 아이디
        role = discord.utils.get(message.guild.roles, name="죄수") #죄수 변수 찾아라
        await author.remove_roles(role)#죄수 해제
        
    if message.content.startswith("아듀로 따라해"):
        msg = message.content[8:] #할말 보내는거
        await message.channel.send(msg) #할말 보내는거
        
    if message.content.startswith("아듀로 주사위"):
        num = message.content[8:]
        op = random.randint(0, int(num))
        await message.channel.send(op)

    if message.content == "아듀로 잘했어":
        await message.channel.send("yeah! dude.")

        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
