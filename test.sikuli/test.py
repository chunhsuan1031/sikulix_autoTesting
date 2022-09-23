from sikuli import *
import datetime
import unittest
import function_common
import function_mall
import test

if exists(Pattern("1663840156041-1.png").similar(0.90),60):
    click(Pattern("1663840156041-1.png").similar(0.90))
    if exists(Pattern("1663840189999-1.png").similar(0.90),60):
        #QA
        if exists(Pattern("1663840387883-1.png").similar(0.90),60):
            click(Pattern("1663840387883-1.png").similar(0.90))
            assert exists(Pattern("1663840472745-1.png").similar(0.90),60)
            click(Pattern("1663840472745-1.png").similar(0.90).targetOffset(182,-149))
            print("club admin notifications QA pass")
        else:
            print("club admin notifications QA pass")
            assert False
        #image 
        if exists(Pattern("1663840730020-1.png").similar(0.90),60):
            click(Pattern("1663840730020-1.png").similar(0.90))
            assert exists(Pattern("1663840764492-1.png").similar(0.90),60)
            click(Pattern("1663840764492-1.png").similar(0.90).targetOffset(0,-17))
            assert exists(Pattern("1663840832341-1.png").similar(0.90),60)
            click(Pattern("1663840832341-1.png").similar(0.90).targetOffset(123,33))
            print("club admin notifications image pass")
        else:
            print("club admin notifications image pass")
            assert False 
        #image end time
        if exists(Pattern("1663840947838.png").similar(0.90),60):
            click(Pattern("1663840947838.png").similar(0.90))
            assert exists(Pattern("1663840993635.png").similar(0.90),60)
            click(Pattern("1663840993635.png").similar(0.90).targetOffset(-182,3))
            print("club admin notifications image end time pass")
        else:
            print("club admin notifications image end time pass")
            assert False   
        #image send
        if exists(Pattern("1663841096309-1.png").similar(0.90),60):
            click(Pattern("1663841096309-1.png").similar(0.90))
            assert exists(Pattern("1663841120900-1.png").similar(0.90),60)
            print("club admin notifications image send pass")
        else:
            print("club admin notifications image send pass")
            assert False
        #text
        if exists(Pattern("1663841166098-1.png").similar(0.90),60):
            click(Pattern("1663841166098-1.png").similar(0.90))
            assert exists(Pattern("1663841209952-1.png").similar(0.90),60)
            click(Pattern("1663841303043-1.png").similar(0.90))
            assert exists(Pattern("1663841327934-1.png").similar(0.90),60)
            click(Pattern("1663841354199-1.png").similar(0.90))
            print("club admin notifications text pass")
        else:
            print("club admin notifications text pass")
            assert False
        #text end time
        if exists(Pattern("1663840947838.png").similar(0.90),60):
            click(Pattern("1663840947838.png").similar(0.90))
            assert exists(Pattern("1663840993635.png").similar(0.90),60)
            click(Pattern("1663840993635.png").similar(0.90).targetOffset(-182,3))
            print("club admin notifications text end time pass")
        else:
            print("club admin notifications text end time pass")
            assert False   
        #text send
        if exists(Pattern("1663841096309-1.png").similar(0.90),60):
            click(Pattern("1663841096309-1.png").similar(0.90))
            assert exists(Pattern("1663841120900-1.png").similar(0.90),60)
            print("club admin notifications text send pass")
        else:
            print("club admin notifications text send pass")
            assert False
        #exit
        if exists(Pattern("1663841490888-1.png").similar(0.90),60):
            click(Pattern("1663841490888-1.png").similar(0.90))
            assert exists(Pattern("1663841512110-1.png").similar(0.90),60)
            click(Pattern("1663841512110-1.png").similar(0.90).targetOffset(2,145))
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