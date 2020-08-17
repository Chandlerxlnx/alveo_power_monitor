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
        print 'Usage: python file_name(.xls),  gap_time(seconds), points'
        exit(1)

    file_name = sys.argv[1]
    gap_time = sys.argv[2]
    points = sys.argv[3]

    # create recoder file
    rec = open(file_name, 'w')
    rec.write('card0_pwr\t card_pwr\t time\n')

    # prepare env
    os.system('source /opt/xilinx/xrt/setup.sh')

    number = 1

    while True:

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

        rec.write(card0_pwr["board"]["physical"]["power"])
        rec.write('\t')
        rec.write(card1_pwr["board"]["physical"]["power"])
        rec.write('\t')
        rec.write(str(datetime.datetime.now()))
        rec.write('\n')

        time.sleep(int(gap_time))

        # judge return
        number = number + 1
        if number > int(points):
            print "test finish"
            exit(0)
