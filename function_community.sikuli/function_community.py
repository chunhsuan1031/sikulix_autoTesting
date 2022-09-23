from sikuli import *

### community ###
# community_featured
def featured():
    if exists((Pattern("1662456010859.png").similar(0.90))and"1663138508792.png",60):
        print("featured pass")
        sleep(1) 
        assert True
    else:
        print("featured error")
        assert False

# community_notice
def notice():
    click("1662456546765.png")
    if exists(Pattern("1662456754978.png").similar(0.90),60):
        print("notice like pass")
        sleep(2)
        click(Pattern("1662456770345.png").similar(0.90))
        sleep(2)
        assert exists(Pattern("1662456794403.png").similar(0.90))
        print("notice comment pass")
        sleep(2)
        click(Pattern("1662456890659.png").similar(0.90))
        assert exists(Pattern("1662456923007.png").similar(0.90))
        print("notice news pass")
        sleep(2)
        click("1662456977713.png")
        print("notice pass")
        sleep(1) 
        assert True
    else:
        print("notice error")
        assert False

# community_hand
def hand():
    click("1662457513046.png")
    sleep(1)
    click(Pattern("1662457545758.png").targetOffset(-33,0))
    if exists(Pattern("1662457561375.png").similar(0.90),60):
        click("1662457804352.png")
        print("featured hand pass")
        sleep(1)
        assert True
    else:
        print("featured hand error")
        assert False        

# community_post
def post():
    click("1662457513046.png")
    sleep(1)
    click(Pattern("1662457886258.png").targetOffset(-36,0))
    if exists("1662457901450.png",3):
        click(Pattern("1662457901450.png").targetOffset(-183,-214))
        print("featured post pass")
        sleep(1)
        assert True
    else:
        print("featured post error")
        assert False      

# community_replay
def replay():
    click("1662458599582.png")
    if exists("1662458659333.png",60):
        click(Pattern("1662458659333.png").targetOffset(-18,0))
        sleep(1)
        click("1662458713280.png")
                
        print("featured replay pass")
        sleep(1)
        assert True
    else:
        print("featured replay error")
        assert False    

# community_hot
def hot():
    click("1662459067731.png")
    if exists((Pattern("1662459092668.png").similar(0.90))and("1663138072278.png"),60):
        print("hot pass")
        sleep(1) 
        assert True
    else:
        print("hot error")
        assert False

# community_new
def new():
    click("1662459367412.png")
    if exists((Pattern("1662459377316.png").similar(0.90))and"1663138094302.png",60):
        print("new pass")
        sleep(1) 
        assert True
    else:
        print("new error")
        assert False

# community_mine
def mine():
    click("1662459426823.png")
    if exists(Pattern("1662459436976.png").similar(0.90),60):
        print("mine pass")
        sleep(1) 
        assert True
    else:
        print("mine error")
        assert False


























