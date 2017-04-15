# coding=utf-8
import time

elements = 1000000
good_time = 0
bad_time = 0
tricky_good_time = 0
tricky_bad_time = 0

my_set = {value for value in range(elements)}
my_list = [value for value in range(elements)]

start = time.time()
999999 in my_set
end = time.time()
good_time = end - start

start = time.time()
999999 in my_list
end = time.time()
bad_time = end - start

start = time.time()
5 in my_set
end = time.time()
tricky_good_time = end - start

start = time.time()
5 in my_list
end = time.time()
tricky_bad_time = end - start

print('Good time: %s' % good_time)
print('Bad time:  %s' % bad_time)
print('Tricky good time: %s' % tricky_good_time)
print('Tricky bad time:  %s' % tricky_bad_time)
