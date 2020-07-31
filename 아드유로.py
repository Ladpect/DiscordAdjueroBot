import discord, asyncio, random, datetime
import os, sys, json
from discord.ext import commands
import psycopg2
from discord.ext.commands import CommandError
client = commands.Bot(command_prefix="ad", case_insensitive=True)

db = psycopg2.connect(database="dc9hhd2o22qlo3", 
                        user="midsidwlblizqq",
                        host="ec2-34-200-101-236.compute-1.amazonaws.com",
                        password="e2a6845e3037cee0e984167b94af99951b014222a86e9af0004f7a3722355f20",
                        port="5432")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("ad도움"))
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
    await ctx.send(f"그래. 질문이 `{q}`(이)라고?")
    await asyncio.sleep(1)
    a = await ctx.send("음... :thinking:")
    await asyncio.sleep(3)
    if aa == 1:
        aaa = "그래"
    elif aa == 2:
        aaa = "아니"
    await a.edit(content=aaa)


@client.command(pass_content=True)
async def 삭제(ctx, a):
    try:
        if ctx.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=int(a) + 1)
            await asyncio.sleep(3)
            await ctx.send(f"{a}개의 메세지를 삭제했습니다")
            await asyncio.sleep(2)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send(f"{ctx.author.name}님은 관리자 권한이 없습니다.")
    except CommandError:
        await ctx.send("봇에게 메세지를 삭제할 수 있는 권한이 없거나 메세지를 삭제하지 못한 것 같습니다.")

@client.command()
async def 가입(ctx):
    cursor = db.cursor()
    cursor.execute(f"SELECT 'user_id' FROM 광산 WHERE user_id = {ctx.author.id};")
    result = cursor.fetchone()
    if result is None:
        channel = ctx.channel
        a = discord.Embed(title="가입", color=0x4641D9)
        a.add_field(name="1", value="가입을 하시면 아드봇의 여러 기능을 이용할 수 있습니다.", inline=False)
        a.add_field(name="2", value="유저의 ID와 닉네임이 데이터베이스에 저장됩니다.", inline=False)
        a.add_field(name="3", value="`ad탈퇴`로 탈퇴가 가능합니다.", inline=False)
        await ctx.send(embed=a)
        b = await ctx.send("가입하시겠습니까?")
        await b.add_reaction('⭕')
        await b.add_reaction('❌')
        try: 
            reaction, user = await client.wait_for('reaction_add', timeout = 5, check = lambda reaction, user: user == ctx.author and str(reaction.emoji) in ['⭕', '❌'])
            if str(reaction.emoji) == '⭕':
                sql = (f"insert into 광산(user_id, user_name, coin) values('{ctx.author.id}','{ctx.author.name}','0');")
                cursor.execute(sql)
                sql1 = (f"UPDATE 광산 SET 둘기석 = '0', 삼다석 = '0', 불즈석 = '0', 로아석 = '0', 에릭석 = '0' WHERE user_id = '{ctx.author.id}';")
                cursor.execute(sql1)
                sql2 = (f"UPDATE 광산 SET 염라석 = '0', 템프석 = '0', 태양석 = '0', 사랑석 = '0', 아드석 = '0' WHERE user_id = '{ctx.author.id}';")
                cursor.execute(sql2)
                db.commit()
                await ctx.send(f"{ctx.author.name}님은 가입되었습니다.")
            else:
                await ctx.send("취소되었습니다.")
        except asyncio.TimeoutError:
            await ctx.send("취소되었습니다.")
    else:
        await ctx.send(f"{ctx.author.name}님은 이미 가입되어 있습니다.")

