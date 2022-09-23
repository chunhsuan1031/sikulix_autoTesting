from sikuli import *
import function_common
import function_club

### club ###
# club
def club():
    if exists(Pattern("1663210438783.png").similar(0.90),60):
        click(Pattern("1663210438783.png").similar(0.90))
        function_common.declineInvitation()
        if exists(Pattern("1663209991655.png").similar(0.90),60):
            print("club pass")
            assert True
        elif exists(Pattern("1663121261042.png").similar(0.90),60):
            click("1663121294039.png")
            sleep(1)
            click("1663121294039.png")
            sleep(1)
            assert exists(Pattern("1663209991655.png").similar(0.90),60)
            print("club pass")
            assert True
        elif exists(Pattern("1663121342586.png").similar(0.90),60):
            click("1663121294039.png")
            sleep(1)
            assert exists(Pattern("1663209991655.png").similar(0.90),60)
            print("club pass")
            assert True
        else:
            print("club error")
            assert False            
    else:
        print("can't find club")
        assert False

# club_mail
def club_mail():
    if exists(Pattern("1663233319853.png").similar(0.90),60):
        click(Pattern("1663233319853.png").similar(0.90))
        if exists((Pattern("1663233371964.png").similar(0.90))and(Pattern("1663233399870.png").similar(0.90)),60):
            click("1663233417677.png")
            sleep(1)
            print("club mail pass")
            assert True
        else:
            print("club mail error")
            assert False
    else:
        print("can't find club mail button")
        assert False

# club_support
def club_support():
    if exists(Pattern("1663233662822.png").similar(0.90),60):
        click(Pattern("1663233662822.png").similar(0.90))
        if exists(Pattern("1663233697221.png").similar(0.90),60):
            click("1663233732757.png")
            if exists(Pattern("1663233755156.png").similar(0.90),60):
                click("1663233786165.png")
                sleep(1)
                click("1663233810852.png")
                sleep(1)
                print("club support pass")
                assert True                
            else:
                print("club support error")
                assert False        
        else:
            print("club support error")
            assert False
    else:
        print("can't find club support button")
        assert False

# club_introduction
def club_introduction():
    if exists(Pattern("1663209991655.png").similar(0.90),60):
        click(Pattern("1663209991655.png").similar(0.90))
        if exists(Pattern("1663234270937.png").similar(0.90),60):
            print("club introduction pass")
            assert True
        else:
            print("club introduction error")
            assert False
    else:
        print("can't find club introduction button")
        assert False

# club_introduction_share
def club_introduction_share():
    if exists(Pattern("1663234473422.png").similar(0.90),60):
        click(Pattern("1663234473422.png").similar(0.90))
        if exists(Pattern("1663234508612.png").similar(0.90),60):
            click("1663238038313.png")
            print("club introduction share pass")
            assert True
        else:
            print("club introduction share error")
            assert False
    else:
        print("can't find club introduction share button")
        assert False

# club_introduction_edit
def club_introduction_edit():
    if exists(Pattern("1663234839784.png").similar(0.90),60):
        click(Pattern("1663234839784.png").similar(0.90))
        if exists(Pattern("1663234957021.png").similar(0.90),60):
            print("club introduction edit page pass")
        else:
            print("club introduction error")
            assert False
        if exists(Pattern("1663235173550.png").similar(0.90),60):
            click(Pattern("1663235173550.png").similar(0.90))
            assert exists(Pattern("1663235576816.png").similar(0.90),60)
            click("1663238076055.png")
            print("club introduction edit share pass")
        else:
            print("club introduction edit share error")
            assert False
        if exists(Pattern("1663235745823.png").similar(0.90),60):
            click(Pattern("1663235745823.png").similar(0.90))
            assert exists(Pattern("1663235794093.png").similar(0.90),60)
            click(Pattern("1663235794093.png").similar(0.90).targetOffset(0,-15))
            assert exists("1663235866911.png",60)
            click("1663235885030.png")
            print("club introduction edit album pass")
        else:
            print("club introduction edit album error")
            assert False
        if exists(Pattern("1663236246311.png").similar(0.90),60):
            click(Pattern("1663236246311.png").similar(0.90))
            assert exists("1663734347811.png",60)
            click(Pattern("1663236932126.png").similar(0.90))
            print("club introduction edit name pass")
        else:
            print("club introduction edit name error")
            assert False
        if exists(Pattern("1663237431880.png").similar(0.90),60):
            click(Pattern("1663237431880.png").similar(0.90))
            assert exists("1663734347811.png",60)
            click(Pattern("1663236932126.png").similar(0.90))
            sleep(1)
            print("club introduction edit announcement pass")
        else:
            print("club introduction edit announcement error")
            assert False
        click("1663237605960.png")
        sleep(1)
        click("1663237605960.png")
        sleep(1)
        print("club introduction edit pass")
        assert True
    else:
        print("club introduction edit error")
        assert False

# club_ppcoin
def club_ppcoin():
    if exists(Pattern("1663310745169.png").similar(0.90),60):
        click(Pattern("1663310745169.png").similar(0.90))
        if exists((Pattern("1663310812477.png").similar(0.90))and(Pattern("1663310839634.png").similar(0.90)),60):
            print("club ppcoin pass")
            assert True
        else:
            print("club ppcoin error")
            assert False
    else:
        print("can't find club ppcoin button")
        assert False

# club_ppcoin_ppcoinExchange
def club_ppcoin_ppcoinExchange():
    if exists(Pattern("1663311056560.png").similar(0.90),60):
        click(Pattern("1663311056560.png").similar(0.90))
        if exists(Pattern("1663311100528.png").similar(0.90),60):
            click(Pattern("1663311116074.png").similar(0.90))
            print("club ppcoin ppcoinExchange pass")
            assert True
        else:
            print("club ppcoin ppcoinExchange error")
            assert False
    else:
        print("can't find club ppcoin ppcoinExchange button")
        assert False

# club_ppcoin_daimondExchange
def club_ppcoin_daimondExchange():
    if exists(Pattern("1663311484667.png").similar(0.90),60):
        click(Pattern("1663311484667.png").similar(0.90))
        if exists(Pattern("1663311522866.png").similar(0.90),60):
            if exists(Pattern("1663311795993.png").similar(0.90),60):
                click(Pattern("1663311795993.png").similar(0.90))
                assert exists(Pattern("1663311985289.png").similar(0.90),60)
                click(Pattern("1663312017560.png").similar(0.90))
                sleep(1)
                print("club ppcoin daimondExchange 60 pass")
            else:
                print("club ppcoin daimondExchange 60 error")
                assert False
            if exists(Pattern("1663312110920.png").similar(0.90),60):
                click(Pattern("1663312110920.png").similar(0.90))
                assert exists(Pattern("1663312131281.png").similar(0.90),60)
                click(Pattern("1663312017560.png").similar(0.90))
                sleep(1)
                print("club ppcoin daimondExchange 780 pass")
            else:
                print("club ppcoin daimondExchange 780 error")
                assert False
            if exists(Pattern("1663312201649.png").similar(0.90),60):
                click(Pattern("1663312201649.png").similar(0.90))
                assert exists(Pattern("1663312226115.png").similar(0.90),60)
                click(Pattern("1663312017560.png").similar(0.90))
                sleep(1)
                print("club ppcoin daimondExchange 6280+188 pass")
            else:
                print("club ppcoin daimondExchange 6280+188 error")
                assert False
            click("1663313293088.png")
        else:
            print("club ppcoin daimondExchange error")
            assert False
    else:
        print("can't find club ppcoin daimondExchange button")
        assert False

# club_globalTournament
def club_globalTournament():
    if exists(Pattern("1663314084267.png").similar(0.90),60):
        click("1663314084267.png")
        #function_common.declineInvitation()
        if exists("1663054039133.png"and(Pattern("1663054222636.png").similar(0.90)),60):
            click("1663053346296.png")
            print("club global tournament pass")
            assert True
        else:
            print("club global tournament error")
            assert False            
    else:
        print("can't find club global tournament")
        assert False

# club_league
def club_league():
    if exists(Pattern("1663314837509.png").similar(0.90),60):
        click(Pattern("1663314837509.png").similar(0.90))
        if exists("1663316193964.png",60):
            print("club league pass")
            assert True
        else:
            print("club league error")
            assert False            
    else:
        print("can't find club league")
        assert False

