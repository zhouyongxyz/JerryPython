import os;
# -*- coding: UTF-8 -*-

src_path="/home/zhouyong0701/hsae/bluetooth"
aim_path="/home/zhouyong0701/tmp/hsae/bluetooth/bluetooth"

def main():
    #递归遍历 root目录下所有文件
    list_dir(aim_path)
    print "generate report ..."
    lcov = "lcov -c -b " + src_path + " --gcov-tool /home/zhouyong0701/tmp/hsae/gcov-4.8 -d " + aim_path + " -o report.info";
    os.system(lcov);
    os.system("genhtml report.info -o ./result");

def list_dir(filepath):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            list_dir(fi_d)
        else:
            if file_extension(fi) == ".gcda" :
                targetFile = os.path.join(filepath, fi_d)
                #print targetFile
                targetFile = targetFile.replace("gcda","gcno")
                #print targetFile
                #print aim_path + sourceFile[len(src_path):]
                sourceFile = src_path + targetFile[len(aim_path):]
                print "cp " + sourceFile + " --> " + targetFile
                open(targetFile, "wb").write(open(sourceFile, "rb").read())

def file_extension(path):
  return os.path.splitext(path)[1]


if __name__ == "__main__":
    main()