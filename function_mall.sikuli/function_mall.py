from sikuli import *

### mall_props ###
# mall_props recommend electronic playground card table
def props_recommend_electronicPlaygroundCardTable(): 
    if exists(Pattern("1661328071224.png").similar(0.90),60):
        click(Pattern("1661333734134.png").similar(0.90).targetOffset(2,85))
        sleep(1)
        assert exists(Pattern("1661333673052.png").similar(0.90).targetOffset(181,-305))
        click(Pattern("1661333673052.png").targetOffset(181,-305))
        sleep(1)
        print("electronic playground card table pass")
    else:
        print("electronic playground card table error")
        assert False

# mall_props recommend electronic playground card
def props_recommend_electronicPlaygroundCard():         
    if exists(Pattern("1661333812123.png").similar(0.90).targetOffset(0,85),60):
        click(Pattern("1661333812123.png").similar(0.90).targetOffset(0,85))
        sleep(1)
        assert exists(Pattern("1661333851663.png").similar(0.90).targetOffset(181,-153))
        click(Pattern("1661333851663.png").targetOffset(181,-153))
        sleep(1)
        print("electronic playground card pass")
    else:
        print("electronic playground card error")
        assert False

# mall_props recommend 6M gold coin
def props_recommend_6MGoldCoin():         
    if exists(Pattern("1662016272424.png").similar(0.90),60):
        click(Pattern("1662016272424.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662016300252.png").similar(0.90).targetOffset(182,-152))
        click(Pattern("1662016300252.png").targetOffset(182,-152))
        sleep(1)
        print("6M gold coin pass")
    else:
        print("6M gold coin error")
        assert False

# mall_props VIP silver card
def props_vip_silverCard():             
    if exists(Pattern("1662017007399.png").similar(0.90),60):
        click(Pattern("1662017007399.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662017031314.png").similar(0.90).targetOffset(182,-307))
        click(Pattern("1662017031314.png").targetOffset(182,-307))
        sleep(1)
        print("VIP silver card pass")
    else:
        print("VIP silver card error")
        assert False

# mall_props VIP black card
def props_vip_blackCard():             
    if exists(Pattern("1662017379995.png").similar(0.90),60):
        click(Pattern("1662017379995.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662017464675.png").similar(0.90).targetOffset(182,-304))
        click(Pattern("1662017464675.png").targetOffset(182,-304))
        sleep(1)
        print("VIP black card pass")
    else:
        print("VIP black card error")
        assert False

# mall_props VIP platinum card
def props_vip_platinumCard():                     
    if exists(Pattern("1662017654692.png").similar(0.90),60):
        click(Pattern("1662017654692.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662017675624.png").similar(0.90).targetOffset(178,-306))   
        click(Pattern("1662017675624.png").targetOffset(178,-306))
        sleep(1)
        print("VIP platinum card pass")
    else:
        print("VIP platinum card error")
        assert False

# mall_props coin 6M gold coin
def props_coin_6MGoldCoin():                     
    if exists(Pattern("1662016272424.png").similar(0.90),60):
        click(Pattern("1662016272424.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662016300252.png").similar(0.90).targetOffset(182,-152))
        click(Pattern("1662016300252.png").targetOffset(182,-152))
        sleep(1)
        print("6M gold coin pass")
    else:
        print("6M gold coin error")
        assert False

# mall_props coin 33M gold coin
def props_coin_33MGoldCoin():                             
    if exists(Pattern("1662018913450.png").similar(0.90),60):
        click(Pattern("1662018913450.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662018931431.png").similar(0.90).targetOffset(182,-152))
        click(Pattern("1662018931431.png").targetOffset(182,-152))
        sleep(1)
        print("33M gold coin pass")
    else:
        print("33M gold coin error")
        assert False

# mall_props coin 78M gold coin
def props_coin_78MGoldCoin():                             
    if exists(Pattern("1662019207929.png").similar(0.90),60):
        click(Pattern("1662019207929.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662019225166.png").similar(0.90).targetOffset(181,-152))
        click(Pattern("1662019225166.png").targetOffset(181,-152))
        sleep(1)
        print("78M gold coin pass")
    else:
        print("78M gold coin error")
        assert False

