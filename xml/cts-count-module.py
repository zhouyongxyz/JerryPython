#!/usr/bin/python
# -*- coding: UTF-8 -*-
# owner zhouyong0701 2018/01/19
from lxml import etree
import sys
import getopt

def count_moudle(inputfile,module):
    tree = etree.parse(inputfile)
    if module != "":
        tests = tree.xpath('/Result/Module[@name="'+module+'" and @abi="arm64-v8a"]/TestCase/Test')
        test_cases = tree.xpath('/Result/Module[@name="' + module + '" and @abi="arm64-v8a"]/TestCase')
        for testcase in test_cases:
            print "TestCase: " + testcase.xpath('./@name')[0] + " Tests: " + str(len(testcase.xpath('./Test')))
        print "Module: " + module + " Total tests: " + str(len(tests))
def main(argv):
    module = 'CtsAppSecurityHostTestCases'
    inputfile = './test_result.xml'
    try:
        opts, args = getopt.getopt(argv, "hm:i:", ["moudle=","input="])
    except getopt.GetoptError:
        print 'cts-count-module.py -m <moudle>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'cts-count-module.py -m <moudle>'
            sys.exit()
        elif opt in ("-m", "--moudle"):
            if arg != "":
                module = arg
        elif opt in ("-i", "--input"):
            if arg != "":
                inputfile = arg

        count_moudle(inputfile,module);


if __name__ == '__main__':
    main(sys.argv[1:]);