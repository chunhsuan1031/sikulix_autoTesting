from sikuli import *

### profile_nft ###
# profile_nft_interface
def nft_interface():
    if exists(Pattern("1663225662914.png").similar(0.90),60):
        print("nft interface pass")
        sleep(1) 
        assert True
    else:
        print("nft interface error")
        assert False

# profile_nft_question
def nft_question():
    if exists("1662349429755.png",60):
        click("1662349429755.png")
        sleep(1)
        assert exists("1662349503186.png",10)
        assert exists("1662349517913.png",10)
        click("1662349542540.png")
        sleep(1)
        print("nft qusetion pass")
        sleep(1) 
    else:
        print("nft qusetion error")
        assert False

# profile_nft_wallet
def nft_wallet():
    if exists("1662349759846.png",60):
        click("1662349759846.png")
        sleep(1)
        assert exists("1662349781094.png")
        click("1662349542540.png")
        sleep(1)
        print("nft wallet pass")
        sleep(1) 
    else:
        print("nft wallet error")
        assert False

# profile_nft_share
def nft_share():
    if exists("1662349853945.png",60):
        click("1662349853945.png")
        sleep(1)
        assert exists("1662349917519.png")
        click(Pattern("1662349917519.png").targetOffset(-4,-282))
        sleep(1)
        print("nft share pass")
        sleep(1) 
    else:
        print("nft share error")
        assert False

### profile_tutorial ###
# profile_tutorial
def tutorial():
    if exists(Pattern("1661395399764.png").similar(0.90),60):
        click("1661395399764.png")
        if exists(Pattern("1661395458001.png").similar(0.90),3):
            click(Pattern("1661395458001.png").targetOffset(-184,-233))
            print("tutorial pass")
            sleep(1)
            assert True
        else:
            print("tutorial error")
            assert False
    else:
        print("can't find tutorial button")
        assert False

### profile_avatar ###
# profile_avatar
def avatar():
    if exists(Pattern("1662362409205.png").similar(0.90),60):
        click(Pattern("1662362409205.png").targetOffset(3,-24))
        assert exists(Pattern("1662362503245.png").similar(0.90))
        print("avatar pass")
        sleep(1)
    else:
        print("avatar error")        
        assert False    

# profile_avatar_image
def avatar_image():
    click("1662362645264.png")
    if exists(Pattern("1662362745536.png").similar(0.90),60):
        print("avatar image pass")
        sleep(1)
        assert True    
    else:    
        print("avatar image error")
        assert False

# profile_avatar_image_customize
def avatar_image_customize():
    click(Pattern("1662363123128.png").similar(0.90))
    if exists("1662363173051.png",60):
        print("avatar image customize pass")
        click("1662363193954.png")
        sleep(1)
        assert True
    else:
        print("avatar image customize error")        
        assert False

# profile_avatar_image_album
def avatar_image_album():
    click(Pattern("1662363379151.png").similar(0.90))
    sleep(1)
    if exists(Pattern("1662363505157.png").similar(0.90),60):
        print("avatar image album pass")
        click("1662363591579.png")
        sleep(1)
        assert True
    else:
        print("avatar image album error")        
        assert False

# profile_avatar_image_cancel
def avatar_image_cancel():
    click(Pattern("1662363838851.png").similar(0.90))
    sleep(1)    
    if exists(Pattern("1662362503245.png").similar(0.90),60):
        print("avatar image cancel pass")
        sleep(1)
        assert True
    else:
        print("avatar image cancel error") 
        assert False

# profile_avatar_photo frame
def avatar_photoFrame():
    click(Pattern("1662364397855.png").similar(0.90))
    if exists("1662364434611.png",60):
        click("1662364475487.png")
        print("avatar photo frame pass")
        sleep(1)
        assert True
    else:
        print("avatar photo frame pass")        
        assert False

# profile_avatar_name
def avatar_name():
    click("1662365473943.png")
    if exists("1662365509338.png",60):
        click(Pattern("1662365509338.png").targetOffset(173,113))
        print("avatar name pass")
        sleep(1)
        assert True
    else:
        print("avatar name error")
        assert False        

# profile_avatar_region
def avatar_region():
    click(Pattern("1662365805523.png").similar(0.90))
    if exists("1662365828202.png",60):
        click(Pattern("1662365854801.png").similar(0.90))
        print("avatar region pass")
        sleep(1)
        assert True
    else:
        print("avatar region error")
        assert False