# mall_props coin 148M gold coin
def props_coin_148MGoldCoin():                                     
    if exists(Pattern("1662019275460.png").similar(0.90),60):
        click(Pattern("1662019275460.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662019290235.png").similar(0.90).targetOffset(181,-152))
        click(Pattern("1662019290235.png").targetOffset(181,-152))
        sleep(1)
        print("148M gold coin pass")
    else:
        print("148M gold coin error")
        assert False

# mall_props coin 388M gold coin
def props_coin_388MGoldCoin():                                             
    if exists(Pattern("1662019488352.png").similar(0.90),60):
        click(Pattern("1662019488352.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662019503726.png").similar(0.90).targetOffset(181,-153))
        click(Pattern("1662019503726.png").targetOffset(181,-153))
        sleep(1)
        print("388M gold coin pass")
    else:
        print("388M gold coin error")
        assert False

# mall_props coin 768M gold coin
def props_coin_768MGoldCoin():                                                     
    if exists(Pattern("1662019539203.png").similar(0.90),60):
        click(Pattern("1662019539203.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662019556484.png").similar(0.90).targetOffset(180,-149))
        click(Pattern("1662019556484.png").targetOffset(180,-149))
        sleep(1)
        print("768M gold coin pass")
    else:
        print("768M gold coin error")
        assert False

# mall_props featured props mi river card
def props_featured_miRiverCard():                                                     
    if exists("1662019901399.png",60):
        click("1662019901399.png")
        sleep(1)
        assert exists(Pattern("1662019918130.png").targetOffset(181,-155))
        click(Pattern("1662019918130.png").targetOffset(181,-155))
        sleep(1)
        print("mi river card pass")
    else:
        print("mi river card error")
        assert False

# mall_props featured props time bank
def props_featured_timeBank():                                                             
    if exists("1662020014216.png",60):
        click("1662020014216.png")
        sleep(1)
        assert exists(Pattern("1662020050010.png").targetOffset(179,-149))
        click(Pattern("1662020050010.png").targetOffset(179,-149))
        sleep(1)
        print("time bank pass")
    else:
        print("time bank error")
        assert False

# mall_props featured props community card
def props_featured_communityCard():                                                             
    if exists("1662020094404.png",60):
        click("1662020094404.png")
        sleep(1)
        assert exists(Pattern("1662020123406.png").targetOffset(181,-151))
        click(Pattern("1662020123406.png").targetOffset(181,-151))
        sleep(1)
        print("community card pass")
    else:
        print("community card error")
        assert False

# mall_props featured props halloween emoji
def props_featured_halloweenEmoji():                                                             
    if exists("1662020241003.png",60):
        click("1662020241003.png")
        sleep(1)
        assert exists(Pattern("1662020259826.png").targetOffset(178,-151))
        click(Pattern("1662020259826.png").targetOffset(178,-151))
        sleep(1)
        print("halloween emoji pass")
    else:
        print("halloween emoji error")
        assert False

# mall_props featured props shark emoji
def props_featured_sharkEmoji():                                                             
    if exists("1662020458802.png",60):
        click("1662020458802.png")
        sleep(1)
        assert exists(Pattern("1662020481514.png").targetOffset(181,-148))
        click(Pattern("1662020481514.png").targetOffset(181,-148))
        sleep(1)
        print("shark emoji pass")
    else:
        print("shark emoji error")
        assert False

# mall_props featured props joker emoji
def props_featured_jokerEmoji():                                                             
    if exists("1662020609320.png",60):
        click("1662020609320.png")
        sleep(1)
        assert exists(Pattern("1662020636188.png").targetOffset(181,-148))
        click(Pattern("1662020636188.png").targetOffset(181,-148))
        sleep(1)
        print("joker emoji pass")
    else:
        print("joker emoji error")
        assert False

# mall_props featured props king emoji
def props_featured_kingEmoji():                                                             
    if exists("1662022032985.png",60):
        click("1662022032985.png")
        sleep(1)
        assert exists(Pattern("1662022051152.png").targetOffset(178,-150))
        click(Pattern("1662022051152.png").targetOffset(178,-150))
        sleep(1)
        print("king emoji pass")
    else:
        print("king emoji error")
        assert False

