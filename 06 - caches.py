# coding=utf-8
import time
from repoze.lru import lru_cache

elements = 1000
good_time = 0
bad_time = 0
tricky_good_time = 0
tricky_bad_time = 0


@lru_cache(maxsize=16)
def cached_expensive_function(value):
    time.sleep(0.1)
    return value * 2


def good_cache_testing():
    for loop_count in range(elements):
        cached_expensive_function(loop_count % 8)


def non_cached_expensive_function(value):
    time.sleep(0.1)
    return value * 2


def bad_cache_testing():
    for loop_count in range(elements):
        non_cached_expensive_function(loop_count % 8)


@lru_cache(maxsize=16)
def cached_inexpensive_function(value):
    return value * 2


def tricky_good_cache_testing():
    for loop_count in range(elements):
        cached_inexpensive_function(loop_count % 8)


def non_cached_inexpensive_function(value):
    return value * 2


def tricky_bad_cache_testing():
    for loop_count in range(elements):
        non_cached_inexpensive_function(loop_count % 8)


start = time.time()
good_cache_testing()
end = time.time()
good_time = end - start


start = time.time()
bad_cache_testing()
end = time.time()
bad_time = end - start


start = time.time()
tricky_good_cache_testing()
end = time.time()
tricky_good_time = end - start


start = time.time()
tricky_bad_cache_testing()
end = time.time()
tricky_bad_time = end - start

print('Good time: %s' % good_time)
print('Bad time:  %s' % bad_time)
print('Tricky good time: %s' % tricky_good_time)
print('Tricky bad time:  %s' % tricky_bad_time)
