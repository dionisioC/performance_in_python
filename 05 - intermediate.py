# coding=utf-8
import time

elements = 1000000
good_time = 0
bad_time = 0


def good_intermediate():
    for loop_count in range(elements):
        print ('Hi how are you')


def bad_intermediate():
    for loop_count in range(elements):
        print ('Hi')
        print ('How')
        print ('Are')
        print ('You')

start = time.time()
good_intermediate()
end = time.time()
good_time = end - start


start = time.time()
bad_intermediate()
end = time.time()
bad_time = end - start


print('Good time: %s' % good_time)
print('Bad time:  %s' % bad_time)
