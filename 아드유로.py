import discord, asyncio, random, datetime
import os, sys, urllib.request, json
import urllib, bs4, request
from discord.ext import commands
import sqlite3
from discord.ext.commands import CommandError
client = commands.Bot(command_prefix="ad", case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("ad도움&ad광산도움"))
    print("준비 되었다")
    print(client.user.name)
    print(client.user.id)
    
@client.command(pass_content=True)
async def 따라해(ctx, *, msg):
    await ctx.channel.purge(limit=1)
    await ctx.send(msg)
    
@client.command(pass_content=True)
async def 질문(ctx):
    await ctx.send("안녕. 난 `마법의 아드곶둥`이야.")
    await asyncio.sleep(1)
    q = ctx.message.content[5:]
    aa = random.randint(1, 2)
    aaa = "blank"
    await ctx.send(f"그래. 질문이 `{q} `라고?")
    await asyncio.sleep(1)
    a = await ctx.send("음... :thinking:")
    await asyncio.sleep(3)
    if aa == 1:
        aaa = "그래"
    elif aa == 2:
        aaa = "안돼"
    await a.edit(content=aaa)


@client.command(pass_content=True)
async def 삭제(ctx, a):
    try:
        if ctx.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=int(a) + 1)
            await asyncio.sleep(3)
            await ctx.send(f"{a}개의 메세지를 삭제했습니다")
        else:
            await ctx.send(f"{ctx.author.name}님은 관리자 권한이 없습니다.")
    except CommandError:
        await ctx.send("봇에게 메세지를 삭제할 수 있는 권한이 없거나 메세지를 삭제하지 못한 것 같습니다.")

