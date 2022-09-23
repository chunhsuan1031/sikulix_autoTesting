from sikuli import *
import datetime
import unittest
import function_career
import function_common

class career(unittest.TestCase): 
    ### career ###
    def testA1_profile_career(self):
        function_common.reopenApp()
        function_common.globalTournamentNotice()
        if exists("1662606427744.png",10):
            click("1662606427744.png")
            sleep(1)
            function_career.career()
        else:
            print("can't find career")
            assert False

    def testA2_profile_career_month(self):
        function_career.career_month()

    def testA3_profile_career_year(self):
        function_career.career_year()

    def testA4_profile_career_day(self):
        function_career.career_day()

    def testA5_profile_career_club_nlh(self):
        function_career.career_filter()
        function_career.career_club_nlh()

    def testA6_profile_career_club_aof(self):
        function_career.career_filter()
        function_career.career_club_aof()

    def testA7_profile_career_club_sixPlus(self):
        function_career.career_filter()
        function_career.career_club_sixPlus()

    def testA8_profile_career_club_plo(self):
        function_career.career_filter()
        function_career.career_club_plo()

    def testA9_profile_career_club_ploHL(self):
        function_career.career_filter()
        function_career.career_club_ploHL()

    def testB1_profile_career_club_flashNlh(self):
        function_career.career_filter()
        function_career.career_club_flashNlh()

    def testB2_profile_career_club_flashPlo(self):
        function_career.career_filter()
        function_career.career_club_flashPlo()

    def testB3_profile_career_club_nlhPlo(self):
        function_career.career_filter()
        function_career.career_club_nlhPlo()

    def testB4_profile_career_club_pusoy(self):
        function_career.career_filter()
        function_career.career_club_pusoy()

    def testB5_profile_career_club_ofc(self):
        function_career.career_filter()
        function_career.career_club_ofc()

    def testB6_profile_career_club_spinUp(self):
        function_career.career_filter()
        function_career.career_club_spinUp()

    def testB7_profile_career_club_sngNlh(self):
        function_career.career_filter()
        function_career.career_club_sngNlh()

    def testB8_profile_career_club_sngPlo(self):
        function_career.career_filter()
        function_career.career_club_sngPlo()

    def testB9_profile_career_club_mttNlh(self):
        function_career.career_filter()
        function_career.career_club_mttNlh()

    def testC1_profile_career_club_mttPlo(self):
        function_career.career_filter()
        function_career.career_club_mttPlo()

    def testC2_profile_career_club_teenPatti(self):
        function_career.career_filter()
        function_career.career_club_teenPatti()

    def testC3_profile_career_club_all(self):
        function_career.career_filter()
        function_career.career_club_all()

    def testD1_profile_career_lobby_all(self):
        function_career.career_filter()
        function_career.career_lobby_all()

    def testD2_profile_career_lobby_nlh(self):
        function_career.career_filter()
        function_career.career_lobby_nlh()

    def testD3_profile_career_lobby_plo(self):
        function_career.career_filter()
        function_career.career_lobby_plo()

    def testD4_profile_career_lobby_ofc(self):
        function_career.career_filter()
        function_career.career_lobby_ofc()

    def testE1_profile_career_globalTournament_all(self):
        function_career.career_filter()
        function_career.career_globalTournament_all()

    def testE2_profile_career_globalTournament_sng(self):
        function_career.career_filter()
        function_career.career_globalTournament_sng()

    def testE3_profile_career_globalTournament_spinUp(self):
        function_career.career_filter()
        function_career.career_globalTournament_spinUp()

    def testE4_profile_career_globalTournament_mttNlh(self):
        function_career.career_filter()
        function_career.career_globalTournament_mttNlh()

    def testE5_profile_career_globalTournament_mttPlo(self):
        function_career.career_filter()
        function_career.career_globalTournament_mttPlo()