# club_league_add
def club_league_add():
    if exists(Pattern("1663317199112.png").similar(0.90),60):
        click(Pattern("1663317199112.png").similar(0.90))
        if exists(Pattern("1663317363335.png").similar(0.90),60):
            click(Pattern("1663317399232.png").similar(0.90).targetOffset(-81,0))
            sleep(1)
            click(Pattern("1663317433776.png").similar(0.90))
            if exists(Pattern("1663317454349.png").similar(0.90),60):
                click(Pattern("1663317497953.png").similar(0.90))
                #club league add sale
                if exists(Pattern("1663317989566.png").similar(0.90),60):
                    click(Pattern("1663317989566.png").similar(0.90))
                    assert exists(Pattern("1663318022327.png").similar(0.90),60)
                    click(Pattern("1663318054998.png").similar(0.90))
                    print("club league add sale pass")
                else:
                    print("club league add sale error")
                    assert False
                #club league add 2 star
                if exists(Pattern("1663821760059.png").similar(0.90),60):
                    click(Pattern("1663821760059.png").similar(0.90))
                    assert exists(Pattern("1663318469574.png").similar(0.95),60)
                    click(Pattern("1663318469574.png").similar(0.95).targetOffset(182,-149))
                    print("club league add 2 star pass")
                else:
                    print("club league add 2 star error")
                    assert False
                #club league add 3 star
                if exists(Pattern("1663830760556.png").similar(0.90),60):
                    click(Pattern("1663830760556.png").similar(0.90))
                    assert exists(Pattern("1663318759198.png").similar(0.95),60)
                    click(Pattern("1663318759198.png").similar(0.95).targetOffset(183,-151))
                    print("club league add 3 star pass")
                else:
                    print("club league add 3 star error")
                    assert False
                #club league add 4 star
                if exists(Pattern("1663830790483.png").similar(0.90),60):
                    click(Pattern("1663830790483.png").similar(0.90))
                    assert exists(Pattern("1663318916711.png").similar(0.95).targetOffset(184,-152),60)
                    click(Pattern("1663318916711.png").similar(0.95).targetOffset(184,-152))
                    print("club league add 4 star pass")
                else:
                    print("club league add 4 star error")
                    assert False
                #club league add 5 star
                if exists(Pattern("1663830817150.png").similar(0.90),60):
                    click(Pattern("1663830817150.png").similar(0.90))
                    assert exists(Pattern("1663320085097.png").similar(0.95),60)
                    click(Pattern("1663320085097.png").similar(0.95).targetOffset(180,-151))
                    print("club league add 5 star pass")
                else:
                    print("club league add 5 star error")
                    assert False
                # switch lv6
                sleep(1)
                dragDrop(Pattern("1663830817150.png").similar(0.90),Pattern("1663821760059.png").similar(0.90))
                sleep(1)
                #club league add 6 star
                if exists(Pattern("1663830882979.png").similar(0.90),60):
                    click(Pattern("1663830882979.png").similar(0.90))
                    assert exists(Pattern("1663659749986.png").similar(0.95),60)
                    click(Pattern("1663659749986.png").similar(0.95).targetOffset(182,-151))
                    print("club league add 6 star pass")
                else:
                    print("club league add 6 star error")
                    assert False
                #club league add 7 star
                if exists(Pattern("1663830911529.png").similar(0.90),60):
                    click(Pattern("1663830911529.png").similar(0.90))
                    assert exists(Pattern("1663660486242.png").similar(0.95),60)
                    click(Pattern("1663660486242.png").similar(0.95).targetOffset(183,-151))
                    print("club league add 7 star pass")
                else:
                    print("club league add 7 star error")
                    assert False
                #club league add 8 star
                if exists(Pattern("1663830932339.png").similar(0.90),60):
                    click(Pattern("1663830932339.png").similar(0.90))
                    assert exists(Pattern("1663661260722.png").similar(0.95),60)
                    click(Pattern("1663661260722.png").similar(0.95).targetOffset(181,-153))
                    print("club league add 8 star pass")
                else:
                    print("club league add 8 star error")
                    assert False
                # switch lv10
                sleep(1)
                dragDrop(Pattern("1663830932339.png").similar(0.90),Pattern("1663830882979.png").similar(0.90))
                sleep(1)
                #club league add 9 star
                if exists(Pattern("1663831001643.png").similar(0.90),60):
                    click(Pattern("1663831001643.png").similar(0.90))
                    assert exists(Pattern("1663661473162.png").similar(0.95),60)
                    click(Pattern("1663661473162.png").similar(0.95).targetOffset(182,-151))
                    print("club league add 9 star pass")
                else:
                    print("club league add 9 star error")
                    assert False
                #club league add 10 star
                if exists(Pattern("1663831022380.png").similar(0.90),60):
                    click(Pattern("1663831022380.png").similar(0.90))
                    assert exists(Pattern("1663661740242.png").similar(0.95),60)
                    click(Pattern("1663661740242.png").similar(0.95).targetOffset(182,-152))
                    print("club league add 10 star pass")
                else:
                    print("club league add 10 star error")
                    assert False
                sleep(1)
                click(Pattern("1663662834877.png").similar(0.90))
                sleep(1)
                click(Pattern("1663662834877.png").similar(0.90))
            else:  
                print("club league add error")
                assert False
        else:
            print("club league add error")
            assert False            
    else:
        print("can't find club league add")
        assert False

# club_league_create
def club_league_create():
    if exists(Pattern("1663664062302.png").similar(0.90),60):
        click(Pattern("1663664062302.png").similar(0.90))
        if exists(Pattern("1663317363335.png").similar(0.90),60):
            click(Pattern("1663317399232.png").similar(0.90).targetOffset(-81,0))
            sleep(1)
            click(Pattern("1663317433776.png").similar(0.90))
            if exists(Pattern("1663317454349.png").similar(0.90),60):
                click(Pattern("1663317497953.png").similar(0.90))
                #club league add sale
                if exists(Pattern("1663317989566.png").similar(0.90),60):
                    click(Pattern("1663317989566.png").similar(0.90))
                    assert exists(Pattern("1663318022327.png").similar(0.90),60)
                    click(Pattern("1663318054998.png").similar(0.90))
                    print("club league create sale pass")
                else:
                    print("club league create sale error")
                    assert False
                #club league add 2 star
                if exists(Pattern("1663821760059.png").similar(0.90),60):
                    click(Pattern("1663821760059.png").similar(0.90))
                    assert exists(Pattern("1663318469574.png").similar(0.95),60)
                    click(Pattern("1663318469574.png").similar(0.95).targetOffset(182,-149))
                    print("club league add 2 star pass")
                else:
                    print("club league add 2 star error")
                    assert False
                #club league add 3 star
                if exists(Pattern("1663830760556.png").similar(0.90),60):
                    click(Pattern("1663830760556.png").similar(0.90))
                    assert exists(Pattern("1663318759198.png").similar(0.95),60)
                    click(Pattern("1663318759198.png").similar(0.95).targetOffset(183,-151))
                    print("club league add 3 star pass")
                else:
                    print("club league add 3 star error")
                    assert False
                #club league add 4 star
                if exists(Pattern("1663830790483.png").similar(0.90),60):
                    click(Pattern("1663830790483.png").similar(0.90))
                    assert exists(Pattern("1663318916711.png").similar(0.95).targetOffset(184,-152),60)
                    click(Pattern("1663318916711.png").similar(0.95).targetOffset(184,-152))
                    print("club league add 4 star pass")
                else:
                    print("club league add 4 star error")
                    assert False
                #club league add 5 star
                if exists(Pattern("1663830817150.png").similar(0.90),60):
                    click(Pattern("1663830817150.png").similar(0.90))
                    assert exists(Pattern("1663320085097.png").similar(0.95),60)
                    click(Pattern("1663320085097.png").similar(0.95).targetOffset(180,-151))
                    print("club league add 5 star pass")
                else:
                    print("club league add 5 star error")
                    assert False
                # switch lv6
                sleep(1)
                dragDrop(Pattern("1663830817150.png").similar(0.90),Pattern("1663821760059.png").similar(0.90))
                sleep(1)
                #club league add 6 star
                if exists(Pattern("1663830882979.png").similar(0.90),60):
                    click(Pattern("1663830882979.png").similar(0.90))
                    assert exists(Pattern("1663659749986.png").similar(0.95),60)
                    click(Pattern("1663659749986.png").similar(0.95).targetOffset(182,-151))
                    print("club league add 6 star pass")
                else:
                    print("club league add 6 star error")
                    assert False
                #club league add 7 star
                if exists(Pattern("1663830911529.png").similar(0.90),60):
                    click(Pattern("1663830911529.png").similar(0.90))
                    assert exists(Pattern("1663660486242.png").similar(0.95),60)
                    click(Pattern("1663660486242.png").similar(0.95).targetOffset(183,-151))
                    print("club league add 7 star pass")
                else:
                    print("club league add 7 star error")
                    assert False
                #club league add 8 star
                if exists(Pattern("1663830932339.png").similar(0.90),60):
                    click(Pattern("1663830932339.png").similar(0.90))
                    assert exists(Pattern("1663661260722.png").similar(0.95),60)
                    click(Pattern("1663661260722.png").similar(0.95).targetOffset(181,-153))
                    print("club league add 8 star pass")
                else:
                    print("club league add 8 star error")
                    assert False
                # switch lv10
                sleep(1)
                dragDrop(Pattern("1663830932339.png").similar(0.90),Pattern("1663830882979.png").similar(0.90))
                sleep(1)
                #club league add 9 star
                if exists(Pattern("1663831001643.png").similar(0.90),60):
                    click(Pattern("1663831001643.png").similar(0.90))
                    assert exists(Pattern("1663661473162.png").similar(0.95),60)
                    click(Pattern("1663661473162.png").similar(0.95).targetOffset(182,-151))
                    print("club league add 9 star pass")
                else:
                    print("club league add 9 star error")
                    assert False
                #club league add 10 star
                if exists(Pattern("1663831022380.png").similar(0.90),60):
                    click(Pattern("1663831022380.png").similar(0.90))
                    assert exists(Pattern("1663661740242.png").similar(0.95),60)
                    click(Pattern("1663661740242.png").similar(0.95).targetOffset(182,-152))
                    print("club league add 10 star pass")
                else:
                    print("club league add 10 star error")
                    assert False
                sleep(1)
                click(Pattern("1663662834877.png").similar(0.90))
                sleep(1)
                click(Pattern("1663662834877.png").similar(0.90))
            else:  
                print("club league create error")
                assert False
        else:
            print("club league create error")
            assert False            
    else:
        print("can't find club league create")
        assert False

