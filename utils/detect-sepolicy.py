#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

Path_delta_N = "sepolicy_android_n_delta"
Path_delta_O = "sepolicy_android_o_delta"
Path_origin_O = "sepolicy_android_o_origin"
count = 0
need_porting = 0


def detect_dir(filepath):
    global count
    global need_porting
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            detect_dir(fi_d)
        else:
            if True or file_extension(fi) == ".te" :
                targetFile = os.path.join(filepath, fi_d)
                #print "fi = " + fi
                count += 1
                cmd = "find " + Path_delta_O + " -name \"" + fi + "\""
                #print "cmd = " + cmd
                delta_files = os.popen(cmd).readlines()
                cmd = "find " + Path_origin_O + " -name \"" + fi + "\""
                origin_files = os.popen(cmd).readlines()

                if len(delta_files) <= 0 :
                    show_head = True;
                    # check every line
                    file = open(fi_d)
                    line = file.readline()
                    while line:
                        line = line.strip()
                        if line != "" and "#" not in line and "userdebug_or_eng" not in line:
                            #print "line =" + line
                            grep_cmd = "grep -rn \"" + line + "\" " + Path_origin_O

                            find_str = os.popen(grep_cmd).readlines()
                            if fi == "zygote.te":
                                print "grep_cmd = " + grep_cmd
                                print len(find_str)
                            if len(find_str) <= 0:
                                if show_head :
                                    out_file = open("./out/" + fi_d.split("/")[1] + "/" + fi,'w')
                                    show_head = False
                                    print fi_d
                                    need_porting += 1
                                #print "    " + line
                                out_file.write(line+"\n")

                        line = file.readline()
                    if out_file :
                        out_file.close()
                    file.close()
                # else:
                #     print "skip " + fi_d



                #print len(delta_files)
                #print origin_files
                # result_file = open(targetFile)
                # line = result_file.readline()

                # while line:
                #     line = result_file.readline()
                #
                # result_file.close()

def file_extension(path):
  return os.path.splitext(path)[1]

def main():
    global count
    global need_porting
    count = 0
    need_porting = 0
    detect_dir(Path_delta_N)
    print "count = " + str(count) + " need_porting = " + str(need_porting)



if __name__ == "__main__":
    main()

