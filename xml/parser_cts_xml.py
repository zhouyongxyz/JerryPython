#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

#result_keys = ['start','end','start_display','end_display','suite_name','suite_version','suite_plan','suite_build_number']

def sperate():
    # arm64_v8a
    arm64_v8a = xml.dom.minidom.Document()
    arm64_v8a_result = arm64_v8a.createElement('Result')

    arm64_v8a_style = arm64_v8a.createProcessingInstruction("xml-stylesheet", "href=\"compatibility_result.xsl\" type=\"text/xsl\"")
    arm64_v8a.appendChild(arm64_v8a_style)

    # armeabi_v7a
    armeabi_v7a = xml.dom.minidom.Document()
    armeabi_v7a_result = armeabi_v7a.createElement('Result')
    armeabi_v7a_style = armeabi_v7a.createProcessingInstruction("xml-stylesheet", "href=\"compatibility_result.xsl\" type=\"text/xsl\"")
    armeabi_v7a.appendChild(armeabi_v7a_style)

    #all_fail
    all_fail = xml.dom.minidom.Document()
    all_fail_result = armeabi_v7a.createElement('Result')
    all_fail_style = armeabi_v7a.createProcessingInstruction("xml-stylesheet","href=\"compatibility_result.xsl\" type=\"text/xsl\"")
    all_fail.appendChild(all_fail_style)

    DOMTree = xml.dom.minidom.parse("./test_result.xml")
    collection = DOMTree
    result = collection.getElementsByTagName("Result")
    build = collection.getElementsByTagName("Build")
    summary = collection.getElementsByTagName("Summary")
    modules = collection.getElementsByTagName("Module")

    print result.length
    print build.length
    print summary.length
    print modules.length
    attrs = result[0].attributes.keys()
    for attr in attrs:
        #print attr + " -> " +result[0].attributes[attr].value
        arm64_v8a_result.setAttribute(attr,result[0].attributes[attr].value)
        armeabi_v7a_result.setAttribute(attr,result[0].attributes[attr].value)
        all_fail_result.setAttribute(attr,result[0].attributes[attr].value)

    arm64_v8a_result.appendChild(build[0].cloneNode(-1))
    arm64_v8a_result.appendChild(summary[0].cloneNode(-1))
    armeabi_v7a_result.appendChild(build[0].cloneNode(-1))
    armeabi_v7a_result.appendChild(summary[0].cloneNode(-1))
    all_fail_result.appendChild(build[0].cloneNode(-1))
    all_fail_result.appendChild(summary[0].cloneNode(-1))

    for module in modules :
        #arm64_v8a_module = arm64_v8a.createElement("Module")
        #armeabi_v7a_module = armeabi_v7a.createElement("Module")
        print "parser moudule -> " + module.getAttribute('name') + " start ..."
        all_fail_module = module.cloneNode(1)
        print module.getAttribute('abi')
        if module.getAttribute('abi') == 'arm64-v8a':
            arm64_v8a_result.appendChild(module.cloneNode(-1))
        elif module.getAttribute('abi') == 'armeabi-v7a':
            armeabi_v7a_result.appendChild(module.cloneNode(-1))
        testcases = module.getElementsByTagName("TestCase")
        for testcase in testcases:
            tests = testcase.getElementsByTagName("Test")
            for test in tests:
                if test.getAttribute('result') == 'fail':
                    fail_testcase = testcase.cloneNode(1)
                    fail_test = test.cloneNode(-1)
                    fail_testcase.appendChild(fail_test)
                    all_fail_module.appendChild(fail_test)
                    all_fail_result.appendChild(all_fail_module)
        print "parser moudule -> " + module.nodeName + " end ..."
    arm64_v8a.appendChild(arm64_v8a_result)
    armeabi_v7a.appendChild(armeabi_v7a_result)
    all_fail.appendChild(all_fail_result)
    #write arm64_v8a module file
    f = open('test_result_arm64_v8a.xml', 'w')
    arm64_v8a.writexml(f, addindent='  ', newl='', encoding='utf-8')
    f.close()
    # write armeabi_v7a module file
    f = open('test_result_armeabi_v7a.xml', 'w')
    armeabi_v7a.writexml(f, addindent='  ', newl='', encoding='utf-8')
    f.close()
    # write all fail report
    f = open('test_result_all_fail.xml', 'w')
    all_fail.writexml(f, addindent='  ', newl='', encoding='utf-8')
    f.close()

def main():
    sperate();


if __name__ == '__main__':
    main();