#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os

def flash_all(path):
    files = os.listdir(path)
    for fi in files:
        if file_extension(fi) == ".img":
            print("flashing {} ...".format(fi))
            cmd = "sudo fastboot flash " + file_name(fi) + " "  + fi
            #print("{}".format(cmd))
            print("\033[0;32m{} \033[0m".format(cmd))
            os.system(cmd)
        else:
            print("\033[0;32m{} \033[0m".format("skip " + fi))

    print("\033[0;32mflashing done ...\033[0m")
    cmd = "sudo fastboot reboot"
    os.system(cmd)
    pass

def file_name(path):
  return os.path.splitext(path)[0]

def file_extension(path):
  return os.path.splitext(path)[1]

def main():
    flash_all("./")
    pass

if __name__ == "__main__":
    main()