@client.command(pass_context=True)
async def 가입(ctx):
    db = sqlite3.connect('adjuero.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id FROM cm WHERE user_id = '{ctx.author.id}'")
    result = cursor.fetchone()
    if result is None:
        sql = ("INSERT INTO cm(user_id, user_name, coin, mine) VALUES(?,?,?,?)")
        val = (ctx.author.id, ctx.author.name, 0, "F")
        cursor.execute(sql, val)
        db.commit()
        await ctx.send(f"{ctx.author.name}님은 이제 가입되었습니다!")
    else:
        await ctx.send(f"{ctx.author.name}님은 이미 가입되어 있습니다.")

@client.command(pass_context=True)
async def 광산건설(ctx):
    db = sqlite3.connect('adjuero.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id, user_name, coin, mine, miner, 지비석, 삼다석, 방패석, 로아석, 초아석, 염라석, 화석, 태양석, 사랑석, 아드석 FROM cm WHERE user_id = '{ctx.author.id}'")
    result = cursor.fetchone()
    if result is None:
        await ctx.send("`ad가입`을 통해 가입을 해주세요.")
    elif result[3] == "T":
        await ctx.send("{ctx.author.name}님은 이미 광산이 있습니다.")
    else:
        sql = (f"UPDATE cm SET miner = ?, 지비석 = ?, 삼다석 = ?, 방패석 = ? WHERE user_id = ?")
        val = (1, 0, 0, 0, ctx.author.id)
        cursor.execute(sql, val)
        sql3 = (f"UPDATE cm SET 로아석 = ?, 초아석 = ?, 염라석 = ?, 화석 = ?, 태양석 = ?, 사랑석 = ?, 아드석 = ? WHERE user_id = ?")
        val3 = (0, 0, 0, 0, 0, 0, 0, ctx.author.id)
        cursor.execute(sql3, val3)
        sql2 = ("UPDATE cm SET mine = ? WHERE user_id = ?")
        val2 = ("T", ctx.author.id)
        cursor.execute(sql2, val2)
        db.commit()
        await ctx.send(f"{ctx.author.name}님의 광산을 만들었습니다!")

@client.command(pass_context=True)
async def 광산(ctx):
    db = sqlite3.connect('adjuero.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id, user_name, coin, mine, miner, 지비석, 삼다석, 방패석, 로아석, 초아석, 염라석, 화석, 태양석, 사랑석, 아드석 FROM cm WHERE user_id = '{ctx.author.id}'")
    result = cursor.fetchone()
    if result is None:
        await ctx.send("`ad가입`을 통해 가입을 해주세요.")
    elif result[3] == "F":
        await ctx.send("`ad광산건설`을 통해 광산을 먼저 만들어주세요!")
    else:
        embed = discord.Embed(title=f":pick: {ctx.author.name}님의 창고 :pick:", description="아드광산", color=0x4641D9)
        embed.add_field(name=":pick: 광부 :pick:", value=f"{result[4]}명", inline=False)
        embed.add_field(name=":dove: 지비석 :dove:", value=f"{result[5]}개", inline=True)
        embed.add_field(name=":droplet: 삼다석 :droplet:", value=f"{result[6]}개", inline=True)
        embed.add_field(name=":shield: 방패석 :shield:", value=f"{result[7]}개", inline=True)
        embed.add_field(name=":full_moon: 로아석 :full_moon:", value=f"{result[8]}개", inline=True)
        embed.add_field(name=":dizzy: 초아석 :dizzy:", value=f"{result[9]}개", inline=True)
        embed.add_field(name=":fire: 염라석 :fire:", value=f"{result[10]}개", inline=True)
        embed.add_field(name=":bone: 화석 :bone:", value=f"{result[11]}개", inline=True)
        embed.add_field(name=":sun_with_face: 태양석 :sun_with_face:", value=f"{result[12]}개", inline=True)
        embed.add_field(name=":heart: 사랑석 :heart:", value=f"{result[13]}개", inline=True)
        embed.add_field(name=":boom: 아드석 :boom:", value=f"{result[14]}개", inline=True)
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def 광부고용(ctx):
    db = sqlite3.connect('adjuero.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id, user_name, coin, mine, miner, 지비석, 삼다석, 방패석, 로아석, 초아석, 염라석, 화석, 태양석, 사랑석, 아드석 FROM cm WHERE user_id = '{ctx.author.id}'")
    result = cursor.fetchone()
    miner = int(100 + int(result[4] * 6000))
    if result is None:
        await ctx.send("`ad가입`을 통해 가입을 해주세요.")
    elif result[3] == "F":
        await ctx.send("`ad광산건설`을 통해 광산을 먼저 만들어주세요!")
    elif not int(result[2]) >= int(100 + int(result[4] * 6000)):
        await ctx.send("광부를 고용하는데엔 " + str(int(100 + int(result[4] * 6000))) + f":euro: 의 비용이 소요됩니다. {ctx.author.name}님은 현재 {result[2]} :euro: 를 가지고 계십니다.")
    else:
        sql = (f"UPDATE cm SET coin = ? WHERE user_id = ?")
        val = (int(result[2] - miner), ctx.author.id)
        cursor.execute(sql, val)
        sql1 = (f"UPDATE cm SET miner = ? WHERE user_id = ?")
        val1 = (int(result[4] + 1), ctx.author.id)
        cursor.execute(sql1, val1)
        db.commit()
        await ctx.send("광부를 고용하였습니다!")

@client.command(pass_context=True)
async def 채굴(ctx):
    pro = random.randint(1, 100)
    sl = random.randint(5, 10)
    m = "blank"
    num = 0
    db = sqlite3.connect('adjuero.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id, user_name, coin, mine, miner, 지비석, 삼다석, 방패석, 로아석, 초아석, 염라석, 화석, 태양석, 사랑석, 아드석 FROM cm WHERE user_id = '{ctx.author.id}'")
    result = cursor.fetchone()
    if result is None:
        await ctx.send("`ad가입`을 통해 가입을 해주세요.")
    elif result[3] == "F":
        await ctx.send("`ad광산건설`을 통해 광산을 먼저 만들어주세요!")
    else:
        msg = await ctx.send(":pick: 채굴을 시작합니다 :pick:")
        await asyncio.sleep(sl)
        if pro >= 1 and pro <= 23:
            m = ":dove: 지비석 :dove:"
            num = random.randint(5, 17)
            sql = (f"UPDATE cm SET 지비석 = ? WHERE user_id = ?")
            val = (int(result[5]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 24 and pro <= 39:
            m = ":droplet: 삼다석 :droplet:"
            num = random.randint(4, 12)
            sql = (f"UPDATE cm SET 삼다석 = ? WHERE user_id = ?")
            val = (int(result[6]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 40 and pro <= 51:
            m = ":shield: 방패석 :shield:"
            num = random.randint(3, 9)
            sql = (f"UPDATE cm SET 방패석 = ? WHERE user_id = ?")
            val = (int(result[7]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 52 and pro <= 65:
            m = ":full_moon: 로아석 :full_moon:"
            num = random.randint(2, 6)
            sql = (f"UPDATE cm SET 로아석 = ? WHERE user_id = ?")
            val = (int(result[8]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 66 and pro <= 78:
            m = ":dizzy: 초아석 :dizzy:"
            num = random.randint(3, 6)
            sql = (f"UPDATE cm SET 초아석 = ? WHERE user_id = ?")
            val = (int(result[9]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 79 and pro <= 85:
            m = ":fire: 염라석 :fire:"
            num = random.randint(2, 5)
            sql = (f"UPDATE cm SET 염라석 = ? WHERE user_id = ?")
            val = (int(result[10]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 86 and pro <= 90:
            m = ":bone: 화석 :bone:"
            num = random.randint(2, 8)
            sql = (f"UPDATE cm SET 화석 = ? WHERE user_id = ?")
            val = (int(result[11]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 91 and pro <= 95:
            m = ":sun_with_face: 태양석 :sun_with_face:"
            num = random.randint(2, 6)
            sql = (f"UPDATE cm SET 태양석 = ? WHERE user_id = ?")
            val = (int(result[12]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 96 and pro <= 98:
            m = ":heart: 사랑석 :heart"
            num = random.randint(2, 6)
            sql = (f"UPDATE cm SET 사랑석 = ? WHERE user_id = ?")
            val = (int(result[13]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        elif pro >= 99 and pro <= 100:
            m = ":boom: 아드석 :boom:"
            num = random.randint(1, 5)
            sql = (f"UPDATE cm SET 아드석 = ? WHERE user_id = ?")
            val = (int(result[14]) + int(int(num) * int(result[4])), ctx.author.id)
            cursor.execute(sql, val)
            db.commit()
        await msg.edit(content=f"{m}을 {str(num * result[4])}개 얻었다! (광부가 {result[4]}명이어서 {result[4]}배를 얻습니다!)")


    
@client.event
async def on_message(message):
    if message.author.bot: #채팅친 놈이 봇이면 구문 종료
        return None

    if message.content in ["아듀로 안녕", "ad안녕"]:
        await message.channel.send("안녕")
        #channel을 author로 바꾸면 DM으로 감
        
    if message.content in ["아듀로 도움", "ad도움", "adhelp"]:
        embed = discord.Embed(title="아드유로 봇 명령어들", description="이용법은 ad(명령어)야. 적다고? 곧 추가할거야 아드유로가 일을 해야할텐데...", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="관리", value="`ad삭제 {삭제량}`", inline=False)
        embed.add_field(name="대화", value="`ad대화 도움` 또는 `ad대도`에서 확인하세요", inline=False)
        embed.add_field(name="이미지", value="`ad이미지 도움` 또는 `ad이도`에서 확인하세요", inline=False)
        embed.add_field(name="기타", value="`ad거꾸로 {할말}`, `ad질문 {질문}`(O 또는 X만 가능)", inline=False)
        embed.add_field(name="각종 공식", value="`ad에너지 {질량값}`, `ad제곱 {숫자}`, `ad루트 {숫자} {근}`", inline=False)
        embed.add_field(name="게임", value="`ad룰렛`", inline=False)
        embed.add_field(name="밀크초코 온라인", value="`ad밀초 도움`", inline=False)
        embed.add_field(name="아드코인", value="`ad광산도움`", inline=False)
        embed.add_field(name="번역", value="`ad한영`(한->영), `ad영한`(영->한)", inline=False)
        embed.set_footer(text="자주 봐두면 좋아!")
        await message.channel.send("도움이 필요하신가요?", embed=embed)
        embed2 = discord.Embed(title="문의", description="문의", color=0x4641D9)
        embed2.add_field(name="문의방법", value="`adjuero#5331`로 DM주시면 됩니다", inline=False)
        await message.channel.send(embed=embed2)
        
    if message.content == "ad광산도움":
        embed3 = discord.Embed(title=":pick: 아드광산 :pick:", color=0x4641D9)
        embed3.add_field(name="`ad가입`", value="가입합니다.", inline=False)
        embed3.add_field(name="`ad지갑`", value="아드코인 소유량을 확인합니다.", inline=False)
        embed3.add_field(name="`ad광산건설`", value="자신의 광산을 짓습니다", inline=False)
        embed3.add_field(name="`ad광산`", value="광부 수, 광물 수를 확인합니다", inline=False)
        embed3.add_field(name="`ad채굴`", value="채굴합니다. 무작위로 광물 종류와 갯수가 정해집니다.", inline=False)
        embed3.add_field(name="`ad광부고용`", value="광부를 고용합니다. 광부가 많을수록 채굴량이 많아집니다.", inline=False)
        embed3.add_field(name="`ad판매 {광물} {갯수(모두)}`", value="광물을 판매해 아드코인을 획득합니다.", inline=False)
        await message.channel.send(embed=embed3)
        
    if message.content in ["ad대화 도움", "ad대도"]:
        embed = discord.Embed(title="대화명령어들!", description="말해라 아듀로 봇", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="대화명령어", value="`ad안녕`, `ad따라해 {할말}`, `ad주사위 {숫자}`, `ad잘했어`, `ad나 어때?`, `ad레니`", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content in ["ad이미지 도움", "ad이도"]:
        embed = discord.Embed(title="이미지명령어들", description="이미지 노예 아듀로 봇", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="이미지", value="`ad김두한`, `ad물리치료사`, `ad심영`, `ad김치싸대기`, `ad김치수거`, `adㅌㅌ`, `ad포나춤`, `ad샌즈`, `ad시공`", inline=False)
        await message.channel.send(embed=embed)
    
    if message.content in ["아듀로 나 어때?", "ad나 어떄?"]:
        embed = discord.Embed(title="관심법", description="그는 김두한의 또다른 인격체라 카더라", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688029161956311060/2.jpg")
        embed.set_footer(text="금부장?")
        await message.channel.send("내가 관심법으로 가만히 보아하니...", embed=embed)
        await asyncio.sleep(4)
        await message.channel.send("네놈 머리속엔 마구니가 가득차있어")
        
    if message.content.startswith("ad에너지"):
        m = message.content[6:]
        embed = discord.Embed(
            title="E = mc^2",
            description="에너지를 구해드립니다",
            color=0x4641D9
        )
        embed.add_field(name="m", value=m, inline=False)
        embed.add_field(name="결과", value=int(299792458 ** 2 * int(m)), inline=False)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("ad레니"):
        Lenny = ["( ͡° ͜ʖ ͡°)", "( ͠° ͟ʖ ͡°)", "( ͡~ ͜ʖ ͡°)", "( ͡ʘ ͜ʖ ͡ʘ)", "( ͡o ͜ʖ ͡o)", "(° ͜ʖ °)", "( ‾ʖ̫‾)", 
        "( ಠ ͜ʖಠ)", "( ͡° ʖ̯ ͡°)", "( ͡ಥ ͜ʖ ͡ಥ)", "༼  ͡° ͜ʖ ͡° ༽", "(▀̿Ĺ̯▀̿ ̿)", "( ✧≖ ͜ʖ≖)", "(ง ͠° ͟ل͜ ͡°)ง", 
        "(͡ ͡° ͜ つ ͡͡°)", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "(✿❦ ͜ʖ ❦)", "ᕦ( ͡° ͜ʖ ͡°)ᕤ", "( ͡° ͜ʖ ͡°)╭∩╮", 
        "(╯ ͠° ͟ʖ ͡°)╯┻━┻", "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)", "ಠ_ಠ"]
        r = random.randrange(0, len(Lenny))
        print("랜덤수 값 :" + str(r))
        print(Lenny[r])
        await message.channel.send(embed=discord.Embed(description=Lenny[r]))
   
    if message.content in ["아듀로 김두한", "ad김두한"]:
        embed = discord.Embed(title="김두한.", description="1972의 사나이", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685873878723067915/1541313521858.jpg")
        embed.set_footer(text="다함께 폭사하자.")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 물리치료사", "ad물리치료사"]:
        embed = discord.Embed(title="마사지사양반.", description="자자 이리로 왓", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874384295952427/1518347904432.gif")
        embed.set_footer(text="그래도 의사니까 안심하자.")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 심영", "ad심영"]:
        embed = discord.Embed(title="심영이.", description="국민 고자", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874314138222640/JPEG_20180922_092147.jpg")
        embed.set_footer(text="폭8이다!.")
        await message.channel.send("아듀로 이미지", embed=embed)
        
    if message.content in ["아듀로 김치수거", "ad김치수거"]:
        embed = discord.Embed(title="김치수거중", description="내 아까운 김치", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311211783356426/a8300e3efe453a83.gif")
        embed.set_footer(text="김치를 아끼자.")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 김치싸대기", "ad김치싸대기"]:
        embed = discord.Embed(title="예끼 이놈", description="김치워리어", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311226354237477/068b27a2f06240e8.gif")
        embed.set_footer(text="김치워리어 운다")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 ㅌㅌ", "adㅌㅌ"]:
        embed = discord.Embed(title="모두 다음에 만나요", description="사라짐", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311120640999425/1583662278990.gif")
        embed.set_footer(text="잘가")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 시공", "ad시공"]:
        embed = discord.Embed(title="시공의 폭풍은 정말 최고야!", description="히오스", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311711677415424/1535025935602.gif")
        embed.set_footer(text="히오스는 최고가 맞습니다. 맞다고요")
        await message.channel.send("아듀로 이미지", embed=embed)
        
    if message.content in ["아듀로 포나춤", "ad포나춤"]:
        embed = discord.Embed(title="F.O.R.T.N.I.T.E", description="D.E.F.A.U.L.T D.A.N.C.E", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/689719145855844382/1328177857dfa41ab6bb71bf3166f42e.gif")
        embed.set_footer(text="WOW")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 샌즈", "ad샌즈"]:
        embed = discord.Embed(title="WA! SANS!", description="참고로 이거 겁.나.어.렵.습.니.다", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/689720396345638941/1537569816_hqx7okmi64c11.gif")
        embed.set_footer(text="(SANS LAUGH)")
        await message.channel.send("아듀로 이미지", embed=embed)
        
    if message.content.startswith("ad주사위"):
        num = message.content[6:]
        op = random.randint(0, int(num))
        await message.channel.send(op)

    if message.content == "ad밀초 도움":
        embed = discord.Embed(title="아듀로 봇의 밀초 정보 저장소", description="영웅들과 총 정보 등등 많은 정보를 제공합니다", color=0x4641D9)
        embed.add_field(name="캐릭터", value="`ad어썰트`, `ad메딕`, `ad바머`, `ad리콘`, `ad고스트`, `ad쉴드`, `ad런쳐`, `ad인비`, `ad후크`, `ad미오캣`, `ad데페`, `ad아이언`, `ad캐로그`, `ad크리미`, `ad휠레그`, `ad에어`, `ad일렉트릭`, `ad블레이드`, `ad스위니`, `ad마고`", inline=False)
        embed.add_field(name="총기", value="(유저들이 주로 쓰는 총으로 추가 예정)", inline=False)
        embed.add_field(name="유의사항 1", value="1.정보가 맞지 않을 수 있습니다.(만약 정보가 맞지 않거나 추가할 부분이 있다면 증명자료와 함께 `아드유로#5331`로 DM주세요)", inline=False)
        embed.add_field(name="유의사항 2", value="2.원뚝여부에 총기 옆에 '(S)'가 있다면 리콘, 에어의 스킬사용중 나타나는 데미지임을 밝히는 바입니다.", inline=False)
        embed.add_field(name="원뚝여부 `최대뎀 기준 {원래뎀}/{스킬추가뎀(스나한정)}`", value="`에땁 168/184`, `알디 173/190`, `스피라 184/202`, `신스나 193/212`, `클샷 220`, `신샷 230`", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad어썰트"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 어썰트", description="굴러라 굴러", color=0x4641D9)
        embed.add_field(name="체력", value="200", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="스피라(S) 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="1.6초동안 구른다. 이때 적군과 부딫히면 0.4초마다 40뎀이 들어간다. 추가적으론 구르기 상태에선 피격데미지 절반감소, 모든 판정이 몸샷이 된다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634145853308962/cdb73b014dbd173a.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad메딕"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 메딕", description="의사양반! 이쪽에...", color=0x4641D9)
        embed.add_field(name="체력", value="210", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="신스나(S) 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="아군 1명의 체력을 90회복한다. 시체가 터지지 않은 팀원을 90체력으로 부활, 잠시동안 무적상태 부여, 부활한 아군 데스기록제거를 할 수 있다. 그리고 스킬 시전시 자신의 체력 30회복한다.", inline=False)
        embed.add_field(name="배틀로얄", value="스킬 사용불가(솔로 한정)로 인해 회복템 사용속도가 증가한다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634142053269570/741a1317414241ce.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad바머"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 바머", description="다함께 폭사하자.", color=0x4641D9)
        embed.add_field(name="체력", value="225", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="100/13", inline=True)
        embed.add_field(name="원뚝여부", value="X", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 앞으로 돌진후 폭파하며 최대 250 데미지를 입힌다. (이 스킬은 벽뒤에 숨어도 맞는다.)", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634143408029721/f605c923f31b3f55.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad리콘"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 리콘", description="버프를 굉장히 많이 먹는 아이.", color=0x4641D9)
        embed.add_field(name="체력", value="150", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="70/32", inline=True)
        embed.add_field(name="원뚝여부", value="클샷 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 지형투시와 인비스킬, 크리미 지뢰(스킬)을 감지할 수 있다.(아군 전체적용, 크리미 지뢰(스킬)파괴 가능) 그리고 스킬쓰는 동안에는 스나뎀이 10% 상승한다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634139909849114/3f5b28ad7369b2e4.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad쉴드"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 쉴드", description="방패에 의존하는 은근 대처하기 어렵고 단단한 아이", color=0x4641D9)
        embed.add_field(name="체력", value="170", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="135/15", inline=True)
        embed.add_field(name="원뚝여부", value="X", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 8초간 방패를 들며 총알을 막는다.(단, 적군의 스킬은 막을 수 없다), 방패를 들면 이동속도가 느려지며 총을 바꿀 수 없다.", inline=False)
        embed.add_field(name="부가사항", value="스킬을 공중에서 쓰면 잠깐 공중에서 멈추었다가 아주 빠르게 떨어진다. 이것을 응용하면 잔기술을 만들 수 있다.", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634144347422745/7c0b2093df6cb7fb.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad고스트"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 고스트", description="뒤치 전문가", color=0x4641D9)
        embed.add_field(name="체력", value="140", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="30/20", inline=True)
        embed.add_field(name="원뚝여부", value="알디 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰고 특정 위치에 에임을 갖다대면 그곳으로 순간이동한다. (단, 무조건 바닥에 에임을 갖다대야한다. 벽 or 천장에 할 시 스킬이 발동이 안된다.)", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634071039639587/82eb70e95996fb6b.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)
        
    if message.content.startswith("ad런쳐"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 런쳐", description="북쪽의 김동지를 보는 듯 하다.", color=0x4641D9)
        embed.add_field(name="체력", value="250", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="X", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 에임이 있는 부분에 광역 공격을 한다. 스킬 시전 하기전에 약 3초의 딜레이가 있다. 최소 데미지는 50이며 데미지는 220대 초반까지 들어간다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/688011394955739146/6d760227c908d2fa.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad인비"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 인비", description="이 아이는 on/off 가능합니다", color=0x4641D9)
        embed.add_field(name="체력", value="165", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="에땁 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 잠깐의 딜레이 후 8초간 은신상태가 된다. 이때 공격(수류탄 투척 포함)을 하면 은신이 풀리며 은신상태에서 근접무기로 상대공격시 데미지가 50% 더 들어간다.", inline=True)
        embed.add_field(name="유의사항", value="리콘 스킬, 캐로그 포탑이 적군에게 존재한다면 인비가 은신을 써도 적군에게는 인비가 보인다.", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/688011390119837713/b369e79c7587b9b7.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad후크"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 후크", description="준비됐나요? 네, 네, 선장님!", color=0x4641D9)
        embed.add_field(name="체력", value="190", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="40/7", inline=True)
        embed.add_field(name="원뚝여부", value="신샷", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰고 파란에임이 되었을때 적군에게 에임을 갖다대면 적군이 끌려온다. 이때 스킬 적용시 50데미지를 입히며 끌려오다 구조물에 걸릴시 더이상 끌려오지 않는다. 그리고 끌어올 수 있는 최대 거리는 확인 결과 약 32m 까지다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/688011393026359300/d3513a9979172c1b.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)
        
    if message.content.startswith("ad미오캣"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 미오캣", description="냥냥군단의 근원지.", color=0x4641D9)
        embed.add_field(name="체력", value="185", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="신스나 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬 사용시 돌진하며 이때 적군과 부딫히면 130데미지를 입힌다. 돌진거리는 총의 무게에 비례하며 100% 기준 돌진거리는 약 24m 이다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/688281235222560779/399ded0af0cef27c.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad아이언"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 아이언", description="디즈니에서 소송걸어도 할 말 없다", color=0x4641D9)
        embed.add_field(name="체력", value="180", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="90/18", inline=True)
        embed.add_field(name="원뚝여부", value="X", inline=True)
        embed.add_field(name="스킬", value="스킬 사용시 5초간 받는 데미지를 30%만 받는다. 이때 총 사용, 수류탄, 점프가 가능하다", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/688281237751595057/c0c18f37b9cbb53d.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad데페"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 데페", description="아 대패삽겹살 먹고싶다.", color=0x4641D9)
        embed.add_field(name="체력", value="190", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="40/7", inline=True)
        embed.add_field(name="원뚝여부", value="신샷", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 약 3초간의 딜레이 후 스킬을 시전, 타겟팅이 된 적군(들)에게 총합 500데미지를 준다. 데미지 분배는 랜덤이며 대부분 5의 배수이다.", inline=True)
        embed.add_field(name="유의사항", value="스킬 시전 중(딜레이 중) 사망시 스킬은 취소된다.", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/688281239261937664/0f3e7019db08410e.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad크리미"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 크리미", description="처음 나올때 얘 이름 푸푸였다", color=0x4641D9)
        embed.add_field(name="체력", value="185", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="신스나 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬 사용시 적군에겐 보이지 않는 지뢰를 설치하며 적군이 밟을시 80데미지가 들어간다. 이 지뢰는 80체력이며 수류탄, 총(리콘 스킬로 드러났을 경우)로 제거 가능하다", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/691973327421571142/04a0b43509f93c4c.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad캐로그"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 캐로그", description="캐로그 5인큐 만나면 진짜 무섭다", color=0x4641D9)
        embed.add_field(name="체력", value="155", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="65/29", inline=True)
        embed.add_field(name="원뚝여부", value="클샷 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 사용하면 잠깐의 딜레이 후 적을 공격하는 포탑을 설치한다. 0.5초마다 9데미지를 주며 인비의 은신을 감지할 수 있다", inline=False)
        embed.add_field(name="유의사항", value="사망 중에는 포탑이 아무것도 하지 않으며 일정시간이 지나면 사라지며, 포탑이 있는 상태로 스킬을 쓰면 기존 포탑이 사라지고 스킬을 쓴곳에 포탑이 설치된다.", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/691973325697581056/d177c0504ce48078.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad휠레그"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 휠레그", description="I'm so fast f**k boiiii", color=0x4641D9)
        embed.add_field(name="체력", value="190", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="알디(S) 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 사용할 시 속도가 빨라지며 약 60% 정도 빨라지며 6초 지속된다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/691973311214911519/67656ca552613712.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad에어"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 에어", description="눈 덮인 숲속 마을 꼬마 펭귄 나가신다", color=0x4641D9)
        embed.add_field(name="체력", value="180", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="스피라 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 사용할 시 그 자리에서 높게 점프하며 높이는 약 12m 정도 된다. 스킬을 쓰고 공중에서 스나로 공격하면 데미지가 10퍼센트 추가로 들어간다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/691973322954768414/919dde290529189d.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad블레이드"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 블레이드", description="칼 하나로 쓱싹 하는 벌레", color=0x4641D9)
        embed.add_field(name="체력", value="165", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="에땁 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 에임 방향으로 12m 돌진하며 적군에 맞으면 적군은 200데미지를 입는다. 스킬로 적군이 죽으면 스킬을 바로 또 쓸 수 있다.(돌진 거리는 총 무게에 비례한다.)", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/691973319888470016/e589eb34d9b03bea.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad마고"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 마고", description="샤머니즘 그 자체", color=0x4641D9)
        embed.add_field(name="체력", value="165", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="에땁 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬이 다 차면 두 상태가 번갈아 가면서 바뀐다. 타이밍 맞게 누르면 발동된다.", inline=False)
        embed.add_field(name="스킬(버프)", value="반경 3m 범위 안에 초록색 마법진이 생기며 초당 35 체력을 회복시킨다.", inline=True)
        embed.add_field(name="스킬(디버프)", value="반경 6m 범위 안에 적색 마법진이 생기며 적군의 이속을 약 50% 감소시킨다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/691973086651744286/78587f88a293c334.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad일렉트릭"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 일렉트릭", description="번쩍번쩍 번개따라 찌리찌리 짜라짜라", color=0x4641D9)
        embed.add_field(name="체력", value="145", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="55/24", inline=True)
        embed.add_field(name="원뚝여부", value="스피라(S) 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰고 적군에게 에임을 갖다대면 적군은 감전 상태가 되며 공격 불능, 배리어 삭제 디버프를 먹는다. 지속시간은 4초이며 스킬 적중시 1데미지가 들어간다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/691973324129173544/f89736c26cf2c27a.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("ad스위니"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 스위니", description="동해번쩍 서해번쩍", color=0x4641D9)
        embed.add_field(name="체력", value="175", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="스피라 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 당근을 던지고 일정 시간안에 스킬 버튼을 다시 누르면 당근이 있는 자리로 순간이동 한다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/691973322296131654/c23e921847396022.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)
        
    if message.content.startswith("ad타이머"):
        time = message.content[6:]
        p = message.author.mention
        t = await message.channel.send(time)
        await asyncio.sleep(1)
        for sec in range(1, int(time)):
                time = int(time) - 1
                await t.edit(content=str(int(time)))
                await asyncio.sleep(1)
        else:
            await message.channel.send(p + " " + str(int(sec) + 1) + "초가 지났습니다!")
            
    if message.content.startswith("ad제곱"):
        n = message.content.split(" ")
        embed = discord.Embed(title="제곱", description="^", color=0x4641D9)
        embed.add_field(name="1", value=n[1], inline=True)
        embed.add_field(name="2", value=n[2], inline=True)
        embed.add_field(name="결과", value="답은 " + str(int(n[1]) ** int(n[2])) + " 입니다", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith("ad루트"):
        l = message.content.split(" ")
        embed = discord.Embed(title="뿌리", description="(대충 루트)", color=0x4641D9)
        embed.add_field(name="1", value=l[1], inline=True)
        embed.add_field(name="2", value=l[2], inline=True)
        embed.add_field(name="결과", value="답은 " + str(int(l[1]) ** float(1 / float(l[2]))) + " 입니다", inline=False)
        await message.channel.send(embed=embed)
            
    if message.content.startswith("ad거꾸로"):
        say = message.content[6:]
        embed = discord.Embed(title="로꾸거", description="로대반 은상세 이", color=0x4641D9)
        embed.add_field(name="결과", value=":arrows_counterclockwise: " + " " + str(say[::-1]), inline=False)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("ad한영"):
        learn = message.content.split(" ")
        Text = ""

        client_id = "UPlhusJW5Lhg6SIKuzfm"
        client_secret = "Lch08eFSWA"

        url = "https://openapi.naver.com/v1/papago/n2mt"
        print(len(learn))
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize): #띄어쓰기 한 텍스트들 인식함
            Text = Text+" "+learn[i]
        encText = urllib.parse.quote(Text)
        data = "source=ko&target=en&text=" + encText

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(request, data=data.encode("utf-8"))

        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            data = response_body.decode('utf-8')
            data = json.loads(data)
            tranText = data['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        print('번역된 내용 :', tranText)

        embed = discord.Embed(
            title=':flag_kr: :arrow_right: :flag_um:',
            description=tranText,
            color=0x4641D9
        )
        await message.channel.send(embed=embed)

    if message.content.startswith("ad영한"):
        learn = message.content.split(" ")
        Text = ""

        client_id = "UPlhusJW5Lhg6SIKuzfm"
        client_secret = "Lch08eFSWA"

        url = "https://openapi.naver.com/v1/papago/n2mt"
        print(len(learn))
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize): #띄어쓰기 한 텍스트들 인식함
            Text = Text+" "+learn[i]
        encText = urllib.parse.quote(Text)
        data = "source=en&target=ko&text=" + encText

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(request, data=data.encode("utf-8"))

        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            data = response_body.decode('utf-8')
            data = json.loads(data)
            tranText = data['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        print('번역된 내용 :', tranText)

        embed = discord.Embed(
            title=':flag_um: :arrow_right: :flag_kr:',
            description=tranText,
            color=0x4641D9
        )
        await message.channel.send(embed=embed)
        
    if message.content == "ad프로필":
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x4641D9)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉넴", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        
    if message.content == "ad룰렛":
        db = sqlite3.connect('adjuero.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id FROM cm WHERE user_id = '{message.author.id}'")
        result = cursor.fetchone()
        if result is None:
            await message.channel.send("`ad가입`을 통해 가입해주세요.")
        else:
            mention = message.author.mention
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            num3 = random.randint(0, 10)
            coi = random.randint(1, 7)
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
                role = discord.utils.get(message.guild.roles, name="잭팟 당첨자")
                await author.add_roles(role)
                await message.channel.send(message.author.mention + " :tada: 축하드립니다! :tada:")
                db = sqlite3.connect('adjuero.db')
                cursor = db.cursor()
                cursor.execute(f"SELECT user_id, user_name, coin FROM cm WHERE user_id = '{message.author.id}'")
                result = cursor.fetchone()
                coin = int(result[2])
                sql = ("UPDATE cm SET coin = ? WHERE user_id = ?")
                val = (coin + 10, message.author.id)
                cursor.execute(sql, val)
                db.commit()
                await message.channel.send("100 :euro: 얻었습니다!")
            elif num1 == num2 or num2 == num3 or num1 == num3:
                embed.add_field(name="result", value="OOOF", inline=False)
                db = sqlite3.connect('adjuero.db')
                cursor = db.cursor()
                cursor.execute(f"SELECT user_id, user_name, coin FROM cm WHERE user_id = '{message.author.id}'")
                result = cursor.fetchone()
                coin = int(result[2])
                sql = ("UPDATE cm SET coin = ? WHERE user_id = ?")
                val = (coin + coi, message.author.id)
                cursor.execute(sql, val)
                db.commit()
                await message.channel.send(f"{coi} :euro: 얻었습니다!")
            else:
                embed.add_field(name="result", value="YEAHHHHHH", inline=False)
            await message.channel.send(embed=embed)
            await message.channel.send(mention)
        
    if message.content == "ad프로필":
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x4641D9)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉넴", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "ad지갑":
        db = sqlite3.connect('adjuero.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id, user_name, coin FROM cm WHERE user_id = '{message.author.id}'")
        result = cursor.fetchone()
        if result is None:
            await message.channel.send("`ad가입`을 통해 가입을 해주세요.")
        else:
            coin = str(result[2])
            embed = discord.Embed(title=f"{message.author.name}님의 :euro: 지갑 :euro:", color=0x4641D9)
            embed.add_field(name="아드코인", value=coin + " :euro:", inline=True)
            await message.channel.send(embed=embed)

    if message.content.startswith("ad판매"):
        sp = message.content.split(" ")
        mi = sp[1]
        nu = sp[2]
        sell = 0
        t = 0
        db = sqlite3.connect('adjuero.db')
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id, user_name, coin, mine, miner, 지비석, 삼다석, 방패석, 로아석, 초아석, 염라석, 화석, 태양석, 사랑석, 아드석 FROM cm WHERE user_id = '{message.author.id}'")
        result = cursor.fetchone()
        if result is None:
            await message.channel.send("`ad가입`을 통해 가입을 해주세요.")
        elif result[3] == "F":
            await message.channel.send("`ad광산건설`을 통해 광산을 먼저 만들어주세요!")
        else:
            if mi == "지비석":
                sell = 1
                t = 5
            elif mi == "삼다석":
                sell = 3
                t = 6
            elif mi == "방패석":
                sell = 5
                t = 7
            elif mi == "로아석":
                sell = 10
                t = 8
            elif mi == "초아석":
                sell = 13
                t = 9
            elif mi == "염라석":
                sell = 15
                t = 10
            elif mi == "화석":
                sell = 25
                t = 11
            elif mi == "태양석":
                sell = 30
                t = 12
            elif mi == "사랑석":
                sell = 50
                t = 13
            elif mi == "아드석":
                sell = 100
                t = 14
            if (str(type(nu)) == "<class 'int'>"):
                if result[t] < int(nu):
                    await message.channel.send(f"{message.author.name}님의 {mi}는 {result[t]}개입니다.")
                else:
                    sql = (f"UPDATE cm SET coin = ?, {mi} = ? WHERE user_id = ?")
                    val = (int(result[2] + int(nu) * sell), int(result[t] - int(nu)),message.author.id)
                    cursor.execute(sql, val)
                    db.commit()
                    await message.channel.send(f"{message.author.name}님은 {mi}를 판매하여 {int(nu) * sell} :euro: 를 얻었습니다!")
            else:
                if str(nu) == "모두":
                    if int(result[t]) == int(0):
                        await message.channel.send(f"{message.author.name}님은 {mi}을 보유하고 있지 않습니다.")
                    else:    
                        sql = (f"UPDATE cm SET coin = ?, {mi} = ? WHERE user_id = ?")
                        val = (int(result[2] + result[t] * sell), int(result[t] - result[t]),message.author.id)
                        cursor.execute(sql, val)
                        db.commit()
                        await message.channel.send(f"{message.author.name}님은 {mi}를 전부 판매하여 {result[t] * sell} :euro: 를 얻었습니다!")

    await client.process_commands(message)
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token, bot=True, reconnect=True)
