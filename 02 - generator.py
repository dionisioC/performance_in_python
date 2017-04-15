# coding=utf-8
from memory_profiler import profile
import time
import gc

elements = 1000000
good_time = 0
bad_time = 0
own_time = 0


@profile
def generator(element_number, start_value=0):
    while start_value < element_number:
        yield start_value
        start_value += 1


@profile
def my_generator():
    return (x*2 for x in generator(elements))


@profile
def my_generator_testing():
    for loop_count in my_generator():
        foo = loop_count + 3


@profile
def good_generator():
    return (x*2 for x in xrange(elements))


@profile
def good_generator_testing():
    for loop_count in good_generator():
        foo = loop_count + 3


@profile
def bad_generator():
    return (x*2 for x in range(elements))


@profile
def bad_generator_testing():
    for loop_count in bad_generator():
        foo = loop_count + 3

start = time.time()
my_generator_testing()
end = time.time()
own_time = end - start
gc.collect()
start = time.time()
good_generator_testing()
end = time.time()
good_time = end - start
gc.collect()

start = time.time()
bad_generator_testing()
end = time.time()
bad_time = end - start


print('Good time: %s' % good_time)
print('Bad time:  %s' % bad_time)
print('Own time:  %s' % own_time)