# club_member
def club_member():
    if exists(Pattern("1663665481116.png").similar(0.90),60):
        click(Pattern("1663665481116.png").similar(0.90))
        if exists((Pattern("1663665611770.png").similar(0.90))and(Pattern("1663665633277.png").similar(0.90)),60):
            print("club member pass")
            assert True
        else:
            print("club member error")
            assert False            
    else:
        print("can't find club member")
        assert False

# club_member_personalInfo
def club_member_personalInfo():
    if exists(Pattern("1663666130410.png").similar(0.90),60):
        click(Pattern("1663666130410.png").similar(0.90))
        if exists(Pattern("1663666195289.png").similar(0.90),60):
            # question
            if exists(Pattern("1663666270746.png").similar(0.90),60):
                click(Pattern("1663666270746.png").similar(0.90))
                assert exists(Pattern("1663666338472.png").similar(0.90),60)
                click(Pattern("1663666338472.png").similar(0.90).targetOffset(180,-284))
                print("club member personalInfo question pass")
            else:
                print("club member personalInfo question error")
                assert False
            # edit
            if exists(Pattern("1663667557903.png").similar(0.90),60):
                click(Pattern("1663667557903.png").similar(0.90))
                assert exists(Pattern("1663667595666.png").similar(0.90),60)
                click(Pattern("1663667595666.png").similar(0.90).targetOffset(181,-177))
                print("club member personalInfo edit pass")
            else:
                print("club member personalInfo edit error")
                assert False
            # before 7 days
            if exists(Pattern("1663667780341.png").similar(0.90),60):
                click(Pattern("1663667780341.png").similar(0.90))
                assert exists(Pattern("1663667824432.png").similar(0.95),60)
                print("club member personalInfo before 7 days pass")
            else:
                print("club member personalInfo before 7 days error")
                assert False
            # choose day
            if exists(Pattern("1663667920194.png").similar(0.90),60):
                click(Pattern("1663667920194.png").similar(0.90))
                assert exists(Pattern("1663667949653.png").similar(0.90),60)
                click(Pattern("1663667949653.png").similar(0.90).targetOffset(-174,-18))
                print("club member personalInfo choose day pass")
            else:
                print("club member personalInfo choose day error")
                assert False
            # track
            if exists(Pattern("1663668075946.png").similar(0.90),60):
                click(Pattern("1663668075946.png").similar(0.90))
                assert exists(Pattern("1663668103409.png").similar(0.90),60)
                click(Pattern("1663668103409.png").similar(0.90).targetOffset(176,-2))
                print("club member personalInfo track pass")
            else:
                print("club member personalInfo track error")
                assert False
            sleep(1)
            click(Pattern("1663668257403.png").similar(0.95).targetOffset(180,0))
            print("club member personalInfo pass")
        else:
            print("club member personalInfo error")
            assert False            
    else:
        print("can't find club member personalInfo")
        assert False

# club_member_otherInfo
def club_member_otherInfo():
    if exists(Pattern("1663668442377.png").similar(0.90),60):
        click(Pattern("1663668442377.png").similar(0.90))
        if exists(Pattern("1663668496760.png").similar(0.90),60):
            # question
            if exists(Pattern("1663666270746.png").similar(0.90),60):
                click(Pattern("1663666270746.png").similar(0.90))
                assert exists(Pattern("1663666338472.png").similar(0.90),60)
                click(Pattern("1663666338472.png").similar(0.90).targetOffset(180,-284))
                print("club member otherInfo question pass")
            else:
                print("club member otherInfo question error")
                assert False
            # edit
            if exists(Pattern("1663668614922.png").similar(0.90),60):
                click(Pattern("1663668614922.png").similar(0.90))
                assert exists(Pattern("1663668644413.png").similar(0.90),60)
                click(Pattern("1663668644413.png").similar(0.90).targetOffset(178,-177))
                print("club member otherInfo edit pass")
            else:
                print("club member otherInfo edit error")
                assert False
            # before 7 days
            if exists(Pattern("1663667780341.png").similar(0.90),60):
                click(Pattern("1663667780341.png").similar(0.90))
                assert exists(Pattern("1663667824432.png").similar(0.95),60)
                print("club member otherInfo before 7 days pass")
            else:
                print("club member otherInfo before 7 days error")
                assert False
            # choose day
            if exists(Pattern("1663667920194.png").similar(0.90),60):
                click(Pattern("1663667920194.png").similar(0.90))
                assert exists(Pattern("1663667949653.png").similar(0.90),60)
                click(Pattern("1663667949653.png").similar(0.90).targetOffset(-174,-18))
                print("club member otherInfo choose day pass")
            else:
                print("club member otherInfo choose day error")
                assert False
            # administrator
            if exists(Pattern("1663668886406.png").similar(0.90),60):
                click(Pattern("1663668886406.png").similar(0.90))
                assert exists(Pattern("1663668933944.png").similar(0.90),60)
                click(Pattern("1663668933944.png").similar(0.90).targetOffset(181,-304))
                print("club member otherInfo administrator pass")
            else:
                print("club member otherInfo administrator error")
                assert False
            # agent
            if exists(Pattern("1663669581607.png").similar(0.90),60):
                click(Pattern("1663669581607.png").similar(0.90))
                assert exists(Pattern("1663669621280.png").similar(0.90),60)
                click(Pattern("1663669621280.png").similar(0.90).targetOffset(92,147))
                print("club member otherInfo agent pass")
            else:
                print("club member otherInfo agent error")
                assert False
            # track
            if exists(Pattern("1663668075946.png").similar(0.90),60):
                click(Pattern("1663668075946.png").similar(0.90))
                assert exists(Pattern("1663668103409.png").similar(0.90),60)
                click(Pattern("1663668103409.png").similar(0.90).targetOffset(176,-2))
                print("club member otherInfo track pass")
            else:
                print("club member otherInfo track error")
                assert False
            # delete
            if exists(Pattern("1663669736483.png").similar(0.90),60):
                click(Pattern("1663669736483.png").similar(0.90))
                assert exists(Pattern("1663669763133.png").similar(0.90),60)
                click(Pattern("1663669763133.png").similar(0.90).targetOffset(182,-153))
                print("club member otherInfo delete pass")
            else:
                print("club member otherInfo delete error")
                assert False
            sleep(1)
            click(Pattern("1663746962225.png").similar(0.95).targetOffset(179,0))
            print("club member otherInfo pass")
        else:
            print("club member otherInfo error")
            assert False            
    else:
        print("can't find club member otherInfo")
        assert False

