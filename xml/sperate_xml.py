#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

#result_keys = ['start','end','start_display','end_display','suite_name','suite_version','suite_plan','suite_build_number']

def sperate():
    # 使用minidom解析器打开 XML 文档
    impl = xml.dom.minidom.getDOMImplementation()
    arm64_v8a = impl.createDocument(None, 'Result', None)
    style = xml.dom.minidom.Document().createProcessingInstruction("xml-stylesheet", "href=\"compatibility_result.xsl\" type=\"text/xsl\"")
    arm64_v8a.appendChild(style)
    armeabi_v7a = impl.createDocument(None, 'Result', None)#dom.documentElement
    #armeabi_v7a.createProcessingInstruction("xml-stylesheet", "href=\"compatibility_result.xsl\" type=\"text/xsl\"")
    armeabi_v7a.appendChild(style)

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
        print attr + " -> " +result[0].attributes[attr].value
        arm64_v8a.documentElement.setAttribute(attr,result[0].attributes[attr].value)
        armeabi_v7a.documentElement.setAttribute(attr,result[0].attributes[attr].value)

    arm64_v8a.documentElement.appendChild(build[0])
    arm64_v8a.documentElement.appendChild(summary[0])
    armeabi_v7a.documentElement.appendChild(build[0])
    armeabi_v7a.documentElement.appendChild(summary[0])

    for module in modules :
        print module.getAttribute('abi')
        if module.getAttribute('abi') == 'arm64-v8a':
            arm64_v8a.documentElement.appendChild(module)
        elif module.getAttribute('abi') == 'armeabi-v7a':
            armeabi_v7a.documentElement.appendChild(module)
    #write arm64_v8a module file
    f = open('arm64_v8a.xml', 'w')
    arm64_v8a.writexml(f, addindent='  ', newl='', encoding='utf-8')
    f.close()
    # write armeabi_v7a module file
    f = open('armeabi_v7a.xml', 'w')
    arm64_v8a.writexml(f, addindent='  ', newl='', encoding='utf-8')
    f.close()

def main():
    sperate();


if __name__ == '__main__':
    main();