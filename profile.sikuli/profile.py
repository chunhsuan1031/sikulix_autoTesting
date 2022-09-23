from sikuli import *
import datetime
import unittest
import function_profile
import function_common

class profile(unittest.TestCase): 
    ### profile_nft ###
    def testA1_profile_nft_interface(self):
        function_common.reopenApp()
        function_common.globalTournamentNotice()
        if exists("1662430711217.png",10):
            click("1662430711217.png")
            sleep(1)
            if exists(Pattern("1661394657614-2.png").similar(0.80),3):
                sleep(1)
                click(Pattern("1661394657614-2.png").similar(0.90))
                sleep(1)
                function_profile.nft_interface()
            else:
                print("can't find nft button")
                assert False
        else:
            print("can't find profile")
            assert False

    def testA2_profile_nft_question(self):
        function_profile.nft_question()

    def testA3_profile_nft_wallet(self):
        function_profile.nft_wallet()  

    def testA4_profile_nft_share(self):
        function_profile.nft_share()
        click("1662350042725.png")
        sleep(1)

    ### profile_tutorial ###
    def testB1_profile_tutorial(self):
        function_profile.tutorial()
        
    ### profile_avatar ###
    def testC1_profile_avatar(self):
        function_profile.avatar()

    def testC2_profile_avatar_image(self):
        function_profile.avatar_image()

    def testC3_profile_avatar_image_customize(self):
        function_profile.avatar_image_customize()

    def testC4_profile_avatar_image_album(self):
        function_profile.avatar_image_album()

    def testC5_profile_avatar_image_cancel(self):
        function_profile.avatar_image()
        function_profile.avatar_image_cancel()    

    def testC6_profile_avatar_photoFrame(self):
        function_profile.avatar_photoFrame()    

    def testC7_profile_avatar_name(self):
        function_profile.avatar_name()    

    def testC8_profile_avatar_region(self):
        function_profile.avatar_region() 

    def testC9_profile_avatar_confirm(self):
        function_profile.avatar_confirm() 

    ### profile_lv ###
    def testD1_profile_lv(self):
        function_profile.lv()

    ### profile_hand ###
    def testE1_profile_hand_recenv(self):
        function_profile.hand_recent()

    def testE2_profile_hand_recent_replayv(self):
        function_profile.hand_recent_replay()

    def testE3_profile_hand_recent_sharev(self):
        function_profile.hand_recent_share()

    def testE4_profile_hand_recent_heartv(self):
        function_profile.hand_recent_heart()

    def testE5_profile_hand_collect(self):
        function_profile.hand_collect()

    def testE6_profile_hand_collect_replay(self):
        function_profile.hand_collect_replay()

    def testE7_profile_hand_collect_share(self):
        function_profile.hand_collect_share()
        click("1662374250802.png")
        sleep(1)
        
    ### profile_feedback ###
    def testF1_profile_feedback(self):
        function_profile.feedback()

    ### profile_setup ###
    def testG1_profile_setup(self):
        function_profile.setup()

    def testG2_profile_setup_sound(self):
        function_profile.setup_sound()

    def testG3_profile_setup_mail(self):
        function_profile.setup_mail()

    def testG4_profile_setup_password(self):
        function_profile.setup_password()        

    def testG5_profile_setup_language(self):
        function_profile.setup_language()

    def testG6_profile_setup_signOut(self):
        function_profile.setup_signOut()

    ### profile_aboutUs ###
    def testH1_profile_aboutUs(self):
        function_profile.aboutUs()

    def testH2_profile_aboutUs_fair(self):
        function_profile.aboutUs_fair()

    def testH3_profile_aboutUs_contactUs(self):
        function_profile.aboutUs_contactUs()

    def testH4_profile_aboutUs_service(self):
        function_profile.aboutUs_service()

    def testH5_profile_aboutUs_privacy(self):
        function_profile.aboutUs_privacy()

    ### profile_compliance ###
    def testI1_profile_compliance(self):
        function_profile.compliance()

    ### profile_invite ###
    def testJ1_profile_invite(self):
        function_profile.invite()

    def testJ2_profile_invite_copy(self):
        function_profile.invite_copy()

    def testJ3_profile_invite_share(self):
        function_profile.invite_share()

    def testJ4_profile_invite_poster(self):
        function_profile.invite_poster()

    def testJ5_profile_invite_task(self):
        function_profile.invite_task()









