from sikuli import *
import datetime
import unittest
import function_mall
import function_common

class mall(unittest.TestCase): 
    #props
    def testA1_mall_props_recommend_electronicPlaygroundCardTable(self):
        function_common.openApp()
        function_common.globalTournamentNotice()
        if exists("1660299042385.png",10):
            click("1660299042385.png")
            sleep(1)
            if exists("1661329961213.png" or "1661329973625.png"):
                click("1661329961213.png" or "1661329973625.png")
                function_mall.props_recommend_electronicPlaygroundCardTable()
        else:
            print("can't find mall")
            assert False

    def testA2_mall_props_recommend_electronicPlaygroundCard(self):
        function_mall.props_recommend_electronicPlaygroundCard()
        
    def testA3_mall_props_recommend_6MGoldCoin(self):
        function_mall.props_recommend_6MGoldCoin()

    def testA4_mall_props_vip_silverCard(self):
        function_mall.props_vip_silverCard()

    def testA5_mall_props_vip_blackCard(self):
        function_mall.props_vip_blackCard()

    def testA6_mall_props_vip_platinumCard(self):
        function_mall.props_vip_platinumCard()

    def testA7_mall_props_coin_6MGoldCoin(self):
        function_mall.props_switchCoin()
        function_mall.props_coin_6MGoldCoin()

    def testA8_mall_props_coin_33MGoldCoin(self):
        function_mall.props_coin_33MGoldCoin()

    def testA9_mall_props_coin_78MGoldCoin(self):
        function_mall.props_coin_78MGoldCoin()

    def testB1_mall_props_coin_148MGoldCoin(self):
        function_mall.props_coin_148MGoldCoin()

    def testB2_mall_props_coin_388MGoldCoin(self):
        function_mall.props_coin_388MGoldCoin()

    def testB3_mall_props_coin_768MGoldCoin(self):
        function_mall.props_coin_768MGoldCoin()

    def testB4_mall_props_featured_miRiverCard(self):
        function_mall.props_switchFeaturedPart1()
        function_mall.props_featured_miRiverCard()

    def testB5_mall_props_featured_timeBank(self):
        function_mall.props_featured_timeBank()

    def testB6_mall_props_featured_communityCard(self):
        function_mall.props_featured_communityCard()

    def testB7_mall_props_featured_halloweenEmoji(self):
        function_mall.props_featured_halloweenEmoji()

    def testB8_mall_props_featured_sharkEmoji(self):
        function_mall.props_featured_sharkEmoji()

    def testB9_mall_props_featured_jokerEmoji(self):
        function_mall.props_featured_jokerEmoji()

    def testC1_mall_props_featured_kingEmoji(self):
        function_mall.props_switchFeaturedPart2()
        function_mall.props_featured_kingEmoji()

    def testC2_mall_props_featured_yellowFaceEmoji(self):
        function_mall.props_featured_yellowFaceEmoji()

    def testC3_mall_props_featured_littleSharkEmoji(self):
        function_mall.props_featured_littleSharkEmoji()

    def testC4_mall_props_featured_generalEmoji(self):
        function_mall.props_featured_generalEmoji()

    def testC5_mall_props_featured_circusCardTable(self):
        function_mall.props_featured_circusCardTable()

    def testC6_mall_props_featured_pirateShipCardTable(self):
        function_mall.props_featured_pirateShipCardTable()

    def testC7_mall_props_featured_ruinsCardTable(self):
        function_mall.props_switchFeaturedPart3()
        function_mall.props_featured_ruinsCardTable()

    def testC8_mall_props_featured_electronicPlaygroundCardTable(self):
        function_mall.props_featured_electronicPlaygroundCardTable()

    def testC9_mall_props_featured_warriorCardTable(self):
        function_mall.props_featured_warriorCardTable()

    def testD1_mall_props_featured_cowboyCard(self):
        function_mall.props_featured_cowboyCard()

    def testD2_mall_props_featured_electronicPlaygroundCard(self):
        function_mall.props_featured_electronicPlaygroundCard()

    def testD3_mall_props_featured_warriorCard(self):
        function_mall.props_featured_warriorCard()

    #daimond
    def testD4_mall_daimond_60daimond(self):
        if exists("1660299042385.png",10):
            if exists("1661335974572.png" or "1661335988283.png"):
                click("1661335974572.png" or "1661335988283.png")
                function_mall.daimond_60daimond()
        else:
            print("can't find mall")
            assert False
            
    def testD5_mall_daimond_300daimond(self):
        function_mall.daimond_300daimond()

    def testD6_mall_daimond_780daimond(self):
        function_mall.daimond_780daimond()

    def testD7_mall_daimond_1180daimond(self):
        function_mall.daimond_1180daimond()

    def testD8_mall_daimond_2880daimond(self):
        function_mall.daimond_2880daimond()

    def testD9_mall_daimond_6280daimond(self):
        function_mall.daimond_6280daimond()

    #integral
    def testE1_mall_integral_70KGoldCoin(self):
        if exists("1660299042385.png",10):
            if exists("1661397308333.png" or "1661397324974.png"):
                click("1661397308333.png" or "1661397324974.png")
                function_mall.integral_70KGoldCoin()
        else:
            print("can't find mall")
            assert False

    def testE2_mall_integral_800KGoldCoin(self):
        function_mall.integral_800KGoldCoin()

    def testE3_mall_integral_8MGoldCoin(self):
        function_mall.integral_8MGoldCoin()

    def testE4_mall_integral_silverCard(self):
        function_mall.integral_silverCard()

    def testE5_mall_integral_blackCard(self):
        function_mall.integral_blackCard()

    def testE6_mall_integral_platinumkCard(self):
        function_mall.integral_platinumkCard()

    def testE7_mall_integral_detail(self):
        function_mall.integral_detail()

    def testE8_mall_integral_record(self):
        function_mall.integral_record()
            