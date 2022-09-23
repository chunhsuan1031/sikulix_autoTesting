from sikuli import *
import datetime
import unittest
import function_community
import function_common

class community(unittest.TestCase): 
    ### community ###
    def testA1_community_featured(self):
        function_common.reopenApp()
        function_common.globalTournamentNotice()
        if exists("1662455734322.png",10):
            click("1662455734322.png")
            sleep(1)
            function_community.featured()
        else:
            print("can't find profile")
            assert False

    def testA2_community_notice(self):
        function_community.notice()

    def testA3_community_hand(self):
        function_community.hand()

    def testA4_community_post(self):
        function_community.post()

    def testA5_community_replay(self):
        function_community.replay()

    def testA6_community_hot(self):
        function_community.hot()

    def testA7_community_new(self):
        function_community.new()

    def testA8_community_mine(self):
        function_community.mine()

