# profile_avatar_confirm
def avatar_confirm():
    click(Pattern("1662366139547.png").similar(0.90))
    if exists(Pattern("1662366166515.png").similar(0.90),60):
        print("avatar region confirm pass")
        sleep(1)
        assert True
    else:
        print("avatar region confirm error")
        assert False

### profile_lv ###
# profile_lv
def lv(): 
    click("1662370044214.png")
    if exists("1662370189796.png"and"1662370213972.png"and"1662370322525.png",60):
        print("lv pass")
        click("1662370309863.png")
        sleep(1)
        assert True
    else:
        print("lv error")
        assert False

### profile_hand ###
# profile_hand_recent
def hand_recent():
    click(Pattern("1662370466469.png").similar(0.90))
    if exists("1662371062748.png"and"1662371339313.png"and"1662371544361.png",60):
        print("hand recent pass")
        sleep(1)
        assert True
    else:
        print("hand recent error")
        assert False

# profile_hand_recent_replay
def hand_recent_replay():
    click("1662371544361.png")
    if exists("1662372129343.png"and"1662372143276.png",60):
        click(Pattern("1662372164863.png").targetOffset(-26,-2))
        sleep(1)
        click("1662372222706.png")
        print("hand recent replay pass")  
        assert True
    else:
        print("hand recent replay error")
        assert False

# profile_hand_recent_share
def hand_recent_share():
    click("1662372622286.png")
    if exists("1662372664836.png",60):
        click("1662372699233.png")
        sleep(1)
        print("hand recent share pass")
        assert True
    else:
        print("hand recent share error")
        assert False

# profile_hand_recent_heart
def hand_recent_heart():
    click("1662372878790.png")
    if exists("1662372909940.png",60):
        click("1662372909940.png")
        sleep(1)
        print("hand recent heart pass")
        assert True
    else:
        print("hand recent heart error")
        assert False

# profile_hand_collect
def hand_collect():
    click("1662373051750.png")
    if exists("1662373085469.png"and"1662373103733.png"and"1662373117218.png",60):
        print("hand collect pass")
        assert True
    else:
        print("hand collect error")
        assert False

# profile_hand_collect_replay
def hand_collect_replay():
    click("1662371544361.png")
    if exists("1662372129343.png"and"1662372143276.png",60):
        click(Pattern("1662372164863.png").targetOffset(-26,-2))
        sleep(1)
        click("1662372222706.png")
        print("hand collect replay pass")  
        assert True
    else:
        print("hand collect replay error")  
        assert False

# profile_hand_collect_share
def hand_collect_share():
    click("1662372622286.png")
    if exists("1662372664836.png",60):
        click("1662372699233.png")
        sleep(1)
        print("hand collect share pass")
        assert True
    else:
        print("hand collect share error")
        assert False

### profile_feedback ###
# profile_feedback
def feedback():
    if exists(Pattern("1662432866140.png").similar(0.90),60):
        click("1662432866140.png")
        sleep(1)
        if exists("1662432895695.png",60):
            click(Pattern("1662432895695.png").targetOffset(-181,-419))
            print("feedback pass")
            sleep(1)
            assert True
        else:
            print("feedback error")
            assert False
    else:
        print("can't find feedback button")
        assert False    

### profile_setup ###
# profile_setup
def setup():
    if exists(Pattern("1662433614253.png").similar(0.90),60):
        click("1662433614253.png")
        sleep(1)
        if exists("1662433672808.png"):
            print("setup pass")
            sleep(1)
            assert True
        else:
            print("setup error")
            assert False
    else:
        print("can't find setup button")
        assert False    

# profile_setup_sound
def setup_sound():
    click("1662437868644.png")
    if exists("1662437891993.png",60):
        click("1662437891993.png")
        sleep(1)
        print("setup sound pass")
        assert True
    else:
        print("setup sound error")
        assert False

# profile_setup_mail
def setup_mail():
    click(Pattern("1662438055456.png").similar(0.90))
    if exists("1662438076061.png",60):
        click(Pattern("1662438076061.png").targetOffset(181,-179))
        sleep(1)
        print("setup mail pass")
        assert True
    else:
        print("setup mail error")
        assert False

# profile_setup_password
def setup_password():
    click(Pattern("1662438148820.png").similar(0.90))
    if exists("1662438159976.png",60):
        click(Pattern("1662438159976.png").targetOffset(180,-150))
        sleep(1)
        print("setup password pass")
        assert True
    else:
        print("setup password error")
        assert False