# club_member_search
def club_member_search():
    if exists(Pattern("1663730663380.png").similar(0.90),60):
        type(Pattern("1663730133218.png").similar(0.90),"2528075" + Key.ENTER)
        assert exists(Pattern("1663730713497.png").similar(0.90),60)
        click(Pattern("1663730771369.png").similar(0.95))
        assert exists(Pattern("1663730663380.png").similar(0.90),60)
        print("club member search pass")
    else:
        print("can't find club member search")
        assert False

# club_member_buyin
def club_member_buyin():                    
    if exists(Pattern("1663750426628.png").similar(0.95),60):
        click(Pattern("1663750426628.png").similar(0.95))
        if exists(Pattern("1663750490575.png").similar(0.95),60):
            click(Pattern("1663750490575.png").similar(0.95))
            assert exists(Pattern("1663750552645.png").similar(0.95),60)
            print("club member buyin pass")
        else:
            print("club member buyin error")
            assert False
    else:
        print("can't find club member buyin")
        assert False

# club_member_winnings
def club_member_winnings():                    
    if exists(Pattern("1663750552645.png").similar(0.95),60):
        click(Pattern("1663750552645.png").similar(0.95))
        if exists(Pattern("1663751225156.png").similar(0.95),60):
            click(Pattern("1663751225156.png").similar(0.95))
            assert exists(Pattern("1663751251030.png").similar(0.95),60)
            print("club member winnings pass")
        else:
            print("club member winnings error")
            assert False
    else:
        print("can't find club member winnings")
        assert False

# club_member_hands
def club_member_hands():                    
    if exists(Pattern("1663751251030.png").similar(0.95),60):
        click(Pattern("1663751251030.png").similar(0.95))
        if exists(Pattern("1663751312782.png").similar(0.95),60):
            click(Pattern("1663751312782.png").similar(0.95))
            assert exists(Pattern("1663751356209.png").similar(0.95),60)
            print("club member hands pass")
        else:
            print("club member hands error")
            assert False
    else:
        print("can't find club member hands")
        assert False

# club_member_lastLogin
def club_member_lastLogin():                    
    if exists(Pattern("1663751356209.png").similar(0.95),60):
        click(Pattern("1663751356209.png").similar(0.95))
        if exists(Pattern("1663751442197.png").similar(0.95),60):
            click(Pattern("1663751442197.png").similar(0.95))
            assert exists(Pattern("1663751466728.png").similar(0.95),60)
            print("club member lastLogin pass")
        else:
            print("club member lastLogin error")
            assert False
    else:
        print("can't find club member lastLogin")
        assert False

# club_member_lastPlayed
def club_member_lastPlayed():                    
    if exists(Pattern("1663751466728.png").similar(0.95),60):
        click(Pattern("1663751466728.png").similar(0.95))
        if exists(Pattern("1663751573668.png").similar(0.95),60):
            click(Pattern("1663751573668.png").similar(0.95))
            assert exists(Pattern("1663751606951.png").similar(0.95),60)
            print("club member lastPlayed pass")
        else:
            print("club member lastPlayed error")
            assert False
    else:
        print("can't find club member lastPlayed")
        assert False

# club_member_chipStorm
def club_member_chipStorm():                    
    if exists(Pattern("1663751606951.png").similar(0.95),60):
        click(Pattern("1663751606951.png").similar(0.95))
        if exists(Pattern("1663751674124.png").similar(0.95),60):
            click(Pattern("1663751674124.png").similar(0.95))
            assert exists(Pattern("1663751730151.png").similar(0.95),60)
            print("club member chipStorm pass")
        else:
            print("club member chipStorm error")
            assert False
    else:
        print("can't find club member chipStorm")
        assert False

# club_member_newMember
def club_member_newMember():                    
    if exists(Pattern("1663816944774.png").similar(0.95),60):
        click(Pattern("1663816944774.png").similar(0.95).targetOffset(101,33))
        if exists(Pattern("1663816991770.png").similar(0.95),60):
            click(Pattern("1663816991770.png").similar(0.95).targetOffset(180,-276))
            assert True
            print("club member newMember pass")
        else:
            print("club member newMember error")
            assert False
    else:
        print("can't find club member newMember")
        assert False

# club_counter
def club_counter():                    
    if exists(Pattern("1663753431076.png").similar(0.95),60):
        click(Pattern("1663753431076.png").similar(0.95))
        if exists(Pattern("1663753711632.png").similar(0.90),60):
            print("club counter pass")
            assert True
        else:
            print("club counter error")
            assert False
    else:
        print("can't find club counter")
        assert False

# club_counter_record
def club_counter_record():                    
    if exists(Pattern("1663754836796.png").similar(0.90),60):
        click(Pattern("1663754836796.png").similar(0.90))
        if exists(Pattern("1663754862387.png").similar(0.90),60):
            click(Pattern("1663754862387.png").similar(0.90).targetOffset(181,-36))
            print("club counter record pass")
            assert True
        else:
            print("club counter record error")
            assert False
    else:
        print("can't find club counter record")
        assert False

# club_counter_search
def club_counter_search():                    
    if exists(Pattern("1663755374871.png").similar(0.90),60):
        type(Pattern("1663755374871.png").similar(0.90),"2528075" + Key.ENTER)
        if exists(Pattern("1663755631695.png").similar(0.95),60):
            print("club counter search pass")
            assert True
        else:
            print("club counter search error")
            assert False
    else:
        print("can't find club counter search")
        assert False

# club_counter_sendOut
def club_counter_sendOut():                    
    if exists(Pattern("1663756022391.png").similar(0.90),60):
        click(Pattern("1663756022391.png").similar(0.90))
        if exists(Pattern("1663756048861.png").similar(0.95),60):
            click(Pattern("1663756048861.png").similar(0.95))
            sleep(1)
            assert exists(Pattern("1663756400690.png").similar(0.90),60)
            type(Pattern("1663756290820.png").similar(0.90),"100" + Key.ENTER)
            sleep(1)
            assert exists(Pattern("1663756439062.png").similar(0.95),60)
            click(Pattern("1663756454530.png").similar(0.90))
            assert exists((Pattern("1663756539098.png").similar(0.95))and(Pattern("1663756568813.png").similar(0.95)),60)
            print("club counter sendOut pass")
        else:
            print("club counter sendOut error")
            assert False
    else:
        print("can't find club counter sendOut")
        assert False

# club_counter_claimBack
def club_counter_claimBack():                    
    if exists(Pattern("1663756022391.png").similar(0.90),60):
        click(Pattern("1663756022391.png").similar(0.90))
        if exists(Pattern("1663813718066.png").similar(0.95),60):
            click(Pattern("1663813718066.png").similar(0.95))
            sleep(1)
            assert exists(Pattern("1663813749505.png").similar(0.95),60)
            click(Pattern("1663813749505.png").similar(0.95))
            sleep(1)
            click(Pattern("1663813814481.png").similar(0.95))
            assert exists(Pattern("1663813848558.png").similar(0.95),60)
            click(Pattern("1663756454530.png").similar(0.90))
            assert exists((Pattern("1663813884194.png").similar(0.95))and(Pattern("1663813900502.png").similar(0.95)),60)
            print("club counter claimBack pass")
        else:
            print("club counter claimBack error")
            assert False
    else:
        print("can't find club counter claimBack")
        assert False

