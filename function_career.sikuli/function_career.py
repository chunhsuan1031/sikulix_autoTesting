from sikuli import *
import function_common

### career ###
# career
def career():
    function_common.declineInvitation()
    if exists(Pattern("1662606492525.png").similar(0.90),15):
        print("career pass")
        sleep(1) 
        assert True
    else:
        print("career error")
        assert False

# career_month
def career_month():
    click("1662606661720.png")
    function_common.declineInvitation()
    if exists((Pattern("1662606701946.png").similar(0.90)and"1662606717141.png")or(Pattern("1662607292113.png").similar(0.90)and"1662607440208.png"),15):
        print("career month pass")
        sleep(1) 
        assert True
    else:
        print("career month error")
        assert False

# career_year
def career_year():
    click("1662607278520.png")
    function_common.declineInvitation()
    if exists(Pattern("1662607292113.png").similar(0.90)and"1662607303666.png",15):
        print("career year pass")
        sleep(1) 
        assert True
    else:
        print("career year error")
        assert False

# career_day
def career_day():
    click("1662607341450.png")
    function_common.declineInvitation()
    if exists(Pattern("1662607354817.png").similar(0.90)and"1662607368181.png",15):
        print("career day pass")
        sleep(1) 
        assert True
    else:
        print("career day error")
        assert False

# career_filter
def career_filter():
    function_common.declineInvitation()
    click("1662948899462.png")
    function_common.declineInvitation()
    if exists("1662954760202.png"and"1662954769653.png"and"1662954778518.png",15):
        print("career club pass")
        sleep(1) 
        assert True
    else:
        print("career club error")
        assert False