@client.command()
async def 탈퇴(ctx):
    cursor = db.cursor()
    cursor.execute(f"SELECT 'user_id' FROM 광산 WHERE user_id = '{ctx.author.id}';")
    result = cursor.fetchone()
    channel = ctx.channel
    embed = discord.Embed(title="탈퇴", color=0x4641D9)
    embed.add_field(name="1", value="탈퇴하시면 그동안의 기록이 전부 사라지며 아드봇의 일부 기능을 사용하지 못합니다.", inline=False)
    embed.add_field(name="2", value="유저의 ID와 닉네임이 데이터베이스에서 사라집니다", inline=False)
    await ctx.send(embed=embed)
    b = await ctx.send("탈퇴하시겠습니까?")
    await b.add_reaction('⭕')
    await b.add_reaction('❌')
    try: 
        reaction, user = await client.wait_for('reaction_add', timeout = 5, check = lambda reaction, user: user == ctx.author and str(reaction.emoji) in ['⭕', '❌'])
        if str(reaction.emoji) == '⭕':
            if result is None:
                await ctx.send(f"{ctx.author.name}님은 가입하지 않았습니다.")
            else:
                sql = (f"DELETE FROM 광산 WHERE user_id = '{ctx.author.id}';")
                cursor.execute(sql)
                db.commit()
                await ctx.send(f"{ctx.author.name}님은 탈퇴했습니다.")
        else:
            await ctx.send("취소되었습니다.")
    except asyncio.TimeoutError:
        await channel.send("취소되었습니다.")