# club_counter_ppChip
def club_counter_ppChip():                    
    if exists(Pattern("1663814695121.png").similar(0.95),60):
        click(Pattern("1663814695121.png").similar(0.95))
        if exists(Pattern("1663814724614.png").similar(0.95),60):
            click(Pattern("1663814724614.png").similar(0.95).targetOffset(-29,-25))
            assert exists(Pattern("1663814769938.png").similar(0.95),60)
            print("club counter ppChip pass")
        else:
            print("club counter ppChip error")
            assert False
    else:
        print("can't find club counter ppChip")
        assert False

# club_counter_prizes
def club_counter_prizes():                    
    if exists(Pattern("1663814769938.png").similar(0.95),60):
        click(Pattern("1663814769938.png").similar(0.95))
        if exists(Pattern("1663815067401.png").similar(0.95),60):
            click(Pattern("1663815067401.png").similar(0.95).targetOffset(-18,19))
            assert exists(Pattern("1663815109431.png").similar(0.95),60)
            print("club counter prizes pass")
        else:
            print("club counter prizes error")
            assert False
    else:
        print("can't find club counter prizes")
        assert False

# club_counter_expiryDate
def club_counter_expiryDate():                    
    if exists(Pattern("1663815109431.png").similar(0.95),60):
        click(Pattern("1663815109431.png").similar(0.95))
        if exists(Pattern("1663815210997.png").similar(0.95),60):
            click(Pattern("1663815210997.png").similar(0.95).targetOffset(-36,69))
            assert exists(Pattern("1663815331933.png").similar(0.95),60)
            print("club counter expiryDate pass")
        else:
            print("club counter expiryDate error")
            assert False
    else:
        print("can't find club counter expiryDate")
        assert False

# club_counter_sendItems
def club_counter_sendItems():                    
    if exists(Pattern("1663814238055.png").similar(0.95),60):
        click(Pattern("1663814238055.png").similar(0.95))
        if exists(Pattern("1663815492550.png").similar(0.95),60):
            type(Pattern("1663755374871.png").similar(0.90),"2528075" + Key.ENTER)
            sleep(1)
            click(Pattern("1663756022391.png").similar(0.90))
            sleep(1)
            click(Pattern("1663815617712.png").similar(0.95))
            assert exists(Pattern("1663815838848.png").similar(0.95),60)
            click(Pattern("1663815838848.png").similar(0.95).targetOffset(95,-205))
            assert exists(Pattern("1663815918244.png").similar(0.95),60)
            click(Pattern("1663815942846.png").similar(0.90))
            print("club counter sendItems pass")
        else:
            print("club counter sendItems error")
            assert False
    else:
        print("can't find club counter sendItems")
        assert False

# club_counter_ticket
def club_counter_ticket():                    
    if exists(Pattern("1663816433063.png").similar(0.95),60):
        click(Pattern("1663816433063.png").similar(0.95))
        if exists(Pattern("1663816523848.png").similar(0.95),60):
            click(Pattern("1663816523848.png").similar(0.95).targetOffset(-6,61))
            assert exists((Pattern("1663816589274.png").similar(0.95))and(Pattern("1663816621214.png").similar(0.90)),60)
            click(Pattern("1663816589274.png").similar(0.95).targetOffset(180,-4))
            sleep(1)
            click(Pattern("1663816682221.png").similar(0.90))
            print("club counter ticket pass")
        else:
            print("club counter ticket error")
            assert False
    else:
        print("can't find club counter ticket")
        assert False

# club_data
def club_data():                    
    if exists(Pattern("1663832023272.png").similar(0.90),60):
        click(Pattern("1663832023272.png").similar(0.90))
        if exists(Pattern("1663832194992.png").similar(0.90),60):
            print("club data pass")
            assert True
        else:
            print("club data error")
            assert False
    else:
        print("can't find club data")
        assert False

# club_data_excel
def club_data_excel():                    
    if exists(Pattern("1663832388580.png").similar(0.90),60):
        click(Pattern("1663832388580.png").similar(0.90))
        if exists(Pattern("1663832429172.png").similar(0.90),60):
            #club data excel date
            if exists(Pattern("1663832585910.png").similar(0.90),60):
                click(Pattern("1663832585910.png").similar(0.90))
                assert exists(Pattern("1663832628637.png").similar(0.90),60)
                click(Pattern("1663832628637.png").similar(0.90).targetOffset(-173,-18))
                print("club data excel date pass")
            else:
                print("club data excel date error")
                assert False
            #club data excel mail
            if exists(Pattern("1663834359576.png").similar(0.90),60):
                click(Pattern("1663834359576.png").similar(0.90))
                assert exists(Pattern("1663834389682.png").similar(0.80),60)
                click(Pattern("1663834406532.png").similar(0.90))
                print("club data excel mail pass")
            else:
                print("club data excel mail error")
                assert False 
            #club data excel export
            if exists(Pattern("1663834912922.png").similar(0.90),60):
                click(Pattern("1663834912922.png").similar(0.90))
                assert exists(Pattern("1663834943107.png").similar(0.90),60)
                print("club data excel export pass")
            else:
                print("club data excel export error")
                assert False
            #club data excel exportRecord
            if exists(Pattern("1663835084970.png").similar(0.90),60):
                click(Pattern("1663835084970.png").similar(0.90))
                assert exists(Pattern("1663835109599.png").similar(0.90),60)
                click(Pattern("1663835109599.png").similar(0.90).targetOffset(178,-37))
                print("club data excel exportRecord pass")
            else:
                print("club data excel exportRecord error")
                assert False 
        else:
            print("club data error")
            assert False
    else:
        print("can't find club data")
        assert False

# club_data_dateArrow
def club_data_dateArrow():                    
    if exists(Pattern("1663835650617.png").similar(0.90),60):
        click(Pattern("1663835650617.png").similar(0.90))
        if exists((Pattern("1663835709945.png").similar(0.90))and(Pattern("1663835650617.png").similar(0.90)),60):
            click(Pattern("1663835709945.png").similar(0.90))
            assert exists(Pattern("1663835885309.png").similar(0.90),60)
            print("club counter dateArrow pass")
        else:
            print("club counter dateArrow error")
            assert False
    else:
        print("can't find club counter dateArrow")
        assert False

# club_data_yesterday
def club_data_yesterday():                    
    if exists(Pattern("1663836384806.png").similar(0.90),60):
        click(Pattern("1663836384806.png").similar(0.90))
        if exists((Pattern("1663835709945.png").similar(0.90))and(Pattern("1663835650617.png").similar(0.90)),60):
            print("club counter yesterday pass")
            assert True
        else:
            print("club counter yesterday error")
            assert False
    else:
        print("can't find club counter yesterday")
        assert False

# club_data_lastSevenDay
def club_data_lastSevenDay():                    
    if exists(Pattern("1663836789155.png").similar(0.90),60):
        click(Pattern("1663836789155.png").similar(0.90))
        if exists((Pattern("1663836872885.png").similar(0.90))and(Pattern("1663835885309.png").similar(0.90)),60):
            print("club counter lastSevenDay pass")
            assert True
        else:
            print("club counter lastSevenDay error")
            assert False
    else:
        print("can't find club counter lastSevenDay")
        assert False

# club_data_select
def club_data_select():                    
    if exists(Pattern("1663837107602.png").similar(0.90),60):
        click(Pattern("1663837107602.png").similar(0.90))
        if exists(Pattern("1663837163832.png").similar(0.90),60):
            click(Pattern("1663837163832.png").similar(0.90).targetOffset(-173,-19))
            print("club counter select pass")
            assert True
        else:
            print("club counter select error")
            assert False
    else:
        print("can't find club counter select")
        assert False