# career_club_nlh
def career_club_nlh():
    click(Pattern("1662951553899.png").targetOffset(-42,-69))
    function_common.declineInvitation()
    if exists(Pattern("1662951588340.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662952086718.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career club nlh pass")
            sleep(1)     
            assert True    
        else:
            print("career club nlh data error")            
            assert False
    else:
        print("career club nlh error")
        assert False

# career_club_aof
def career_club_aof():
    click(Pattern("1662954838881.png").targetOffset(35,-72))
    function_common.declineInvitation()
    if exists(Pattern("1662954893221.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662954909220.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career club aof pass")
            sleep(1)     
            assert True    
        else:
            print("career club aof data error")            
            assert False
    else:
        print("career club aof error")
        assert False

# career_club_sixPlus
def career_club_sixPlus():
    click(Pattern("1662955022134.png").targetOffset(117,-71))
    function_common.declineInvitation()
    if exists(Pattern("1662965930840.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662965959743.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career club 6+ pass")
            sleep(1)     
            assert True    
        else:
            print("career club 6+ data error")            
            assert False
    else:
        print("career club 6+ error")
        assert False

# career_club_plo
def career_club_plo():
    click(Pattern("1662966134568.png").targetOffset(-120,-26))
    function_common.declineInvitation()
    if exists(Pattern("1662966200853.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662966212704.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club plo pass")
            sleep(1)     
            assert True    
        else:
            print("career club plo data error")            
            assert False
    else:
        print("career club plo error")
        assert False

# career_club_ploHL
def career_club_ploHL():
    click(Pattern("1662966666960.png").targetOffset(-43,-29))
    function_common.declineInvitation()
    if exists(Pattern("1662966695337.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662966707036.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club plo H/L pass")
            sleep(1)     
            assert True    
        else:
            print("career club plo H/L data error")            
            assert False
    else:
        print("career club plo H/L error")
        assert False

# career_club_flashNlh
def career_club_flashNlh():
    click(Pattern("1662967105562.png").targetOffset(37,-29))
    function_common.declineInvitation()
    if exists(Pattern("1662967136087.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662969288189.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club Flash NLH pass")
            sleep(1)     
            assert True    
        else:
            print("career club Flash NLH data error")            
            assert False
    else:
        print("career club Flash NLH error")
        assert False

# career_club_flashPlo
def career_club_flashPlo():
    click(Pattern("1662969050771.png").targetOffset(116,-30))
    function_common.declineInvitation()
    if exists(Pattern("1662969075042.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662969264852.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club Flash PLO pass")
            sleep(1)     
            assert True    
        else:
            print("career club Flash PLO data error")            
            assert False
    else:
        print("career club Flash PLO error")
        assert False

# career_club_nlhPlo
def career_club_nlhPlo():
    click(Pattern("1662974508560.png").targetOffset(-123,12))
    function_common.declineInvitation()
    if exists(Pattern("1662969231689.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662969241699.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club NLH&PLO pass")
            sleep(1)     
            assert True    
        else:
            print("career club NLH&PLO data error")            
            assert False
    else:
        print("career club NLH&PLO error")
        assert False

# career_club_pusoy
def career_club_pusoy():
    click(Pattern("1662969365451.png").targetOffset(-39,13))
    function_common.declineInvitation()
    if exists(Pattern("1662969387476.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662969550557.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career club pusoy pass")
            sleep(1)     
            assert True    
        else:
            print("career club pusoy data error")            
            assert False
    else:
        print("career club pusoy error")
        assert False

# career_club_ofc
def career_club_ofc():
    click(Pattern("1662969690956.png").targetOffset(37,11))
    function_common.declineInvitation()
    if exists(Pattern("1662969844842.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662970034346.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career club ofc pass")
            sleep(1)     
            assert True    
        else:
            print("career club ofc data error")            
            assert False
    else:
        print("career club ofc error")
        assert False

# career_club_spinUp
def career_club_spinUp():
    click(Pattern("1662970820900.png").targetOffset(115,14))
    function_common.declineInvitation()
    if exists(Pattern("1662970843678.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662970853917.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club spinup pass")
            sleep(1)     
            assert True    
        else:
            print("career club spinup data error")            
            assert False
    else:
        print("career club spinup error")
        assert False

# career_club_sngNlh
def career_club_sngNlh():
    click(Pattern("1662970935532.png").targetOffset(-118,57))
    function_common.declineInvitation()
    if exists(Pattern("1662970964634.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662970978618.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club SNG NLH pass")
            sleep(1)     
            assert True    
        else:
            print("career club SNG NLH data error")            
            assert False
    else:
        print("career club SNG NLH error")
        assert False

# career_club_sngPlo
def career_club_sngPlo():
    click(Pattern("1662972409543.png").targetOffset(-41,52))
    function_common.declineInvitation()
    if exists(Pattern("1662972455365.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662972466483.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club SNG PLO pass")
            sleep(1)     
            assert True    
        else:
            print("career club SNG PLO data error")            
            assert False
    else:
        print("career club SNG PLO error")
        assert False

# career_club_mttNlh
def career_club_mttNlh():
    click(Pattern("1662972544054.png").targetOffset(40,54))
    function_common.declineInvitation()
    if exists(Pattern("1662972564941.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662972574582.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career club MTT NLH pass")
            sleep(1)     
            assert True    
        else:
            print("career club MTT NLH data error")            
            assert False
    else:
        print("career club MTT NLH error")
        assert False

# career_club_mttPlo
def career_club_mttPlo():
    click(Pattern("1662972624277.png").targetOffset(119,55))
    function_common.declineInvitation()
    if exists(Pattern("1662972643726.png").similar(0.96),15):
        click("1662951618020.png")
        if exists(Pattern("1662972657438.png").similar(0.96),15):
            click("1662952106908.png") 
            print("career club MTT PLO pass")
            sleep(1)     
            assert True    
        else:
            print("career club MTT PLO data error")            
            assert False
    else:
        print("career club MTT PLO error")
        assert False

# career_club_teenPatti
def career_club_teenPatti():
    click(Pattern("1662972721559.png").targetOffset(-122,94))
    function_common.declineInvitation()
    if exists(Pattern("1662972745613.png").similar(0.94),15):
        print("career club Teen Patti pass")
        sleep(1)     
        assert True    
    else:
        print("career club Teen Patti error")
        assert False

# career_club_all
def career_club_all():
    click(Pattern("1662972875862.png").targetOffset(-120,-77))
    function_common.declineInvitation()
    if exists(Pattern("1662972895100.png").similar(0.95),15):
        print("career club All pass")
        sleep(1)     
        assert True    
    else:
        print("career club All error")
        assert False

# career_lobby_all
def career_lobby_all():
    click(Pattern("1662974890792.png").targetOffset(-122,13))
    function_common.declineInvitation()
    if exists(Pattern("1662974919777.png").similar(0.95),15):
        print("career lobby All pass")
        sleep(1)     
        assert True    
    else:
        print("career lobby All error")
        assert False

# career_lobby_nlh
def career_lobby_nlh():
    click(Pattern("1662974999494.png").targetOffset(-40,11))
    function_common.declineInvitation()
    if exists(Pattern("1662975053041.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662975081007.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career lobby NLH pass")
            sleep(1)     
            assert True    
        else:
            print("career lobby NLH data error")            
            assert False
    else:
        print("career lobby NLH error")
        assert False

# career_lobby_plo
def career_lobby_plo():
    click(Pattern("1662975217521.png").targetOffset(37,13))
    function_common.declineInvitation()
    if exists(Pattern("1662975244520.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662975253215.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career lobby PLO pass")
            sleep(1)     
            assert True    
        else:
            print("career lobby PLO data error")            
            assert False
    else:
        print("career lobby PLO error")
        assert False

# career_lobby_ofc
def career_lobby_ofc():
    click(Pattern("1662975283360.png").targetOffset(117,16))
    function_common.declineInvitation()
    if exists(Pattern("1662975300720.png").similar(0.94),15):
        click("1662951618020.png")
        if exists(Pattern("1662975310648.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career lobby OFC pass")
            sleep(1)     
            assert True    
        else:
            print("career lobby OFC data error")            
            assert False
    else:
        print("career lobby OFC error")
        assert False

# career_globalTournament_all
def career_globalTournament_all():
    click(Pattern("1662975406095.png").targetOffset(-118,-8))
    function_common.declineInvitation()
    if exists(Pattern("1662975425415.png").similar(0.95),15):
        print("career global tournament All pass")
        sleep(1)     
        assert True    
    else:
        print("career global tournament All error")
        assert False

# career_globalTournament_sng
def career_globalTournament_sng():
    click(Pattern("1662975509487.png").targetOffset(-43,-8))
    function_common.declineInvitation()
    if exists(Pattern("1662975533226.png").similar(0.94),15):
        click("1662951618020.png")
        if exists(Pattern("1662975549736.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career global tournament SNG pass")
            sleep(1)     
            assert True    
        else:
            print("career global tournament SNG data error")            
            assert False
    else:
        print("career global tournament SNG error")
        assert False

# career_globalTournament_spinUp
def career_globalTournament_spinUp():
    click(Pattern("1662975610253.png").targetOffset(36,-8))
    function_common.declineInvitation()
    if exists(Pattern("1662975621880.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662975633263.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career global tournament SpinUp pass")
            sleep(1)     
            assert True    
        else:
            print("career global tournament SpinUp data error")            
            assert False
    else:
        print("career global tournament SpinUp error")
        assert False

# career_globalTournament_mttNlh
def career_globalTournament_mttNlh():
    click(Pattern("1662975689232.png").targetOffset(118,-9))
    function_common.declineInvitation()
    if exists(Pattern("1662975707680.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662975717033.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career global tournament MTT NLH pass")
            sleep(1)     
            assert True    
        else:
            print("career global tournament MTT NLH data error")            
            assert False
    else:
        print("career global tournament MTT NLH error")
        assert False

# career_globalTournament_mttPlo
def career_globalTournament_mttPlo():
    click(Pattern("1662975761002.png").targetOffset(-122,32))
    function_common.declineInvitation()
    if exists(Pattern("1662975782184.png").similar(0.95),15):
        click("1662951618020.png")
        if exists(Pattern("1662975791506.png").similar(0.95),15):
            click("1662952106908.png") 
            print("career global tournament MTT PLO pass")
            sleep(1)     
            assert True    
        else:
            print("career global tournament MTT PLO data error")            
            assert False
    else:
        print("career global tournament MTT PLO error")
        assert False
