# mall_props featured props yellow face emoji
def props_featured_yellowFaceEmoji():                                                             
    if exists("1662022105925.png",60):
        click("1662022105925.png")
        sleep(1)
        assert exists(Pattern("1662022121040.png").targetOffset(180,-152))
        click(Pattern("1662022121040.png").targetOffset(180,-152))
        sleep(1)
        print("yellow face emoji pass")
    else:
        print("yellow face error")
        assert False

# mall_props featured props little shark emoji
def props_featured_littleSharkEmoji():                                                             
    if exists("1662022398860.png",60):
        click("1662022398860.png")
        sleep(1)
        assert exists(Pattern("1662022418634.png").targetOffset(178,-151))
        click(Pattern("1662022418634.png").targetOffset(178,-151))
        sleep(1)
        print("little shark emoji pass")
    else:
        print("little shark error")
        assert False

# mall_props featured props general emoji
def props_featured_generalEmoji():                                                             
    if exists("1662022487353.png",60):
        click("1662022487353.png")
        sleep(1)
        assert exists(Pattern("1662022515633.png").targetOffset(179,-148))
        click(Pattern("1662022515633.png").targetOffset(179,-148))
        sleep(1)
        print("general emoji pass")
    else:
        print("general emoji error")
        assert False

# mall_props featured props circus card table
def props_featured_circusCardTable():                                                             
    if exists(Pattern("1662022578117.png").similar(0.90),60):
        click(Pattern("1662022578117.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662022601417.png").similar(0.90).targetOffset(180,-298))
        click(Pattern("1662022601417.png").targetOffset(180,-298))
        sleep(1)
        print("circus card table pass")
    else:
        print("circus card table error")
        assert False

# mall_props featured props pirate ship card table
def props_featured_pirateShipCardTable():                                                             
    if exists(Pattern("1662022679373.png").similar(0.90),60):
        click(Pattern("1662022679373.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662022694814.png").similar(0.90).targetOffset(183,-297))
        click(Pattern("1662022694814.png").targetOffset(183,-297))
        sleep(1)
        print("pirate ship card table pass")
    else:
        print("pirate ship card table error")
        assert False

# mall_props featured props ruins card table
def props_featured_ruinsCardTable():                                                             
    if exists(Pattern("1662022842162.png").similar(0.90),60):
        click(Pattern("1662022842162.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662022860800.png").similar(0.90).targetOffset(180,-294))
        click(Pattern("1662022860800.png").targetOffset(180,-294))
        sleep(1)
        print("ruins card table pass")
    else:
        print("ruins card table error")
        assert False

# mall_props featured props electronic playground card table
def props_featured_electronicPlaygroundCardTable():                                                             
    if exists(Pattern("1661328071224.png").similar(0.90),60):
        click(Pattern("1661333734134.png").similar(0.90).targetOffset(2,85))
        sleep(1)
        assert exists(Pattern("1661333673052.png").similar(0.90).targetOffset(181,-305))
        click(Pattern("1661333673052.png").targetOffset(181,-305))
        sleep(1)
        print("electronic playground card table pass")
    else:
        print("electronic playground card table error")
        assert False

# mall_props featured props warrior card table
def props_featured_warriorCardTable():                                                             
    if exists(Pattern("1662024125627.png").similar(0.90),60):
        click(Pattern("1662024125627.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662024139284.png").similar(0.90).targetOffset(181,-295))
        click(Pattern("1662024139284.png").targetOffset(181,-295))
        sleep(1)
        print("warrior card table pass")
    else:
        print("warrior card table error")
        assert False

# mall_props featured props cowboy card
def props_featured_cowboyCard():                                                             
    if exists(Pattern("1662024414162.png").similar(0.95),60):
        click(Pattern("1662024414162.png").similar(0.94))
        sleep(1)
        assert exists(Pattern("1662024459321.png").similar(0.95).targetOffset(180,-152))
        click(Pattern("1662024459321.png").targetOffset(180,-152))
        sleep(1)
        print("cowboy card pass")
    else:
        print("cowboy card error")
        assert False