# club_data_category
def club_data_category():
    #NLH
    if exists(Pattern("1663837457410.png").similar(0.90),60):
        click(Pattern("1663837457410.png").similar(0.90))
        assert exists(Pattern("1663837524184.png").similar(0.90),60)
        print("club counter category NLH pass")
    else:
        print("can't find club counter category NLH")
        assert False
    #PLO5
    if exists(Pattern("1663837742662.png").similar(0.90),60):
        click(Pattern("1663837742662.png").similar(0.90))
        assert exists(Pattern("1663837766516.png").similar(0.90),60)
        print("club counter category PLO5 pass")
    else:
        print("can't find club counter category PLO5")
        assert False
    #MTT
    if exists(Pattern("1663837814139.png").similar(0.90),60):
        click(Pattern("1663837814139.png").similar(0.90))
        assert exists(Pattern("1663837834167.png").similar(0.90),60)
        print("club counter category MTT pass")
    else:
        print("can't find club counter category MTT")
        assert False
    #PLO4
    if exists(Pattern("1663837860741.png").similar(0.90),60):
        click(Pattern("1663837860741.png").similar(0.90))
        assert exists(Pattern("1663837881806.png").similar(0.90),60)
        print("club counter category PLO4 pass")
    else:
        print("can't find club counter category PLO4")
        assert False
    #PLO6
    if exists(Pattern("1663837976773.png").similar(0.90),60):
        click(Pattern("1663837976773.png").similar(0.90).targetOffset(44,-1))
        assert exists(Pattern("1663838011514.png").similar(0.90),60)
        print("club counter category PLO6 pass")
    else:
        print("can't find club counter category PLO6")
        assert False
    #SpinUp
    if exists(Pattern("1663838065100.png").similar(0.90),60):
        click(Pattern("1663838065100.png").similar(0.90))
        assert exists(Pattern("1663838088392.png").similar(0.90),60)
        print("club counter category SpinUp pass")
    else:
        print("can't find club counter category SpinUp")
        assert False
    #6+
    if exists(Pattern("1663838128672.png").similar(0.90),60):
        click(Pattern("1663838128672.png").similar(0.90))
        assert exists(Pattern("1663838150724.png").similar(0.90),60)
        print("club counter category 6+ pass")
    else:
        print("can't find club counter category 6+")
        assert False
    #6+
    if exists(Pattern("1663838175116.png").similar(0.90),60):
        click(Pattern("1663838175116.png").similar(0.90))
        assert exists(Pattern("1663838193356.png").similar(0.90),60)
        print("club counter category 6+ pass")
    else:
        print("can't find club counter category 6+")
        assert False
    #OFC
    if exists(Pattern("1663838226718.png").similar(0.90),60):
        click(Pattern("1663838226718.png").similar(0.90))
        assert exists(Pattern("1663838250396.png").similar(0.90),60)
        print("club counter category OFC pass")
    else:
        print("can't find club counter category OFC")
        assert False
    #AoF
    if exists(Pattern("1663838274615.png").similar(0.90),60):
        click(Pattern("1663838274615.png").similar(0.90))
        assert exists(Pattern("1663838293766.png").similar(0.90),60)
        print("club counter category AoF pass")
    else:
        print("can't find club counter category AoF")
        assert False
    #SNG
    if exists(Pattern("1663838329377.png").similar(0.90),60):
        click(Pattern("1663838329377.png").similar(0.90))
        assert exists(Pattern("1663838352287.png").similar(0.90),60)
        print("club counter category SNG pass")
    else:
        print("can't find club counter category SNG")
        assert False
    #PLO H/L
    if exists(Pattern("1663838403333.png").similar(0.90),60):
        click(Pattern("1663838403333.png").similar(0.90))
        assert exists(Pattern("1663838430853.png").similar(0.90),60)
        print("club counter category PLO H/L pass")
    else:
        print("can't find club counter category PLO H/L")
        assert False
    #NLH&PLO
    if exists(Pattern("1663838476139.png").similar(0.90),60):
        click(Pattern("1663838476139.png").similar(0.90))
        assert exists(Pattern("1663838496587.png").similar(0.90),60)
        print("club counter category NLH&PLO pass")
    else:
        print("can't find club counter category NLH&PLO")
        assert False
    #NLH&PLO
    if exists(Pattern("1663838518220.png").similar(0.90),60):
        click(Pattern("1663838518220.png").similar(0.90))
        assert exists(Pattern("1663838539887.png").similar(0.90),60)
        print("club counter category NLH&PLO pass")
    else:
        print("can't find club counter category NLH&PLO")
        assert False
    sleep(1)
    click(Pattern("1663838586044.png").similar(0.90))

# club_admin
def club_admin():                    
    if exists(Pattern("1663839986239.png").similar(0.90),60):
        click(Pattern("1663839986239.png").similar(0.90))
        if exists((Pattern("1663840008311.png").similar(0.90))and(Pattern("1663840032907.png").similar(0.90)),60):
            print("club admin pass")
            assert True
        else:
            print("club admin error")
            assert False
    else:
        print("can't find club admin")
        assert False

# club_admin_notifications
def club_admin_notifications():                    
    if exists(Pattern("1663840156041.png").similar(0.90),60):
        click(Pattern("1663840156041.png").similar(0.90))
        if exists(Pattern("1663840189999.png").similar(0.90),60):
            #QA
            if exists(Pattern("1663840387883.png").similar(0.90),60):
                click(Pattern("1663840387883.png").similar(0.90))
                assert exists(Pattern("1663840472745.png").similar(0.90),60)
                click(Pattern("1663840472745.png").similar(0.90).targetOffset(182,-149))
                print("club admin notifications QA pass")
            else:
                print("club admin notifications QA pass")
                assert False
            #image 
            if exists(Pattern("1663840730020.png").similar(0.90),60):
                click(Pattern("1663840730020.png").similar(0.90))
                assert exists(Pattern("1663840764492.png").similar(0.90),60)
                click(Pattern("1663840764492.png").similar(0.90).targetOffset(0,-17))
                assert exists(Pattern("1663840832341.png").similar(0.90),60)
                click(Pattern("1663840832341.png").similar(0.90).targetOffset(123,33))
                print("club admin notifications image pass")
            else:
                print("club admin notifications image pass")
                assert False 
            #image end time
            if exists(Pattern("1663840947838.png").similar(0.90),60):
                click(Pattern("1663840947838.png").similar(0.90))
                assert exists(Pattern("1663840993635.png").similar(0.90),60)
                sleep(1)
                click(Pattern("1663840993635.png").similar(0.90).targetOffset(-182,3))
                print("club admin notifications image end time pass")
            else:
                print("club admin notifications image end time pass")
                assert False   
            #image send
            if exists(Pattern("1663841096309.png").similar(0.90),60):
                click(Pattern("1663841096309.png").similar(0.90))
                assert exists(Pattern("1663841120900.png").similar(0.90),60)
                print("club admin notifications image send pass")
            else:
                print("club admin notifications image send pass")
                assert False
            #text
            if exists(Pattern("1663841166098.png").similar(0.90),60):
                click(Pattern("1663841166098.png").similar(0.90))
                assert exists(Pattern("1663841209952.png").similar(0.90),60)
                click(Pattern("1663841303043.png").similar(0.90))
                assert exists(Pattern("1663841327934.png").similar(0.90),60)
                click(Pattern("1663841354199.png").similar(0.90))
                print("club admin notifications text pass")
            else:
                print("club admin notifications text pass")
                assert False
            #text end time
            if exists(Pattern("1663840947838.png").similar(0.90),60):
                click(Pattern("1663840947838.png").similar(0.90))
                assert exists(Pattern("1663840993635.png").similar(0.90),60)
                sleep(1)
                click(Pattern("1663840993635.png").similar(0.90).targetOffset(-182,3))
                print("club admin notifications text end time pass")
            else:
                print("club admin notifications text end time pass")
                assert False   
            #text send
            if exists(Pattern("1663841096309.png").similar(0.90),60):
                click(Pattern("1663841096309.png").similar(0.90))
                assert exists(Pattern("1663841120900.png").similar(0.90),60)
                print("club admin notifications text send pass")
            else:
                print("club admin notifications text send pass")
                assert False
            #exit
            if exists(Pattern("1663841490888.png").similar(0.90),60):
                click(Pattern("1663841490888.png").similar(0.90))
                assert exists(Pattern("1663841512110.png").similar(0.90),60)
                click(Pattern("1663841512110.png").similar(0.90).targetOffset(2,145))
                print("club admin notifications exit pass")
            else:
                print("club admin notifications exit pass")
                assert False                
        else:
            print("club admin notifications error")
            assert False
    else:
        print("can't find club admin notifications")
        assert False

