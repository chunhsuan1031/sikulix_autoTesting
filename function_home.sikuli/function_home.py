from sikuli import *
import function_common

### home ###
# home_vip
def home_vip():
    function_common.declineInvitation()
    function_common.waitPush()
    if exists(Pattern("1663034424571-1.png").similar(0.93)):
        click("1663034424571-1.png")
        if exists("1663037588743.png"and"1663038429067.png",60):
            click("1663038465279.png")
            sleep(1)
            print("home vip pass")
            assert True
        else:
            print("home vip error")
            assert False            
    elif exists(Pattern("1663034459797-1.png").similar(0.90)):
        click("1663034459797-1.png")
        if exists("1663037588743.png"and"1663038429067.png",60):
            click("1663038465279.png")
            sleep(1)
            print("home vip pass")
            assert True
        else:
            print("home vip error")
            assert False            
    elif exists(Pattern("1663034506308-1.png").similar(0.90)):
        click("1663034506308-1.png")
        if exists("1663037588743.png"and"1663038429067.png",60):
            click("1663038465279.png")
            sleep(1)
            print("home vip pass")
            assert True
        else:
            print("home vip error")
            assert False
    elif exists(Pattern("1663034518435-1.png").similar(0.90)):
        click("1663034518435-1.png")
        if exists("1663037588743.png"and"1663038429067.png",60):
            click("1663038465279.png")
            sleep(1)
            print("home vip pass")
            assert True
        else:
            print("home vip error")
            assert False    
    else:
        print("can't find home vip")
        assert False

# home_integral
def home_integral():
    function_common.declineInvitation()
    if exists(Pattern("1663040259945.png").similar(0.90),60):
        click("1663040259945.png")
        if exists(Pattern("1663040411568.png").similar(0.90),60):
            sleep(1)
            click("1663051333609.png")
            sleep(1)
            print("home integral pass")
            assert True            
        elif exists(Pattern("1663061826458.png").similar(0.90),60):
            sleep(1)
            click("1663051333609.png")
            sleep(1)
            print("home integral pass")
            assert True
        else:
            print("home integral error")
            assert False            
    else:
        print("can't find home integral")
        assert False       

# home_daimond
def home_daimond():
    function_common.declineInvitation()
    if exists(Pattern("1663051507028.png").similar(0.90),60):
        click("1663051507028.png")
        if exists(Pattern("1663051537287.png").similar(0.90),60):
            click("1663051333609.png")
            sleep(1)
            print("home daimond pass")
            assert True
        else:
            print("home daimond error")
            assert False            
    else:
        print("can't find home daimond")
        assert False      

# home_coin
def home_coin():
    function_common.declineInvitation()
    if exists(Pattern("1663051585116.png").similar(0.90),60):
        click("1663051585116.png")
        if exists(Pattern("1663051610177.png").similar(0.90),60):
            click("1663051333609.png")
            sleep(1)
            print("home coin pass")
            assert True
        else:
            print("home coin error")
            assert False            
    else:
        print("can't find home coin")
        assert False

# home_announcement
def home_announcement():
    if exists(Pattern("1663052363780.png").similar(0.90),60):
        click("1663052363780.png")
        if exists(Pattern("1663213049369.png").similar(0.90),60):
            click("1663052395388.png")
            sleep(1)
            print("home announcement pass")
            assert True
        else:
            print("home announcement error")
            assert False            
    else:
        print("can't find home announcement")
        assert False

# home_task
def home_task():
    if exists(Pattern("1663052455442.png").similar(0.90),60):
        click("1663052455442.png")
        if exists(Pattern("1663052623508.png").similar(0.90),60):
            click("1663052640538.png")
            print("home task pass")
            assert True
        else:
            print("home task error")
            assert False 
    elif exists(Pattern("1663052479467.png").similar(0.90),60):
        click("1663052479467.png")
        if exists(Pattern("1663052623508.png").similar(0.90),60):
            click("1663052640538.png")
            print("home task pass")
            assert True
        else:
            print("home task error")
            assert False
    elif exists(Pattern("1663052501771.png").similar(0.90),60):
        click("1663052501771.png")
        if exists(Pattern("1663052623508.png").similar(0.90),60):
            click("1663052640538.png")
            print("home task pass")
            assert True
        else:
            print("home task error")
            assert False       
    else:
        print("can't find home task")
        assert False

