import time
from random import random
from string import ascii_lowercase

elements = 1000000
good_time = 0
bad_time = 0


lis = list(ascii_lowercase)
examples = [lis[int(random() * 26)] for _ in xrange(elements)]


def good_string_joiner():
    ''.join(examples)


def bad_string_joiner():
    final_string = ''
    for c in examples:
        final_string += c

start = time.time()
good_string_joiner()
end = time.time()
good_time = end - start


start = time.time()
bad_string_joiner()
end = time.time()
bad_time = end - start


print('Good time: %s' % good_time)
print('Bad time:  %s' % bad_time)

print ("Ms. %s! My %s crawled in my %s and then I %s it."
       "Can I have another one?" % ("Hoover", "worm", "mouth", "ate"))

print ("Ms. {}! My {} crawled in my {} and then I {} it."
       "Can I have another one?".format("Hoover", "worm", "mouth", "ate"))

print ("Ms. {0}! My {2} crawled in my {1} and then I {3} it."
       "Can I have another one?".format("Hoover", "worm", "mouth", "ate"))
