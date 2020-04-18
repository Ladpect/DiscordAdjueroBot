import discord, asyncio, random, datetime
import os
import urllib, bs4, request
import mysql.connector
from bs4 import BeautifulSoup

client = discord.Client() #긴거 대신함
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="oneshaman0708*", 
    database="adjuero", 
    charset="utf8", 
    auth_plugin="mysql_native_password"
    )

def generateXP():
    return random.randint(1, 100)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("ad도움 하면 도와드림"))
    print("준비 되었다")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot: #채팅친 놈이 봇이면 구문 종료
        return None

    if message.content in ["아듀로 안녕", "ad안녕"]:
        await message.channel.send("안녕")
        #channel을 author로 바꾸면 DM으로 감

    if message.content in ["아듀로 정체", "ad정체"]:
        await message.channel.send("우주에서 온 이상한 사람")
                           
    if message.content in ["아듀로 고마워", "ad고마워"]:
        await message.channel.send("당신의 칭찬에 찬사를!")
        
    if message.content in ["아듀로 도움", "ad도움", "adhelp"]:
        embed = discord.Embed(title="아드유로 봇 명령어들", description="이용법은 '아듀로 (명령어)' 또는 ad(명령어)야. 적다고? 곧 추가할거야 아드유로가 일을 해야할텐데...", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="대화", value="`ad고마워`, `ad정체`, `ad안녕`, `ad따라해 {할말}` 등등... `ad대도`에서 확인하세요", inline=False)
        embed.add_field(name="이미지", value="`ad김두한`, `ad물리치료사`, `ad심영` 등등...`ad이도`에서 확인하세요", inline=False)
        embed.add_field(name="기타", value="`adDM {유저ID} {할말}`, `ad거꾸로 {할말}`", inline=False)
        embed.add_field(name="각종 공식", value="`ad에너지 {질량값}`, `ad제곱 {숫자}`, `ad루트 {숫자} {나눌 제곱 숫자}`", inline=False)
        embed.add_field(name="게임", value="`ad룰렛`", inline=False)
        embed.add_field(name="밀크초코 온라인", value="`ad밀초 도움`", inline=False)
        embed.set_footer(text="자주 봐두면 좋아!")
        await message.channel.send("도움이 필요하신가요?", embed=embed)
        
    if message.content in ["ad대화 도움", "ad대도"]:
        embed = discord.Embed(title="대화명령어들!", description="말해라 아듀로 봇", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="대화명령어", value="`ad고마워`, `ad정체`, `ad안녕`, `ad따라해 {할말}`, `ad주사위 {숫자}`, `ad잘했어`, `ad나 어때?`, `ad레니`", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content in ["ad이미지 도움", "ad이도"]:
        embed = discord.Embed(title="이미지명령어들", description="이미지 노예 아듀로 봇", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="이미지", value="`ad김두한`, `ad물리치료사`, `ad심영`, `ad햄스터`, `ad프로필`, `ad둘기이마트`, `ad김치싸대기`, `ad김치수거`, `ad비프로스트`, `ad이건 좀`, `ad변신`, `adㅌㅌ`, `ad박수`, `ad충격`, `ad처형`, `ad토마스`, `ad포나춤`, `ad샌즈`", inline=False)
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

    if message.content in ["아듀로 햄스터", "ad햄스터"]:
        embed = discord.Embed(title="햄스터?", description="정체불명", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874094411087988/hamster.jpg")
        embed.set_footer(text="나는 그냥 햄스터다 인간들아")
        await message.channel.send("아듀로 이미지", embed=embed)
        
    if message.content in ["아듀로 둘기이마트", "ad둘기이마트"]:
        embed = discord.Embed(title="둘기는 이마트를 좋아해", description="난나난나나나나", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/686185101700104215/KakaoTalk_20200308_200354653.jpg")
        embed.set_footer(text="이마트는 둘기를 싫어합니다")
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

    if message.content in ["아듀로 이건 좀", "ad이건 좀"]:
        embed = discord.Embed(title="김동지", description="이건 좀...", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311196884926464/036320e13456ba4a.gif")
        embed.set_footer(text="쓰읍")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 비프로스트", "ad비프로스트"]:
        embed = discord.Embed(title="휴대용입니다.", description="접속이다", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311195068923942/8695d6e35b46b6df.gif")
        embed.set_footer(text="시공의 폭ㅍ...")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 변신", "ad변신"]:
        embed = discord.Embed(title="짜잔!", description="난 이제 달라.", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311202497298436/9d89fa7a4cb65379.gif")
        embed.set_footer(text="양자중첩상태.")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 ㅌㅌ", "adㅌㅌ"]:
        embed = discord.Embed(title="모두 다음에 만나요", description="사라짐", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311120640999425/1583662278990.gif")
        embed.set_footer(text="잘가")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 던져", "ad던져"]:
        embed = discord.Embed(title="throw away", description="던질까 말까", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311118967734285/1583592857865.gif")
        embed.set_footer(text="찌리찌리 짜라짜라")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 박수", "ad박수"]:
        embed = discord.Embed(title="짝짝짝", description="와아아아아아아아", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311243890622464/f2e28e1276d65f5f.gif")
        embed.set_footer(text="이 다음 장면은 누가 나올까요?")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 충격", "ad충격"]:
        embed = discord.Embed(title="주르륵", description="뭐라고?", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311242573742167/b5562f1645977f2a.gif")
        embed.set_footer(text="오렌지 쥬스 아깝다")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 처형", "ad처형"]:
        embed = discord.Embed(title="석양이 진다", description="탕탕탕", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311714239873026/1544234146072.gif")
        embed.set_footer(text="무한 총알인거임ㅋㅋㅋㅋ")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 시공", "ad시공"]:
        embed = discord.Embed(title="시공의 폭풍은 정말 최고야!", description="히오스", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/688311711677415424/1535025935602.gif")
        embed.set_footer(text="히오스는 최고가 맞습니다. 맞다고요")
        await message.channel.send("아듀로 이미지", embed=embed)

    if message.content in ["아듀로 토마스", "ad토마스"]:
        embed = discord.Embed(title="돌진조아", description="돌진의 대가", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/689005281400848421/KakaoTalk_20200316_130958972.jpg")
        embed.set_footer(text="빠밤빠빠-빠빠빰 빠밤빠빰-빠라빰-빠빠라-빠라빠라빠라")
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
        
    if message.content in ["ad고양이", "아듀로 고양이"]:
        await message.channel.send("현재 이 명령어를 사용할 수 없습니다. 이상한 사진이 나오던 문제를 해결할 시 다시 재가동 시킬 예정입니다.")
        #embed = discord.Embed(
            #title="야옹",
            #description="냥냥파는 승리한다",
            #color=0x4641D9
        #)

        #urlBase = 'https://loremflickr.com/320/240?lock='
        #randomN = random.randrange(1, 30977)
        #urlF = urlBase + str(randomN)
        #embed.set_image(url = urlF)
        #await message.channel.send(embed=embed)

    if message.content in ["아듀로 강아지", "ad강아지"]:
        await message.channel.send("현재 이 명령어를 사용할 수 없습니다. 이상한 사진이 나오던 문제를 해결할 시 다시 재가동 시킬 예정입니다.")
        #embed = discord.Embed(
            #title="멍멍",
            #description="뭉멍파는 승리한다",
            #color=0x4641D9
        #)

        #urlBase = 'https://loremflickr.com/320/240/dog?lock='
        #randomN = random.randrange(1, 30977)
        #urlF = urlBase + str(randomN)
        #embed.set_image(url = urlF)
        #await message.channel.send(embed=embed)
        
    if message.content.startswith("ad채널확성기"):
        channel = message.content[8:27] #채널 아이디는 18자, ?번째 글자와 ?번째 글자 사이에 그거 
        msg = message.content[27:] #할말 보내는거
        await client.get_channel(int(channel)).send(msg) #채널 그게 정수값으로 해서 그채널 보내게 함
        
    if message.content.startswith("adDM"):
        author = message.guild.get_member(int(message.content[5:24])) #유저 아이디
        msg = message.content[24:] #유저에게 할말
        await author.send(msg)
        
    #if message.content.startswith("아듀로 뮤트죄수임명"):
        #author = message.guild.get_member(int(message.content[11:30])) #유저 아이디
        #role = discord.utils.get(message.guild.roles, name="죄수") #죄수 임명 변수
        #await author.add_roles(role)#죄수 임명

    #if message.content.startswith("아듀로 뮤트죄수해제"):
        #author = message.guild.get_member(int(message.content[11:30])) #유저 아이디
        #role = discord.utils.get(message.guild.roles, name="죄수") #죄수 변수 찾아라
        #await author.remove_roles(role)#죄수 해제
        
    if message.content.startswith("ad따라해"):
        msg = message.content[6:] #할말 보내는거
        await message.channel.send(msg) #할말 보내는거
        
    if message.content.startswith("ad주사위"):
        num = message.content[6:]
        op = random.randint(0, int(num))
        await message.channel.send(op)
                           
    if message.content.startswith("@everyone"):
        await message.channel.send("그런건 진짜 가끔만 쓰자 친구야")

    
    #if message.content == "아듀로 시간":
        #a = datetime.datetime.today().year
        #b = datetime.datetime.today().month
        #c = datetime.datetime.today().day
        #d = datetime.datetime.today().hour
        #e = datetime.datetime.today().minute
        #await message.channel.send("지금의 시간은 " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 입니다")

    if message.content == "ad밀초 도움":
        embed = discord.Embed(title="아듀로 봇의 밀초 정보 저장소", description="영웅들과 총 정보 등등 많은 정보를 제공합니다", color=0x4641D9)
        embed.add_field(name="캐릭터", value="`ad어썰트`, `ad메딕`, `ad바머`, `ad리콘`, `ad고스트`, `ad쉴드`, `ad런쳐`, `ad인비`, `ad후크`, `ad미오캣`, `ad데페`, `ad아이언`, `ad캐로그`, `ad크리미`, `ad휠레그`, `ad에어`, `ad일렉트릭`, `ad블레이드`, `ad스위니`, `ad마고`", inline=False)
        embed.add_field(name="총기", value="(유저들이 주로 쓰는 총으로 추가 예정)", inline=False)
        embed.add_field(name="유의사항 1", value="1.정보가 맞지 않을 수 있습니다.", inline=False)
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
        embed.add_field(name="원뚝여부", value="에땁 이상의 ", inline=True)
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
        
    if message.content.startswith("ad룰렛"):
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
        embed = discord.Embed(title=":star:이것은 룰렛이여:star:", description=":thinking:", color=0x4641D9)
        embed.add_field(name="1", value=emo1, inline=True)
        embed.add_field(name="2", value=emo2, inline=True)
        embed.add_field(name="3", value=emo3, inline=True)
        if num1 == num2 == num3:
            embed.add_field(name="result", value="이거 아주 :star:럭키:star:하군", inline=False)
            role = discord.utils.get(message.guild.roles, name="잭팟 자")
            await author.add_roles(role)
        elif num1 == num2 or num2 == num3 or num1 == num3:
            embed.add_field(name="result", value="이거 꽤나 아쉽군:thinking:", inline=False)
        else:
            embed.add_field(name="result", value="영 좋지 않아요!", inline=False)
        await message.channel.send(embed=embed)
            
    if message.content.startswith("ad거꾸로"):
        say = message.content[6:]
        embed = discord.Embed(title="로꾸거", description="로대반 은상세 이", color=0x4641D9)
        embed.add_field(name="결과", value=":arrows_counterclockwise: " + " " + str(say[::-1]), inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == "ad프로필":
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        cursor = mydb.cursor()
        cursor.execute("SELECT user_xp FROM users where client_id = " + str(message.author.id))
        result = cursor.fetchall()
        xp = generateXP()
        tXP = result[0][0] + xp
        embed = discord.Embed(color=0x4641D9)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉넴", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="대화 경험치", value=tXP, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
    #야 아드유로, 이제 시작이야. 이거 성공하면 존나 쩌는거 완성된다고. 알겄제?
    if message.content.startswith("ad"):
        pass
    else:
        xp = generateXP()
        cursor = mydb.cursor()
        cursor.execute("SELECT user_xp FROM users where client_id = " + str(message.author.id))
        result = cursor.fetchall()
        if len(result) == 0:
            await message.channel.send("등록되지 않은 유저입니다.")
            cursor.execute("insert into users VALUES(" + str(message.author.id) + "," + str(xp) + ")")
            mydb.commit()
            await message.channel.send("자동으로 등록되었습니다")
        else:
            currentXP = result[0][0] + xp
            print(currentXP)
            cursor.execute("UPDATE users SET user_xp = " + str(currentXP) + " WHERE client_id = " + str(message.author.id))
            mydb.commit()
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