@client.command()
async def 광산(ctx):
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id, user_name, coin, 둘기석, 삼다석, 불즈석, 로아석, 에릭석, 염라석, 템프석, 태양석, 사랑석, 아드석, 채굴량, 경험치, 레벨 FROM 광산 WHERE user_id = {ctx.author.id};")
    result = cursor.fetchone()
    if result is None:
        await ctx.send("`ad가입`을 통해 가입을 해주세요.")
    else:
        embed = discord.Embed(title=f":pick: {result[1]}님의 창고 :pick:", description="아드광산", color=0x4641D9)
        embed.add_field(name="채굴횟수", value=f"{result[13]}번", inline=False)
        embed.add_field(name="경험치", value=f":test_tube: {result[14]} :test_tube:", inline=True)
        embed.add_field(name=":dove: 둘기석 :dove:", value=f"{result[3]}개", inline=True)
        embed.add_field(name=":droplet: 삼다석 :droplet:", value=f"{result[4]}개", inline=True)
        embed.add_field(name=":water_buffalo:  불즈석 :water_buffalo: ", value=f"{result[5]}개", inline=True)
        embed.add_field(name=":full_moon: 로아석 :full_moon:", value=f"{result[6]}개", inline=True)
        embed.add_field(name=":sparkles: 에릭석 :sparkles: ", value=f"{result[7]}개", inline=True)
        embed.add_field(name=":fire: 염라석 :fire:", value=f"{result[8]}개", inline=True)
        embed.add_field(name=":classical_building: 템프석 :classical_building:", value=f"{result[9]}개", inline=True)
        embed.add_field(name=":sun_with_face: 태양석 :sun_with_face:", value=f"{result[10]}개", inline=True)
        embed.add_field(name=":heart: 사랑석 :heart:", value=f"{result[11]}개", inline=True)
        embed.add_field(name=":boom: 아드석 :boom:", value=f"{result[12]}개", inline=True)
        await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def 채굴(ctx):
    pro = random.randint(1, 100)
    m = "blank"
    num = 0
    men = ctx.author.mention
    #---------------------------------------
    tr = "F"
    ty = random.randint(1, 2)
    ad = random.randint(2, 4)
    money = random.randint(100, 300)
    #---------------------------------------
    exp = random.randint(1, 5)
    #---------------------------------------
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id, user_name, coin, 둘기석, 삼다석, 불즈석, 로아석, 에릭석, 염라석, 템프석, 태양석, 사랑석, 아드석, 채굴량, 경험치, 레벨 FROM 광산 WHERE user_id = '{ctx.author.id}';")
    result = cursor.fetchone()
    if result is None:
        await ctx.send("`ad가입`을 통해 가입을 해주세요.")
    else:
        msg = await ctx.send(f"{men} :pick: 채굴을 시작합니다 :pick:")
        await asyncio.sleep(5)
        if pro >= 1 and pro <= 16:
            m = ":dove: 둘기석 :dove:"
            num = random.randint(5, 17)
            sql = (f"UPDATE 광산 SET 둘기석 = {int(result[3]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro >= 17 and pro <= 28:
            m = ":droplet: 삼다석 :droplet:"
            num = random.randint(4, 12)
            sql = (f"UPDATE 광산 SET 삼다석 = {int(result[4]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro >= 29 and pro <= 39:
            m = ":water_buffalo:  불즈석 :water_buffalo: "
            num = random.randint(3, 9)
            sql = (f"UPDATE 광산 SET 불즈석 = {int(result[5]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro >= 40 and pro <= 49:
            m = ":full_moon: 로아석 :full_moon:"
            num = random.randint(2, 6)
            sql = (f"UPDATE 광산 SET 로아석 = {int(result[6]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro >= 50 and pro <= 58:
            m = ":sparkles: 에릭석 :sparkles:"
            num = random.randint(3, 6)
            sql = (f"UPDATE 광산 SET 에릭석 = {int(result[7]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro >= 59 and pro <= 65:
            m = ":fire: 염라석 :fire:"
            num = random.randint(2, 5)
            sql = (f"UPDATE 광산 SET 염라석 = {int(result[8]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro >= 66 and pro <= 72:
            m = ":classical_building: 템프석 :classical_building:"
            num = random.randint(2, 8)
            sql = (f"UPDATE 광산 SET 템프석 = {int(result[9]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro >= 73 and pro <= 78:
            m = ":sun_with_face: 태양석 :sun_with_face:"
            num = random.randint(2, 6)
            sql = (f"UPDATE 광산 SET 태양석 = {int(result[10]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro >= 79 and pro <= 82:
            m = ":heart: 사랑석 :heart:"
            num = random.randint(2, 6)
            sql = (f"UPDATE 광산 SET 사랑석 = {int(result[11]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro == 83:
            m = ":boom: 아드석 :boom:"
            num = random.randint(1, 2)
            sql = (f"UPDATE 광산 SET 아드석 = {int(result[12]) + int(num)} WHERE user_id = {ctx.author.id};")
            cursor.execute(sql)
            db.commit()
        elif pro == 84:
            tr == "T"
            if ty == 1:
                sql = (f"UPDATE 광산 SET 아드석 = {int(result[12]) + int(ad)} WHERE user_id = {ctx.author.id};")
                cursor.execute(sql)
                db.commit()
            else:
                sql = (f"UPDATE 광산 SET coin = {result[2] + money} WHERE user_id = {ctx.author.id};")
                cursor.execute(sql)
                db.commit()
        elif pro >= 85:
            tr = "N"
        if tr == "F":
            await msg.edit(content=f"{men} {m}을 {str(num)}개 얻었다!")
        elif tr == "N":
            await msg.edit(content=f"{men} 아무 가치도 없는 돌이다...")
        elif tr == "T":
            if ty == 1:
                await msg.edit(content=f"{men} 어라? :gift: 보물상자다! :gift: 열어보니 :boom: 아드석 :boom: {ad}개가 들어있었다!")
            elif ty == 2:
                await msg.edit(content=f"{men} 어라? :gift: 보물상자다! :gift: 열어보니 {money} :euro:가 있었다!")
        sql = (f"UPDATE 광산 SET 채굴량 = {int(result[13]) + int(1)}, 경험치 = {int(result[14]) + int(exp)} WHERE user_id = {ctx.author.id};")
        cursor.execute(sql)
        await ctx.send(f"{men} :test_tube: 경험치 :test_tube: 가 {exp}만큼 올랐다!")

@client.command()
async def 지갑(ctx):
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id, user_name, coin FROM 광산 WHERE user_id = '{ctx.author.id}';")
    result = cursor.fetchone()
    if result is None:
        await ctx.channel.send("`ad가입`을 통해 가입을 해주세요.")
    else:
        coin = str(result[2])
        embed = discord.Embed(title=f"{result[1]}님의 :euro: 지갑 :euro:", color=0x4641D9)
        embed.add_field(name="아드코인", value=coin + " :euro:", inline=True)
        await ctx.channel.send(embed=embed)

@client.command(pass_content=True)
async def 닉네임(ctx):
    name = ctx.message.content[6:]
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id, user_name FROM 광산 WHERE user_id = '{ctx.author.id}';")
    result = cursor.fetchone()
    if result is None:
        await ctx.send("`ad가입`을 통해 가입을 해주세요.")
    if name is None:
        await ctx.send("바꿀 닉네임을 입력해주세요.")
    else:
        sql = (f"UPDATE 광산 SET user_name = '{name}' WHERE user_id = {ctx.author.id};")
        cursor.execute(sql)
        await ctx.send("닉네임이 변경되었습니다")
        
@client.command(pass_content=True)
async def 판매(ctx, mi, nu):
    try:
        sell = 0
        t = 0
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id, user_name, coin, 둘기석, 삼다석, 불즈석, 로아석, 에릭석, 염라석, 템프석, 태양석, 사랑석, 아드석 FROM 광산 WHERE user_id = {ctx.author.id};")
        result = cursor.fetchone()
        if result is None:
            await ctx.send("`ad가입`을 통해 가입을 해주세요.")
        else:
            if mi == "둘기석":
                sell = 3
                t = 3
            elif mi == "삼다석":
                sell = 5
                t = 4
            elif mi == "불즈석":
                sell = 10
                t = 5
            elif mi == "로아석":
                sell = 15
                t = 6
            elif mi == "에릭석":
                sell = 15
                t = 7
            elif mi == "염라석":
                sell = 20
                t = 8
            elif mi == "템프석":
                sell = 30
                t = 9
            elif mi == "태양석":
                sell = 40
                t = 10
            elif mi == "사랑석":
                sell = 60
                t = 11
            elif mi == "아드석":
                sell = 150
                t = 12
            try:
                nu = int(nu)
                if int(result[t]) < int(nu):
                    await ctx.send(f"{result[1]}님의 {mi}는 {result[t]}개입니다.")
                else:
                    sql = (f"UPDATE 광산 SET coin = {int(result[2] + int(nu) * sell)}, {mi} = {int(result[t] - int(nu))} WHERE user_id = {ctx.author.id};")
                    cursor.execute(sql)
                    db.commit()
                    await ctx.send(f"{result[1]}님은 {mi}를 판매하여 {int(nu) * sell} :euro: 를 얻었습니다!")
            except ValueError:
                if str(nu) == "모두":
                    if int(result[t]) == int(0):
                        await ctx.send(f"{result[1]}님은 {mi}을 보유하고 있지 않습니다.")
                    else:    
                        sql = (f"UPDATE 광산 SET coin = {int(result[2] + result[t] * sell)}, {mi} = 0 WHERE user_id = {ctx.author.id};")
                        cursor.execute(sql)
                        db.commit()
                        await ctx.send(f"{result[1]}님은 {mi}를 전부 판매하여 {result[t] * sell} :euro: 를 얻었습니다!")
    except Exception:
        await ctx.send(":no_entry_sign: 명령어가 잘못되었습니다! :no_entry_sign:")
        db.rollback()
                       
@client.command(pass_content=True)
async def 더블(ctx, bet):
    try:
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id, user_name, coin FROM 광산 WHERE user_id = '{ctx.author.id}'")
        result = cursor.fetchone()
        if result is None:
            await ctx.channel.send("`ad가입`을 통해 가입을 해주세요.")
        if bet is None:
            await ctx.send("베팅금액을 정해주세요.")
        else:
            embed = discord.Embed(title="double or nothing", description="묻고 더블로 가!", color=0x4641D9)
            embed.add_field(name="설명", value="절반의 확률로 두배를 얻거나 전부 잃습니다.", inline=False)
            embed.add_field(name="배팅금액", value=f"{bet} :euro:", inline=False)
            await ctx.send(embed=embed)
            b = await ctx.send("하시겠습니까?")
            await b.add_reaction('⭕')
            await b.add_reaction('❌')
            try: 
                reaction, user = await client.wait_for('reaction_add', timeout = 5, check = lambda reaction, user: user == ctx.author and str(reaction.emoji) in ['⭕', '❌'])
                if str(reaction.emoji) == '⭕':
                    pro = random.randint(1, 2)
                    if pro == 1:
                        sql = (f"UPDATE 광산 SET coin = {result[2] - int(bet)} WHERE user_id = {ctx.author.id};")
                        cursor.execute(sql)
                        db.commit()
                        await ctx.send(f"이런... {bet} :euro: 를 잃었다...")
                    else:
                        sql = (f"UPDATE 광산 SET coin = {result[2] + int(bet)} WHERE user_id = {ctx.author.id};")
                        cursor.execute(sql)
                        db.commit()
                        await ctx.send(f":tada: 와! {bet} :euro: 를 얻었다! :tada:")
                else:
                    await ctx.send("취소되었습니다.")
            except asyncio.TimeoutError:
                await ctx.send("취소되었습니다.")
    except Exception:
        await ctx.send(":no_entry_sign: 명령어가 잘못되었습니다! :no_entry_sign:")
        db.rollback()    
    
@client.command(pass_content=True)
async def 안녕(ctx):
    await ctx.send("ㅎㅇ")
        
        
@client.command()
async def 도움(ctx):
    embed = discord.Embed(title="아드유로 봇 명령어들", description="이용법은 ad(명령어)야. 적다고? 곧 추가할거야 아드유로가 일을 해야할텐데...", color=0x4641D9)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
    embed.add_field(name="관리", value="`ad삭제 {삭제량}`", inline=False)
    embed.add_field(name="대화", value="`ad대화`에서 확인하세요", inline=False)
    embed.add_field(name="이미지", value="`ad이미지`에서 확인하세요", inline=False)
    embed.add_field(name="기타", value="`ad거꾸로 {할말}`, `ad질문 {질문}`(O 또는 X만 가능)", inline=False)
    embed.add_field(name="게임", value="`ad룰렛`, `ad주사위 {최대 숫자}`, `ad타이머`", inline=False)
    embed.add_field(name=":euro:", value="`ad유로`", inline=False)
    await ctx.send("아드봇의 커맨드들", embed=embed)
    embed2 = discord.Embed(title="기타", description="URL", color=0x4641D9)
    embed2.add_field(name="아드봇 초대", value="[초대](https://discord.com/api/oauth2/authorize?client_id=685806440224653341&permissions=8&scope=bot)", inline=False)
    embed2.add_field(name="공식 아드서버", value="[아드서버](https://discord.gg/6WH2cgU)", inline=False)
    embed2.add_field(name="만든 환자", value="adjuero#5331", inline=False)
    await ctx.send(embed=embed2)
        
@client.command()
async def 유로(ctx):
    embed3 = discord.Embed(title=":pick: 아드광산 :pick:", color=0x4641D9)
    embed3.add_field(name="`ad가입`", value="가입합니다.", inline=False)
    embed3.add_field(name="`ad탈퇴`", value="탈퇴합니다.", inline=False)
    embed3.add_field(name="`ad지갑`", value="아드코인 소유량을 확인합니다.", inline=False)
    embed3.add_field(name="`ad광산`", value="광물 수를 확인합니다", inline=False)
    embed3.add_field(name="`ad채굴`", value="채굴합니다. 5초 쿨타임이 있습니다", inline=False)
    embed3.add_field(name="`ad닉네임 {변경할 닉네임}`", value="닉네임을 변경합니다.", inline=False)
    embed3.add_field(name="`ad판매 {광물} {갯수(모두)}`", value="광물을 판매해 아드코인을 획득합니다.", inline=False)
    embed3.add_field(name="`ad더블 {배팅금액}`", value="절반의 확률로 두배를 얻거나 잃습니다.", inline=False)
    await ctx.send(embed=embed3)
        
@client.command()
async def 대화(ctx):
    embed = discord.Embed(title="대화명령어들!", description="말해라 아듀로 봇", color=0x4641D9)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
    embed.add_field(name="대화명령어", value="`ad안녕`, `ad따라해 {할말}`, `ad주사위 {숫자}`, `ad잘했어`, `ad레니`", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def 이미지(ctx):
    embed = discord.Embed(title="이미지명령어들", description="이미지 노예 아듀로 봇", color=0x4641D9)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
    embed.add_field(name="이미지", value="`ad김두한`, `ad물리치료사`, `ad심영`, `ad김치싸대기`, `ad김치수거`, `ad탈주`, `ad포나춤`, `ad샌즈`, `ad시공`", inline=False)
    await ctx.send(embed=embed)
    
@client.command()
async def 레니(ctx):
    Lenny = ["( ͡° ͜ʖ ͡°)", "( ͠° ͟ʖ ͡°)", "( ͡~ ͜ʖ ͡°)", "( ͡ʘ ͜ʖ ͡ʘ)", "( ͡o ͜ʖ ͡o)", "(° ͜ʖ °)", "( ‾ʖ̫‾)", 
    "( ಠ ͜ʖಠ)", "( ͡° ʖ̯ ͡°)", "( ͡ಥ ͜ʖ ͡ಥ)", "༼  ͡° ͜ʖ ͡° ༽", "(▀̿Ĺ̯▀̿ ̿)", "( ✧≖ ͜ʖ≖)", "(ง ͠° ͟ل͜ ͡°)ง", 
    "(͡ ͡° ͜ つ ͡͡°)", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "(✿❦ ͜ʖ ❦)", "ᕦ( ͡° ͜ʖ ͡°)ᕤ", "( ͡° ͜ʖ ͡°)╭∩╮", 
    "(╯ ͠° ͟ʖ ͡°)╯┻━┻", "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)", "ಠ_ಠ"]
    r = random.randrange(0, len(Lenny))
    print("랜덤수 값 :" + str(r))
    print(Lenny[r])
    await ctx.send(embed=discord.Embed(description=Lenny[r]))
    
@client.command()
async def 김두한(ctx):
    embed = discord.Embed(title="김두한.", description="**1972**", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685873878723067915/1541313521858.jpg")
    embed.set_footer(text="다함께 폭사하자.")
    await ctx.send(embed=embed)
    
@client.command()
async def 물리치료사(ctx):
    embed = discord.Embed(title="마사지사양반.", description="자자 이리로 왓", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874384295952427/1518347904432.gif")
    embed.set_footer(text="그래도 의사니까 안심하자.")
    await ctx.send(embed=embed)
    
@client.command()
async def 심영(ctx):
    embed = discord.Embed(title="심영이.", description="국민 고자", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874314138222640/JPEG_20180922_092147.jpg")
    embed.set_footer(text="폭8이다!.")
    await ctx.send(embed=embed)
    
@client.command()
async def 김치수거(ctx):
    embed = discord.Embed(title="김치수거중", description="내 아까운 김치", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311211783356426/a8300e3efe453a83.gif")
    embed.set_footer(text="김치를 아끼자.")
    await ctx.send(embed=embed)
    
@client.command()
async def 김치싸대기(ctx):
    embed = discord.Embed(title="예끼 이놈", description="김치워리어", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311226354237477/068b27a2f06240e8.gif")
    embed.set_footer(text="김치워리어 운다")
    await ctx.send(embed=embed)
    
@client.command()
async def 탈주(ctx):
    embed = discord.Embed(title="모두 다음에 만나요", description="GONE", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311120640999425/1583662278990.gif")
    embed.set_footer(text="잘가")
    await ctx.send(embed=embed)
    
@client.command()
async def 시공(ctx):
    embed = discord.Embed(title="시공의 폭풍은 정말 최고야!", description="히오스", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311711677415424/1535025935602.gif")
    embed.set_footer(text="히오스는 최고가 맞습니다. 맞다고요")
    await ctx.send(embed=embed)
        
@client.command()
async def 포나춤(ctx):
    embed = discord.Embed(title="F.O.R.T.N.I.T.E", description="D.E.F.A.U.L.T D.A.N.C.E", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/689719145855844382/1328177857dfa41ab6bb71bf3166f42e.gif")
    embed.set_footer(text="WOW")
    await ctx.send(embed=embed)

@client.command()
async def 샌즈(ctx):
    embed = discord.Embed(title="WA! SANS!", description="참고로 이거 겁.나.어.렵.습.니.다", color=0x4641D9)
    embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/689720396345638941/1537569816_hqx7okmi64c11.gif")
    embed.set_footer(text="(SANS LAUGH)")
    await ctx.send(embed=embed)
    
@client.command(pass_content=True)
async def 주사위(ctx, *, num):
    op = random.randint(0, int(num))
    await ctx.send(op)
    
@client.command(pass_content=True)
async def 타이머(ctx, time): 
        p = ctx.author.mention
        t = await ctx.send(time)
        await asyncio.sleep(1)
        for sec in range(1, int(time)):
            time = int(time) - 1
            await t.edit(content=str(int(time)))
            await asyncio.sleep(1)
        else:
            await ctx.send(p + " " + str(int(sec) + 1) + "초가 지났습니다!")

            
@client.command(pass_content=True)
async def 거꾸로(ctx):
    say = ctx.message.content[5:]
    await ctx.send(say[::-1])
    
        
        
@client.command(pass_content=True)
async def 룰렛(ctx):
    mention = ctx.author.mention
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
        await ctx.channel.send(ctx.author.mention + " :tada: 축하드립니다! :tada:")
    elif num1 == num2 or num2 == num3 or num1 == num3:
        embed.add_field(name="result", value="OOOF", inline=False)
    else:
        embed.add_field(name="result", value="YEAHHHHHH", inline=False)
    await ctx.channel.send(embed=embed)
    await ctx.channel.send(mention)
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token, bot=True, reconnect=True)
