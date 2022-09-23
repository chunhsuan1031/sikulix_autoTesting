from sikuli import *
import datetime
import unittest
import function_home
import function_common

class home(unittest.TestCase): 
    ### home ###
    def testA1_home_vip(self):
        function_common.reopenApp()
        function_common.globalTournamentNotice()
        function_home.home_vip()

    def testA2_home_integral(self):
        function_home.home_integral()

    def testA3_home_daimond(self):
        function_home.home_daimond()

    def testA4_home_coin(self):
        function_home.home_coin()

    def testA5_home_announcement(self):
        function_home.home_announcement()

    def testA6_home_task(self):
        function_home.home_task()

    def testA7_home_mail(self):
        function_home.home_mail()

    def testA8_home_createClub(self):
        function_home.home_createClub()

    def testA9_home_findClub(self):
        function_home.home_findClub()

    def testB1_home_club(self):
        function_home.home_club()

    def testB2_home_lobby(self):
        function_home.home_lobby()

    def testB3_home_globalTournament(self):
        function_home.home_globalTournament()

    def testB4_home_spinUp(self):
        function_home.home_spinUp()



















