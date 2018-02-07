import os
import getopt
import sys


def del_file_from_ini(configfile):
    print "start deleting ..."
    file = open(configfile)
    line = file.readline()
    while line:
        if line[0] == '[' :
            dir = line[1:-2]
            #print dir
            line = file.readline()
            while line:
                if line[0] == '[':
                    break
                patch = line
                #print patch
                del_dir = dir + "/"  + patch
                del_cmd = 'rm ' + del_dir
                print del_cmd
                #if os.path.exists(del_dir) :
                os.system(del_cmd)
                #else:
                #    print "file not exist .."
                line = file.readline()
        else :
            line = file.readline()



def main(argv):
    configfile = "./cfg.ini"
    try:
        opts, args = getopt.getopt(argv, "hf:", ["file="])
    except getopt.GetoptError:
        print 'delete-file-from-ini.py -f <configfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'delete-file-from-ini.py -f <configfile>'
            sys.exit()
        elif opt in ("-f", "--moudle"):
            if arg != "":
                configfile = arg
    print 'config: ', configfile
    del_file_from_ini(configfile)


if __name__ == '__main__':
    main(sys.argv[1:]);