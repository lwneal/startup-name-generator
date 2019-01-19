#
# Startup name generator
#
import os
import random
import requests
import time
import math

words = []

# Add memorable, easy-to-pronounce cute animals
words.extend(['cat', 'dog', 'hamster', 'bat', 'puppy',
              'kitten', 'bear', 'rabbit', 'monkey',
              'fox', 'panda', 'chimp', 'goat', 'zebra'])

# Add startup buzzwords (NOTE: Refresh yearly)
words.extend(['drop', 'zen', 'box', 'dash', 'com'])
words.extend(['joy', 'crowd', 'crate', 'air', 'tap', 'zip'])
words.extend(['go', 'eco', 'snap', 'life', 'ly'])
words.extend(['mash', 'gig', 'ship', 'one', 'sky'])
words.extend(['coin', 'cash', 'bird', 'flow', 'source'])
words.extend(['smart', 'pin', 'zoom', 'base', 'flare'])

# Add tech buzzwords (NOTE: Refresh monthly)
words.extend(['cloud', 'net', 'deep', 'data', 'bot',
              'mind', 'lab', 'labs', 'bit', 'bubble',
              'hack', 'hub', 'crypto', 'cyber', 'auth'])

# Attenuate ratio of buzzwords to normal words based on macroeconomic conditions
def compute_tech_bubble_factor(alpha=2.8, beta=5.2, gamma=2.97272):
    return int(alpha + math.cos(beta * (time.time() / gamma * 10e8)) + 0.5)

words *= compute_tech_bubble_factor()

# Append (the ten hundred most) common dictionary words
words.extend(open('ten_hundred_most_words.txt').read().splitlines())

# Append additional words extracted from a state-of-the-art deep neural network
words.extend(open('neural_network_words.txt').read().split())

# Remove contractions
words = [w for w in words if "'" not in w]

# Remove abbreviations like Mrs.
words = [w for w in words if "." not in w]

# Normalize case
words = [w.lower() for w in words]


def name():
    tokens = [random.choice(words), random.choice(words), '.com']
    return ''.join(tokens)


def whois(name):
    taken_msg = 'That domain name is taken'
    available_msg = 'Congratulations, your startup name is NOT YET TAKEN!'
    cmd = 'whois {} | grep -v "No match for" | grep -i {} && echo {} || echo "{}"'
    os.system(cmd.format(name, name, taken_msg, available_msg))
    print ''


while True:
    startup = name()
    print 'is \033[32;1;1m{}\033[0m a good name (y/N)?'.format(startup)
    if raw_input().lower().startswith('y'):
        whois(startup)
