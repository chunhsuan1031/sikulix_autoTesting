from sikuli import *
import datetime
import unittest
import function_club
import function_common

class club(unittest.TestCase): 
    ### home ###
    def testA1_club(self):
        function_common.reopenApp()
        function_common.globalTournamentNotice()
        function_club.club()

    def testA2_club_mail(self):
        function_club.club_mail()

    def testA3_club_support(self):
        function_club.club_support()

    def testA4_club_introduction(self):
        function_club.club_introduction()

    def testA5_club_introduction_share(self):
        function_club.club_introduction_share()

    def testA6_club_introduction_edit(self):
        function_club.club_introduction_edit()

    def testA7_club_ppcoin(self):
        function_club.club_ppcoin()

    def testA8_club_ppcoin_ppcoinExchange(self):
        function_club.club_ppcoin_ppcoinExchange()

    def testA9_club_ppcoin_daimondExchange(self):
        function_club.club_ppcoin_daimondExchange()

    def testB1_club_globalTournament(self):
        function_club.club_globalTournament()

    def testB2_club_league(self):
        function_club.club_league()

    def testB3_club_league_add(self):
        function_club.club_league_add()

    def testB4_club_league_create(self):
        function_club.club_league()
        function_club.club_league_create()

    def testB5_club_member(self):
        function_club.club_member()

    def testB6_club_member_personalInfo(self):
        function_club.club_member_personalInfo()

    def testB7_club_member_otherInfo(self):
        function_club.club_member_otherInfo()

    def testB8_club_member_search(self):
        function_club.club_member_search()

    def testB9_club_member_buyin(self):
        function_club.club_member_buyin()

    def testC1_club_member_winnings(self):
        function_club.club_member_winnings()

    def testC2_club_member_hands(self):
        function_club.club_member_hands()

    def testC3_club_member_lastLogin(self):
        function_club.club_member_lastLogin()

    def testC4_club_member_lastPlayed(self):
        function_club.club_member_lastPlayed()

    def testC5_club_member_chipStorm(self):
        function_club.club_member_chipStorm()

    def testC6_club_member_newMember(self):
        function_club.club_member_newMember()

    def testC7_club_counter(self):
        function_club.club_counter()

    def testC8_club_counter_record(self):
        function_club.club_counter_record()

    def testC9_club_counter_search(self):
        function_club.club_counter_search()

    def testD1_club_counter_sendOut(self):
        function_club.club_counter_sendOut()

    def testD2_club_counter_claimBack(self):
        function_club.club_counter_claimBack()

    def testD3_club_counter_ppChip(self):
        function_club.club_counter_ppChip()

    def testD4_club_counter_prizes(self):
        function_club.club_counter_prizes()

    def testD5_club_counter_expiryDate(self):
        function_club.club_counter_expiryDate()

    def testD6_club_counter_sendItems(self):
        function_club.club_counter_sendItems()

    def testD7_club_counter_ticket(self):
        function_club.club_counter_ticket()

    def testD8_club_data(self):
        function_club.club_data()

    def testD9_club_data_excel(self):
        function_club.club_data_excel()

    def testE1_club_data_dateArrow(self):
        function_club.club_data_dateArrow()

    def testE2_club_data_yesterday(self):
        function_club.club_data_yesterday()

    def testE3_club_data_lastSevenDay(self):
        function_club.club_data_lastSevenDay()

    def testE4_club_data_select(self):
        function_club.club_data_select()

    def testE5_club_data_category(self):
        function_club.club_data_category()

    def testE6_club_admin(self):
        function_club.club_admin()

    def testE7_club_admin_notifications(self):
        function_club.club_admin_notifications()

    def testE8_club_admin_clubRating(self):
        function_club.club_admin_clubRating()

    def testE9_club_admin_backpack(self):
        function_club.club_admin_backpack()

    def testF1_club_admin_jackpot(self):
        function_club.club_admin_jackpot()

    def testF2_club_admin_event(self):
        function_club.club_admin_event()

    def testF3_club_admin_preferences(self):
        function_club.club_admin()
        function_club.club_admin_preferences()

    def testF4_club_admin_disband(self):
        function_club.club_admin()
        function_club.club_admin_disband()








