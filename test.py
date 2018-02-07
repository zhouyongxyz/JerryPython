#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: zhouyongxyz


class test(object):
    def __init__(self,a,b):
        self.test = "test"

def main():
    aa = test(0,0)
    print("aa.test = " + aa.test)
    if not aa:
        print("none none")
    else:
        print("aaa")
    pass

if __name__ == '__main__':
    main()