# mall_props featured props electronic playground card
def props_featured_electronicPlaygroundCard():                                                             
    if exists(Pattern("1662024530222.png").similar(0.90),60):
        click(Pattern("1662024530222.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662024548229.png").similar(0.93).targetOffset(178,-152))
        click(Pattern("1662024548229.png").targetOffset(178,-152))
        sleep(1)
        print("electronic playground card pass")
    else:
        print("electronic playground card error")
        assert False

# mall_props featured props warrior card
def props_featured_warriorCard():                                                             
    if exists(Pattern("1662024604031.png").similar(0.95),60):
        click(Pattern("1662024604031.png").similar(0.95))
        sleep(1)
        assert exists(Pattern("1662024618953.png").similar(0.95).targetOffset(182,-150))
        click(Pattern("1662024618953.png").targetOffset(182,-150))
        sleep(1)
        print("warrior card pass")
    else:
        print("warrior card error")
        assert False
    sleep(1)
    
# mall_props switch coins
def props_switchCoin():                     
    dragDrop("1662018518471.png","1662018527135.png")

# mall_props switch featured props part1
def props_switchFeaturedPart1():                                                     
    dragDrop("1662019663379.png","1662018518471.png")

# mall_props switch featured props part2
def props_switchFeaturedPart2():                                                             
    dragDrop("1662021408850.png","1662021472487.png")

# mall_props switch featured props part3
def props_switchFeaturedPart3():                                                             
    dragDrop("1662022771670.png","1662022780038.png")


### mall_daimond ###
# mall_daimond 60 daimond
def daimond_60daimond():
    if exists(Pattern("1663924678436.png").similar(0.90),60):
        click(Pattern("1661335219264.png").similar(0.90).targetOffset(-1,87))
        if exists((Pattern("1663925093687.png").similar(0.90))and(Pattern("1663925111398.png").similar(0.90)),60):
            click("1661335365765.png")
            sleep(2)
            print("60 daimond pass")
        else:
            print("google recharge failed")
            assert False

# mall_daimond 300 daimond
def daimond_300daimond():        
    if exists(Pattern("1663924678436.png").similar(0.90),60):
        click(Pattern("1661335755750.png").similar(0.90).targetOffset(1,-4))
        if exists((Pattern("1663925093687.png").similar(0.90))and(Pattern("1663925152119.png").similar(0.90)),60):
            click("1661335365765.png")
            sleep(2)
            print("300 daimond pass")
        else:
            print("google recharge failed")
            assert False
    else:
        print("300 daimond error")
        assert False

# mall_daimond 780 daimond
def daimond_780daimond():        
    if exists(Pattern("1663924678436.png").similar(0.90),60):
        click(Pattern("1662024727403.png").similar(0.90))
        if exists((Pattern("1663925093687.png").similar(0.90))and(Pattern("1663925169736.png").similar(0.90)),60):
            click("1661335365765.png")
            sleep(2)
            print("780 daimond pass")
        else:
            print("google recharge failed")
            assert False
    else:
        print("780 daimond error")
        assert False

# mall_daimond 1180 daimond
def daimond_1180daimond():        
    if exists(Pattern("1663924678436.png").similar(0.90),60):
        click("1662024842455.png")
        if exists((Pattern("1663925093687.png").similar(0.90))and(Pattern("1663925187894.png").similar(0.90)),60):
            click("1661335365765.png")
            sleep(1)
            print("1180+38 daimond pass")
        else:
            print("google recharge failed")
            assert False
    else:
        print("1180+38 daimond error")
        assert False

# mall_daimond 2880 daimond
def daimond_2880daimond():        
    if exists(Pattern("1663924678436.png").similar(0.90),60):
        click(Pattern("1662024893102.png").similar(0.90))
        if exists((Pattern("1663925093687.png").similar(0.90))and(Pattern("1663925204453.png").similar(0.90)),60):
            click("1661335365765.png")
            sleep(2)
            print("2880+108 daimond pass")
        else:
            print("google recharge failed")
            assert False
    else:
        print("2880+108 daimond error")
        assert False

