#!/usr/bin/python3
#coding=utf-8

import datetime

def get_begin_time(file):
    t2 = datetime.datetime.now()
    f = open(file, "r")
    s = f.readline().replace('\n', '')
    f.close()

    t1 = datetime.datetime.fromisoformat(s)
    d = t2 - t1

    print("开始时间：%s" % str(t1))
    print("结束时间：%s" % str(t2))
    print("耗时: %d秒，%d微秒" % (d.seconds, d.microseconds))


if __name__=="__main__":
    get_begin_time(r'./a.txt')

