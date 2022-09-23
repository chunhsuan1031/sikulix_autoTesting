import unittest
import time
from datetime import datetime
import shutil
from sikuli import *
import HTMLTestRunner
from unittest import TestLoader, TestSuite
from mall import *
from profile import *
from community import *
from career import *
from home import *
from club import *

suite_mall = unittest.TestLoader().loadTestsFromTestCase(mall)
suite_profile = unittest.TestLoader().loadTestsFromTestCase(profile)
suite_community = unittest.TestLoader().loadTestsFromTestCase(community)
suite_career = unittest.TestLoader().loadTestsFromTestCase(career)
suite_home = unittest.TestLoader().loadTestsFromTestCase(home)
suite_club = unittest.TestLoader().loadTestsFromTestCase(club)
suite = TestSuite([suite_mall,suite_community,suite_home,suite_career, suite_profile,suite_club])
#suite = TestSuite([suite_club])
#for i in range(0):
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(result))

timestamp = time.strftime('%Y%m%d%H%M')
rname = 'TestReport_'+timestamp+'.html'
base_dir = os.path.abspath(getBundlePath()+'//..')
report_file = os.path.join(base_dir, rname)
outfile = open(report_file, "wb") # path to report folder
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='PPPoker', description='Test By KIWIGAME')
runner.run(suite)
outfile.close()