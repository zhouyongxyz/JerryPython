#!/usr/bin/python
# -*- coding: UTF-8 -*-
# owner zhouyong0701 2018/01/16
from lxml import etree
import sys
import getopt


def create_sub_plan(inputfile,module,abi,outputfile):
    tree = etree.parse(inputfile)
    # moudules= tree.xpath('/Result/Module')
    # for moudule in moudules:
    #     print moudule.xpath('./@*')[0]
    subplan_file = open('subplan_test.xml', 'w')
    subplan_file.write("<?xml version='1.0' encoding='UTF-8' standalone='no' ?>\n")
    subplan_file.write("<SubPlan version=\"2.0\">\n")

    if module != "":
        tests = tree.xpath('/Result/Module[@name="'+module+'" and @abi="'+abi+'"]/TestCase/Test')
        if len(tests) > 0 :
            for test in tests:
                test_name = test.xpath('./@name')[0]
                test_case_name = test.xpath('../@name')[0]
                test_case = test.xpath('..')[0]
                test_module_name = test_case.xpath('../@name')[0]
                #print len(test_case)
                #print test_module_name + " " + test_case_name +  " " + test_name
                entry_line = '  <Entry include="' + abi + ' ' + test_module_name + ' ' + test_case_name + '#' + test_name + '" />\n'
                print entry_line
                subplan_file.write(entry_line)
    subplan_file.write("</SubPlan>\n")
    subplan_file.close()


def main(argv):
    module = 'CtsAppSecurityHostTestCases'
    abi = 'arm64-v8a'
    inputfile = "./test_result.xml"
    outputfile = "./test_subplan.xml"
    try:
        opts, args = getopt.getopt(argv, "hi:m:a:o:", ["input=","moudle=", "abi="])
    except getopt.GetoptError:
        print 'cts-create-subplan.py -i <inputfile> -m <moudle> -a <abi>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'cts-create-subplan.py -i <inputfile> -m <moudle> -a <abi>'
            sys.exit()
        elif opt in ("-m", "--moudle"):
            if arg != "":
                module = arg
        elif opt in ("-a", "--abi"):
            if arg != "":
                abi = arg
        elif opt in ("-i","--input"):
            if arg != "":
                inputfile = arg
        elif opt in ("-o"):
            if arg != "":
                outputfile = arg
    print 'inputfile: ',inputfile
    print 'module：', module
    print 'abi：', abi
    create_sub_plan(inputfile,module,abi,outputfile);


if __name__ == '__main__':
    main(sys.argv[1:]);