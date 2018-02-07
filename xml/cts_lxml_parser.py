#!/usr/bin/python
# -*- coding: UTF-8 -*-
# owner zhouyong0701 2018/01/16
from lxml import etree


def sperate():
    tree = etree.parse("./test_result.xml")
    # moudules= tree.xpath('/Result/Module')
    # for moudule in moudules:
    #     print moudule.xpath('./@*')[0]
    result_file = open("./test_result.xml")
    fail_file = open('test_result_fail_report.xml', 'w')
    line = result_file.readline()
    while line:
        if "<Module" in line:
            break
        fail_file.write(line)
        line = result_file.readline()

    result_file.close()


    moudules = tree.xpath('/Result/Module')
    total = 0;
    fail = 0;
    #foreache moudule
    for moudule in moudules:
        fail_tests = moudule.xpath('.//Test[@result="fail"]')
        if len(fail_tests) > 0 :
            print "parser moudule -> " + moudule.xpath('./@name')[0] + " fail -> " + str(len(fail_tests))
            #print etree.tostring(moudule)
            total += 1
            fail += len(fail_tests)
            testcases = moudule.xpath('./TestCase')
            #foreach TestCase remove the all pass TestCase from moudule
            for testcase in testcases:
                fail_count = testcase.xpath('.//Test[@result="fail"]')
                if len(fail_count) == 0 :
                    moudule.remove(testcase)
                pass_count = testcase.xpath('.//Test[@result="pass"]')
                if len(pass_count) > 0 :
                    tests = testcase.xpath('./Test')
                    #foreach test remove the pass test in TestCase
                    for test in tests :
                        if test.xpath('./@result')[0] == 'pass' :
                            print "remove test -> " + test.xpath('./@name')[0] + " = " + test.xpath('./@result')[0]
                            testcase.remove(test)

            fail_file.write(etree.tostring(moudule))
    print "total moudules: " + str(total) + " fail : " + str(fail)
    fail_file.write("</Result>\n");
    fail_file.close()

def main():
    sperate();


if __name__ == '__main__':
    main();