# mall_daimond 6280 daimond
def daimond_6280daimond():        
    if exists(Pattern("1663924678436.png").similar(0.90),60):
        click("1662024929819.png")
        if exists((Pattern("1663925093687.png").similar(0.90))and(Pattern("1663925219817.png").similar(0.90)),60):
            click("1661335365765.png")
            sleep(2)
            print("6280+188 daimond pass")
        else:
            print("google recharge failed")
            assert False
    else:
        print("6280+188 daimond error")
        assert False
    sleep(1)


### mall_integral ###
# mall_integral 70K gold coin
def integral_70KGoldCoin():
    if exists(Pattern("1661392529409.png").similar(0.90),60):
        click(Pattern("1661392529409.png").similar(0.90).targetOffset(1,86))
        sleep(1)
        assert exists(Pattern("1661392668582.png").similar(0.90).targetOffset(181,-151))
        click(Pattern("1661392668582.png").targetOffset(181,-151))
        sleep(1)
        print("70K gold coin pass")
    else:
        print("70K gold coin error")
        assert False

# mall_integral 800K gold coin
def integral_800KGoldCoin():
    if exists(Pattern("1661392839487.png").similar(0.90),60):
        click(Pattern("1661392839487.png").similar(0.90).targetOffset(1,88))
        sleep(1)
        assert exists(Pattern("1661393773363.png").similar(0.90).targetOffset(181,-154))
        click(Pattern("1661393773363.png").targetOffset(181,-154))
        sleep(1)
        print("800K gold coin pass")
    else:
        print("800K gold coin error")
        assert False

# mall_integral 8M gold coin
def integral_8MGoldCoin():
    if exists(Pattern("1662025048731.png").similar(0.90),60):
        click(Pattern("1662025048731.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662025062365.png").similar(0.90).targetOffset(183,-150))
        click(Pattern("1662025062365.png").targetOffset(183,-150))
        sleep(1)
        print("8M gold coin pass")
    else:
        print("8M gold coin error")
        assert False

# mall_integral VIP silver card
def integral_silverCard():
    if exists(Pattern("1662025090530.png").similar(0.89),60):
        click(Pattern("1662025090530.png").similar(0.89))
        sleep(1)
        assert exists(Pattern("1662025106400.png").similar(0.90).targetOffset(181,-147))
        click(Pattern("1662025106400.png").targetOffset(181,-147))
        sleep(1)
        print("VIP silver card pass")
    else:
        print("VIP silver card error")
        assert False

# mall_integral VIP black card
def integral_blackCard():
    if exists(Pattern("1662025242458.png").similar(0.89),60):
        click(Pattern("1662025242458.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1662025260828.png").similar(0.90).targetOffset(181,-151))
        click(Pattern("1662025260828.png").targetOffset(181,-151))
        sleep(1)
        print("VIP black card pass")
    else:
        print("VIP black card error")
        assert False

# mall_integral VIP platinumk card
def integral_platinumkCard():
    if exists(Pattern("1662025303556.png").similar(0.89),60):
        click(Pattern("1662025303556.png").similar(0.89))
        sleep(1)
        assert exists(Pattern("1662025318268.png").similar(0.90).targetOffset(182,-150))
        click(Pattern("1662025318268.png").targetOffset(182,-150))
        sleep(1)
        print("VIP platinum card pass")
    else:
        print("VIP platinum card error")
        assert False
    sleep(1)

# mall_integral detail
def integral_detail():
    if exists(Pattern("1663138869265.png").similar(0.90),60):
        click(Pattern("1663138869265.png").similar(0.90))
        sleep(1)
        assert exists(Pattern("1663138914086.png").similar(0.90),60)
        click(Pattern("1663138914086.png").targetOffset(181,-224))
        sleep(1)
        print("detail pass")
    else:
        print("detail error")
        assert False
    sleep(1)

# mall_integral record
def integral_record():
    if exists(Pattern("1663138983952.png").similar(0.90),60):
        click(Pattern("1663138983952.png").similar(0.90))
        sleep(1)
        assert exists("1663139040176.png"and"1663139048119.png",60)
        click("1663139048119.png")
        sleep(1)
        print("record pass")
    else:
        print("record error")
        assert False
    sleep(1)






    