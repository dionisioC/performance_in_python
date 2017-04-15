# coding=utf-8
import time

elements = 1000000
attempts = 3
good_time = 0
bad_time = 0


def good_list():
    my_list = [value for value in range(elements)]


def square_good_list():
    my_list = [value * value for value in range(elements)]


def good_list_validation():
    my_list = [value for value in range(elements)
               if value % 2 == 0]


def bad_list():
    my_list = []
    for value in range(elements):
        my_list.append(value)


for x in range(0, attempts):
    start = time.time()
    good_list()
    end = time.time()
    good_time = (end - start) / attempts


for x in range(0, attempts):
    start = time.time()
    bad_list()
    end = time.time()
    bad_time = (end - start) / attempts


print('Good time: %s' % good_time)
print('Bad time:  %s' % bad_time)
