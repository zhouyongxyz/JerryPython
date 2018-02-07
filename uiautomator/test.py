from uiautomator import device as d
import os
import time
# -*- coding: UTF-8 -*-

def test():
    #d.press.back();
    #d.screenshot("home.png");
    #time.sleep(3);
    response = os.system("adb shell am start -n com.example.zhouyong0701.storagetest/.MainActivity");
    time.sleep(2);
    print response
    d(text="SPEAK").click();


def main():
    test();

if __name__ == '__main__':
    main();