# profile_setup_language
def setup_language():
    click(Pattern("1662438255276.png").similar(0.90))
    if exists("1662438267860.png",60):
        click(Pattern("1662438267860.png").targetOffset(180,-280))
        sleep(1)
        print("setup language pass")
        assert True
    else:
        print("setup language error")
        assert False

# profile_setup_sign out
def setup_signOut():
    click(Pattern("1662438353895.png").similar(0.90))
    if exists("1662438370695.png",60):
        if exists("1662603882286.png",3):
            click("1662603882286.png")
            sleep(1)
        type(Pattern("1662438370695.png").targetOffset(-149,8),"wong2648" + Key.ENTER)
        sleep(1)
        click(Pattern("1662438370695.png").targetOffset(-4,138))
        wait(Pattern("1661397070003.png").similar(0.94),60)
        sleep(1)
        click("1662430711217-1.png")
        sleep(1)
        print("setup sign out pass")
        assert True
    else:
        print("setup sign out error")
        assert False

### profile_about us ###
# profile_about us
def aboutUs():
    if exists(Pattern("1662439772525.png").similar(0.90),60):
        click("1662439772525.png")
        sleep(1)
        if exists("1662439793788.png"):
            print("about us pass")
            sleep(1)
            assert True
        else:
            print("about us error")
            assert False
    else:
        print("can't find about us button")
        assert False    

# profile_about us_fair
def aboutUs_fair():
    click(Pattern("1662439868949.png").similar(0.90))
    if exists("1662439884073.png",60):
        click(Pattern("1662439884073.png").targetOffset(181,-281))
        sleep(1)
        print("about us fair pass")
        assert True
    else:
        print("about us fair error")
        assert False

# profile_about us_contact us
def aboutUs_contactUs():
    click(Pattern("1662440065623.png").similar(0.90))
    if exists("1662440079622.png",60):
        click(Pattern("1662440079622.png").targetOffset(180,-223))
        sleep(1)
        print("about us contact us pass")
        assert True
    else:
        print("about us contact us error")
        assert False

# profile_about us_service
def aboutUs_service():
    click(Pattern("1662440151493.png").similar(0.90))
    if exists("1662440176191.png",3):
        click(Pattern("1662440176191.png").targetOffset(122,427))
        sleep(1)
        print("about us service pass")
        assert True
    else:
        print("about us service error")
        assert False

# profile_about us_privacy
def aboutUs_privacy():
    click(Pattern("1662440257941.png").similar(0.90))
    if exists("1662440272716.png",60):
        click(Pattern("1662440272716.png").targetOffset(122,432))
        sleep(1)
        click("1662440313088.png")
        print("about us privacy pass")
        assert True
    else:
        print("about us privacy error")
        assert False

### profile_compliance ###
# profile_compliance
def compliance():
    if exists(Pattern("1662447890002.png").similar(0.90),60):
        click("1662447890002.png")
        sleep(1)
        if exists("1662447908276.png",60):
            click(Pattern("1662447908276.png").targetOffset(180,-296)) 
            print("compliance pass")
            sleep(1)
            assert True
        else:
            print("compliance error")
            assert False
    else:
        print("can't find compliance button")
        assert False   

### profile_invite ###
# profile_invite
def invite():
    if exists(Pattern("1663124696240.png").similar(0.90),60):
        click(Pattern("1663124696240.png").similar(0.90))
        sleep(1)
        if exists(Pattern("1663042227256.png").similar(0.90),60):
            print("invite pass")
            sleep(1)
            assert True
        else:
            print("invite error")
            assert False
    else:
        print("can't find invite button")
        assert False 

# profile_invite_copy
def invite_copy():
    click("1662448337242.png")
    if exists("1662448402092.png",60):
        print("invite copy pass")
        assert True
    else:
        print("invite copy error")        
        assert False 
        
# profile_invite_share
def invite_share():
    click("1662448853853.png")
    if exists("1662448863336.png",60):
        sleep(1)
        click("1662448892278.png")
        print("invite share pass")
        assert True
    else:
        print("invite share error")        
        assert False 

# profile_invite_poster
def invite_poster():
    click("1662448948396.png")
    if exists("1662448958366.png",60):
        sleep(1)
        click("1662448973736.png")
        print("invite poster pass")
        assert True
    else:
        print("invite poster error")        
        assert False 

# profile_invite_task
def invite_task():
    click("1662449137340.png")
    if exists("1662449147086.png",60):
        sleep(1)
        click("1662449158896.png")
        print("invite task pass")
        assert True
    else:
        print("invite task error")        
        assert False 

















        




        