# club_admin_clubRating
def club_admin_clubRating():                    
    if exists(Pattern("1663841619059.png").similar(0.90),60):
        click(Pattern("1663841619059.png").similar(0.90))
        if exists((Pattern("1663841648126.png").similar(0.90))and(Pattern("1663841662560.png").similar(0.90)),60):
            #sale
            if exists(Pattern("1663317989566.png").similar(0.90),60):
                click(Pattern("1663317989566.png").similar(0.90))
                assert exists(Pattern("1663318022327.png").similar(0.90),60)
                click(Pattern("1663318054998.png").similar(0.90))
                print("club league create sale pass")
            else:
                print("club league create sale error")
                assert False
            #1 star
            if exists(Pattern("1663842295110.png").similar(0.90),60):
                click(Pattern("1663842295110.png").similar(0.90))
                assert exists(Pattern("1663842316832.png").similar(0.90),60)
                click(Pattern("1663842316832.png").similar(0.90).targetOffset(184,-152))
                print("1 star pass")
            else:
                print("1 star error")
                assert False
            #2 star
            if exists(Pattern("1663821760059.png").similar(0.90),60):
                click(Pattern("1663821760059.png").similar(0.90))
                assert exists(Pattern("1663318469574.png").similar(0.95),60)
                click(Pattern("1663318469574.png").similar(0.95).targetOffset(182,-149))
                print("2 star pass")
            else:
                print("2 star error")
                assert False
            #3 star
            if exists(Pattern("1663830760556.png").similar(0.90),60):
                click(Pattern("1663830760556.png").similar(0.90))
                assert exists(Pattern("1663318759198.png").similar(0.95),60)
                click(Pattern("1663318759198.png").similar(0.95).targetOffset(183,-151))
                print("3 star pass")
            else:
                print("3 star error")
                assert False
            #4 star
            if exists(Pattern("1663830790483.png").similar(0.90),60):
                click(Pattern("1663830790483.png").similar(0.90))
                assert exists(Pattern("1663318916711.png").similar(0.95).targetOffset(184,-152),60)
                click(Pattern("1663318916711.png").similar(0.95).targetOffset(184,-152))
                print("4 star pass")
            else:
                print("4 star error")
                assert False
            # switch lv5
            sleep(1)
            dragDrop(Pattern("1663830790483.png").similar(0.90),Pattern("1663842295110.png").similar(0.90))
            sleep(1)
            #5 star
            if exists(Pattern("1663830817150.png").similar(0.90),60):
                click(Pattern("1663830817150.png").similar(0.90))
                assert exists(Pattern("1663320085097.png").similar(0.95),60)
                click(Pattern("1663320085097.png").similar(0.95).targetOffset(180,-151))
                print("5 star pass")
            else:
                print("5 star error")
                assert False
            # 6 star
            if exists(Pattern("1663830882979.png").similar(0.90),60):
                click(Pattern("1663830882979.png").similar(0.90))
                assert exists(Pattern("1663659749986.png").similar(0.95),60)
                click(Pattern("1663659749986.png").similar(0.95).targetOffset(182,-151))
                print("6 star pass")
            else:
                print("6 star error")
                assert False
            #7 star
            if exists(Pattern("1663830911529.png").similar(0.90),60):
                click(Pattern("1663830911529.png").similar(0.90))
                assert exists(Pattern("1663660486242.png").similar(0.95),60)
                click(Pattern("1663660486242.png").similar(0.95).targetOffset(183,-151))
                print("7 star pass")
            else:
                print("7 star error")
                assert False
            # switch lv10
            sleep(1)
            dragDrop(Pattern("1663830911529.png").similar(0.90),Pattern("1663830790483.png").similar(0.90))
            sleep(1)
            # 8 star
            if exists(Pattern("1663830932339.png").similar(0.90),60):
                click(Pattern("1663830932339.png").similar(0.90))
                assert exists(Pattern("1663661260722.png").similar(0.95),60)
                click(Pattern("1663661260722.png").similar(0.95).targetOffset(181,-153))
                print("8 star pass")
            else:
                print("8 star error")
                assert False
            #9 star
            if exists(Pattern("1663831001643.png").similar(0.90),60):
                click(Pattern("1663831001643.png").similar(0.90))
                assert exists(Pattern("1663661473162.png").similar(0.95),60)
                click(Pattern("1663661473162.png").similar(0.95).targetOffset(182,-151))
                print("9 star pass")
            else:
                print("9 star error")
                assert False
            #10 star
            if exists(Pattern("1663831022380.png").similar(0.90),60):
                click(Pattern("1663831022380.png").similar(0.90))
                assert exists(Pattern("1663661740242.png").similar(0.95),60)
                click(Pattern("1663661740242.png").similar(0.95).targetOffset(182,-152))
                print("10 star pass")
            else:
                print("10 star error")
                assert False
            sleep(1)
            click(Pattern("1663662834877.png").similar(0.90))
        else:
            print("club admin error")
            assert False
    else:
        print("can't find club admin")
        assert False

# club_admin_backpack
def club_admin_backpack():                    
    if exists(Pattern("1663842820035.png").similar(0.90),60):
        click(Pattern("1663842820035.png").similar(0.90))
        if exists(Pattern("1663842858596.png").similar(0.90),60):
            click(Pattern("1663842858596.png").similar(0.90).targetOffset(179,-2))
            print("club admin backpack pass")
            assert True
        else:
            print("club admin backpack error")
            assert False
    else:
        print("can't find club admin backpack")
        assert False

# club_admin_jackpot
def club_admin_jackpot():                    
    if exists(Pattern("1663901054544.png").similar(0.90),60):
        click(Pattern("1663901054544.png").similar(0.90))
        if exists(Pattern("1663901087323.png").similar(0.90),60):
            #top up
            if exists(Pattern("1663903152004.png").similar(0.90),60):
                click(Pattern("1663903152004.png").similar(0.90))
                assert exists((Pattern("1663903503276.png").similar(0.90))and(Pattern("1663903527929.png").similar(0.90)),60)
                click(Pattern("1663903503276.png").similar(0.90).targetOffset(101,30))
                assert exists(Pattern("1663903671427.png").similar(0.90),60)
                print("club admin jackpot top up pass")
                click(Pattern("1663903671427.png").similar(0.90).targetOffset(179,-35))
            else:
                print("club admin jackpot top up error")
                assert False
            #mixed jackpot
            if exists(Pattern("1663904037590.png").similar(0.90),60):
                click(Pattern("1663904037590.png").similar(0.90).targetOffset(61,1))
                assert exists(Pattern("1663904085778.png").similar(0.90),60)
                click(Pattern("1663904085778.png").similar(0.90).targetOffset(0,-216))
                assert exists(Pattern("1663904193344.png").similar(0.90),60)
                click(Pattern("1663904193344.png").similar(0.90).targetOffset(127,-217))
                assert exists(Pattern("1663904256660.png").similar(0.90),60)
                click(Pattern("1663904256660.png").similar(0.90).targetOffset(179,-282))
                sleep(1)
                click(Pattern("1663904330688.png").similar(0.90).targetOffset(155,2))
                assert exists((Pattern("1663903503276.png").similar(0.90))and(Pattern("1663903527929.png").similar(0.90)),60)
                click(Pattern("1663903503276.png").similar(0.90).targetOffset(101,30))
                assert exists(Pattern("1663903671427.png").similar(0.90),60)
                print("club admin jackpot mixed jackpot pass")
                click(Pattern("1663903671427.png").similar(0.90).targetOffset(179,-35))
            else:
                print("club admin jackpot mixed jackpot error")
                assert False
            #cooler jackpot
            if exists(Pattern("1663904522505.png").similar(0.90),60):
                click(Pattern("1663904522505.png").similar(0.90).targetOffset(61,2))
                assert exists(Pattern("1663904556811.png").similar(0.90),60)
                click(Pattern("1663904556811.png").similar(0.90).targetOffset(-4,-217))
                assert exists(Pattern("1663904584351.png").similar(0.90).targetOffset(127,-217),60)
                click(Pattern("1663904584351.png").similar(0.90).targetOffset(127,-217))
                assert exists(Pattern("1663904626352.png").similar(0.90).targetOffset(177,-279),60)
                click(Pattern("1663904256660.png").similar(0.90).targetOffset(179,-282))
                sleep(1)
                click(Pattern("1663904658464.png").similar(0.90).targetOffset(155,1))
                assert exists((Pattern("1663903503276.png").similar(0.90))and(Pattern("1663903527929.png").similar(0.90)),60)
                click(Pattern("1663903503276.png").similar(0.90).targetOffset(101,30))
                assert exists(Pattern("1663903671427.png").similar(0.90),60)
                print("club admin jackpot cooler jackpot pass")
                click(Pattern("1663903671427.png").similar(0.90).targetOffset(179,-35))
            else:
                print("club admin jackpot cooler jackpot error")
                assert False
            #cooler jackpot plus
            if exists(Pattern("1663904753160.png").similar(0.90).targetOffset(78,-1),60):
                click(Pattern("1663904753160.png").similar(0.90).targetOffset(78,-1))
                assert exists(Pattern("1663904781528.png").similar(0.90).targetOffset(-4,-214),60)
                click(Pattern("1663904781528.png").similar(0.90).targetOffset(-4,-214))
                assert exists(Pattern("1663904810681.png").similar(0.90).targetOffset(126,-216),60)
                click(Pattern("1663904810681.png").similar(0.90).targetOffset(126,-216))
                assert exists(Pattern("1663904835114.png").similar(0.90).targetOffset(180,-280),60)
                click(Pattern("1663904835114.png").similar(0.90).targetOffset(180,-280))
                sleep(1)
                click(Pattern("1663904860029.png").similar(0.90).targetOffset(149,0))
                assert exists((Pattern("1663903503276.png").similar(0.90))and(Pattern("1663903527929.png").similar(0.90)),60)
                click(Pattern("1663903503276.png").similar(0.90).targetOffset(101,30))
                assert exists(Pattern("1663903671427.png").similar(0.90),60)
                print("club admin jackpot cooler jackpot plus pass")
                click(Pattern("1663903671427.png").similar(0.90).targetOffset(179,-35))
            else:
                print("club admin jackpot cooler jackpot plus error")
                assert False
            sleep(1)
            click(Pattern("1663904916084.png").similar(0.90).targetOffset(179,-3))    
        else:
            print("club admin backpack error")
            assert False
    else:
        print("can't find club admin backpack")
        assert False

