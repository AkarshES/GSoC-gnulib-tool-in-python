#!/usr/bin/python
import argparse
import subprocess

def print_date():
    print "The date today(yyyy/mm/dd):"
    p = subprocess.Popen(["date","+%Y/%m/%d"])
    p.wait()


parser = argparse.ArgumentParser(description='Test Parser')                                                                                                                    
data = None
def init_parser():
    parser.add_argument("--list",action="store_true",help="print the available module names")
    parser.add_argument("--find",help="find the modules which contain the specified file")
    parser.add_argument("--import","--impor","--impo","--imp","--im","--i",dest="modules_import",help="Modules to be included",nargs="*")
    parser.add_argument("--date",action="store_true",help="pritns todays date",default=print_date)

def parse_arguments():
    global data 
    data = parser.parse_args()

def main():
    if data.date is True : print_date()
    if data.modules_import is not []: print data.modules_import

if __name__ == "__main__":
    init_parser()
    parse_arguments()
    main()