# home_mail
def home_mail():
    if exists(Pattern("1663053057166.png").similar(0.90),60):
        click("1663053057166.png")
        if exists(Pattern("1663053071208.png").similar(0.90)and"1663053085165.png",60):
            click("1663052395388.png")
            sleep(1)
            print("home mail pass")
            assert True
        else:
            print("home mail error")
            assert False            
    else:
        print("can't find home mail")
        assert False

# home_createClub
def home_createClub():
    if exists(Pattern("1663052187201.png").similar(0.90),60):
        click("1663052187201.png")
        if exists("1663052207189.png",60):
            print("home create club pass")
            assert True
        else:
            print("home create club error")
            assert False            
    else:
        print("can't find create club")
        assert False

# home_findClub
def home_findClub():
    if exists(Pattern("1663053152581.png").similar(0.90),60):
        click("1663053152581.png")
        if exists(Pattern("1663053169109.png").similar(0.90),60):
            click("1663052395388.png")
            print("home find club pass")
            assert True
        else:
            print("home find club error")
            assert False            
    else:
        print("can't find find club")
        assert False

# home_club
def home_club():
    if exists(Pattern("1663210438783.png").similar(0.90),60):
        click(Pattern("1663210438783.png").similar(0.90))
        function_common.declineInvitation()
        if exists(Pattern("1663209991655.png").similar(0.90),60):
            click("1663053346296.png")
            print("home club pass")
            assert True
        elif exists(Pattern("1663121261042.png").similar(0.90),60):
            click("1663121294039.png")
            sleep(1)
            click("1663121294039.png")
            sleep(1)
            assert exists(Pattern("1663209991655.png").similar(0.90))
            click("1663053346296.png")
            print("home club pass")
            assert True
        elif exists(Pattern("1663121342586.png").similar(0.90),60):
            click("1663121294039.png")
            sleep(1)
            assert exists(Pattern("1663209991655.png").similar(0.90))
            click("1663053346296.png")
            print("home club pass")
            assert True
        else:
            print("home club error")
            assert False            
    else:
        print("can't find club")
        assert False

# home_lobby
def home_lobby():
    if exists(Pattern("1663053686237.png").similar(0.90),60):
        click("1663053686237.png")
        function_common.declineInvitation()
        if exists("1663053731270.png"and(Pattern("1663054240428.png").similar(0.90)),60):
            click("1663053346296.png")
            print("home lobby pass")
            assert True
        elif exists("1663121576850.png",60):
            click("1663121576850.png")
            sleep(1)
            assert exists("1663053731270.png"and(Pattern("1663054240428.png").similar(0.90)),60)
            click("1663053346296.png")
            print("home lobby pass")
            assert True
            
        else:
            print("home lobby error")
            assert False            
    else:
        print("can't find lobby")
        assert False

# home_globalTournament
def home_globalTournament():
    if exists(Pattern("1663054020317.png").similar(0.90),60):
        click("1663054020317.png")
        #function_common.declineInvitation()
        if exists("1663054039133.png"and(Pattern("1663054222636.png").similar(0.90)),60):
            click("1663053346296.png")
            print("home global tournament pass")
            assert True
        else:
            print("home global tournament error")
            assert False            
    else:
        print("can't find global tournament")
        assert False

# home_spinUp
def home_spinUp():
    if exists(Pattern("1663054133110.png").similar(0.90),60):
        click("1663054133110.png")
        #function_common.declineInvitation()
        if exists("1663054160749.png"and(Pattern("1663054208349.png").similar(0.90)),60):
            click("1663053346296.png")
            print("home spin up pass")
            assert True
        else:
            print("home spin up error")
            assert False            
    else:
        print("can't find spin up")
        assert False


