# club_admin_event
def club_admin_event():                    
    if exists(Pattern("1663905404296.png").similar(0.90),60):
        click(Pattern("1663905404296.png").similar(0.90))
        if exists(Pattern("1663905471294.png").similar(0.90),60):
            #QA
            if exists(Pattern("1663905508985.png").similar(0.90),60):
                click(Pattern("1663905508985.png").similar(0.90))
                assert exists(Pattern("1663905563164.png").similar(0.90),60)
                click(Pattern("1663905563164.png").similar(0.90).targetOffset(181,-151))
                print("club admin event QA pass")
            else:
                print("club admin event QA error")
                assert False
            #chip storm
            if exists(Pattern("1663905777925.png").similar(0.90),60):
                click(Pattern("1663905777925.png").similar(0.90))
                assert exists(Pattern("1663916055112.png").similar(0.90),60)
                click(Pattern("1663916055112.png").similar(0.90).targetOffset(0,-176))
                assert exists(Pattern("1663916124448.png").similar(0.90),60)
                click(Pattern("1663916124448.png").similar(0.90).targetOffset(180,-308))
                print("club admin event chip storm pass")
            else:
                print("club admin event chip storm error")
                assert False
            #ring game
            if exists(Pattern("1663905777925.png").similar(0.90),60):
                click(Pattern("1663905777925.png").similar(0.90))
                assert exists(Pattern("1663916055112.png").similar(0.90),60)
                click(Pattern("1663916055112.png").similar(0.90).targetOffset(8,-52))
                assert exists(Pattern("1663916233195.png").similar(0.90),60)
                click(Pattern("1663916233195.png").similar(0.90).targetOffset(181,-309))
                print("club admin event ring game pass")
            else:
                print("club admin event ring game error")
                assert False
            #customized rg
            if exists(Pattern("1663905777925.png").similar(0.90),60):
                click(Pattern("1663905777925.png").similar(0.90))
                assert exists(Pattern("1663916055112.png").similar(0.90),60)
                click(Pattern("1663916055112.png").similar(0.90).targetOffset(3,62))
                assert exists(Pattern("1663917431063.png").similar(0.90),60)
                click(Pattern("1663917431063.png").similar(0.90).targetOffset(182,-311))
                print("club admin event customized rg pass")
            else:
                print("club admin event customized rg error")
                assert False
            #mtt
            if exists(Pattern("1663905777925.png").similar(0.90),60):
                click(Pattern("1663905777925.png").similar(0.90))
                assert exists(Pattern("1663916055112.png").similar(0.90),60)
                click(Pattern("1663916055112.png").similar(0.90).targetOffset(9,176))
                assert exists(Pattern("1663917508177.png").similar(0.90),60)
                click(Pattern("1663917508177.png").similar(0.90).targetOffset(184,-308))
                print("club admin event mtt pass")
            else:
                print("club admin event mtt error")
                assert False
            #template
            if exists(Pattern("1663905777925.png").similar(0.90),60):
                click(Pattern("1663905777925.png").similar(0.90))
                assert exists(Pattern("1663916055112.png").similar(0.90),60)
                click(Pattern("1663916055112.png").similar(0.90).targetOffset(-3,278))
                assert exists(Pattern("1663917583028.png").similar(0.90),60)
                click(Pattern("1663917583028.png").similar(0.90).targetOffset(183,-1))
                print("club admin event template pass")
            else:
                print("club admin event template error")
                assert False
            #record
            if exists(Pattern("1663920933005.png").similar(0.90),60):
                click(Pattern("1663920933005.png").similar(0.90))
                assert exists(Pattern("1663920954858.png").similar(0.90),60)
                print("club admin event record pass")
            else:
                print("club admin event record error")
                assert False
            sleep(1)
            click(Pattern("1663917658434.png").similar(0.90))    
        else:
            print("club admin event error")
            assert False
    else:
        print("can't find club event backpack")
        assert False

# club_admin_preferences
def club_admin_preferences():                    
    if exists(Pattern("1663917886548.png").similar(0.90),60):
        click(Pattern("1663917886548.png").similar(0.90))
        #classic
        if exists(Pattern("1663917915790.png").similar(0.90),60):
            click(Pattern("1663917915790.png").similar(0.90).targetOffset(148,-149))
            sleep(1)
            click(Pattern("1663917915790.png").similar(0.90).targetOffset(24,176))
            sleep(1)
            click(Pattern("1663917915790.png").similar(0.90).targetOffset(178,-228))
            assert exists(Pattern("1663918076144.png").similar(0.90),60)
            print("club admin preferences classic pass")
        else:
            print("club admin preferences classic error")
            assert False
        #listed
        function_club.club_admin()
        sleep(1)
        click(Pattern("1663917886548.png").similar(0.90))
        if exists(Pattern("1663918709842.png").similar(0.90),60):
            click(Pattern("1663918709842.png").similar(0.90).targetOffset(146,-151))
            sleep(1)
            click(Pattern("1663918709842.png").similar(0.90).targetOffset(-100,106))
            sleep(1)
            click(Pattern("1663918709842.png").similar(0.90).targetOffset(180,-229))
            assert exists("1663918783715.png",60)
            print("club admin preferences listed pass")
        else:
            print("club admin preferences listed error")
            assert False
    else:
        print("can't find club admin preferences")
        assert False

# club_admin_disband
def club_admin_disband():                    
    if exists(Pattern("1663918898760.png").similar(0.90).targetOffset(13,37),60):
        click(Pattern("1663918898760.png").similar(0.90).targetOffset(13,37))
        if exists(Pattern("1663918937377.png").similar(0.90).targetOffset(179,-149),60):
            click(Pattern("1663918937377.png").similar(0.90).targetOffset(179,-149))
            print("club admin disband pass")
            sleep(1)
            click(Pattern("1663918997181.png").similar(0.90))
            assert True
        else:
            print("club admin disband error")
            assert False
    else:
        print("can't find club admin disband")
        assert False













