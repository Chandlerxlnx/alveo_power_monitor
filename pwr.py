#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import json
import subprocess
import datetime
import time
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print 'Usage: python file_name(must .csv suffix),  gap_time(second), points(number)'
        exit(1)

    file_name = sys.argv[1]
    gap_time = sys.argv[2]
    points = sys.argv[3]

    # to do check the

    if os.path.splitext(file_name)[-1] != '.csv':
        print os.path.splitext(file_name)[-1]
        print "the file name must be csv suffix"
        exit(1)

    # create recoder file
    rec = open(file_name, 'w')
    rec.write('card0_pwr\t card_pwr\t time\n')
    # rec.close()  # 在内容写完后关闭文件

    # prepare env
    os.system('source /opt/xilinx/xrt/setup.sh')

    number = 1

    while True:

        try:
            # get card0 power
            p0 = subprocess.Popen('xbutil dump -d 0', stdout=subprocess.PIPE, shell=True)
            output = p0.stdout.read()
            card0_pwr = json.loads(output)
            print card0_pwr["board"]["physical"]["power"]

            # get card1 power
            p1 = subprocess.Popen('xbutil dump -d 1', stdout=subprocess.PIPE, shell=True)
            output = p1.stdout.read()
            card1_pwr = json.loads(output)
            print card1_pwr["board"]["physical"]["power"]

            # with open(file_name, 'a') as rec:
            rec.write(card0_pwr["board"]["physical"]["power"])
            rec.write('\t')
            rec.write(card1_pwr["board"]["physical"]["power"])
            rec.write('\t')
            rec.write(str(datetime.datetime.now()))
            rec.write('\n')

        except:
            print ('write error')

        time.sleep(int(gap_time))

        # judge return
        number = number + 1
        if number > int(points):
            rec.close()  # 在内容写完后关闭文件
            print "test finish"
            exit(0)

