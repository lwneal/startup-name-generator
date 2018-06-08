#
# Startup name generator
#
import os
import random
import requests

TECH_BUBBLE_FACTOR = 8

words = []

# Add memorable, easy-to-pronounce cute animals
words.extend(['cat', 'dog', 'hamster', 'bat', 'puppy',
              'kitten', 'bear', 'rabbit', 'monkey',
              'fox', 'panda', 'chimp', 'goat', 'zebra'])

# Add startup buzzwords (NOTE: Refresh yearly)
words.extend(['drop', 'zen', 'box', 'dash', 'com'])
words.extend(['joy', 'crate', 'air', 'tap', 'zip'])
words.extend(['coin', 'cash', 'bird', 'flow', 'source'])

# Add tech buzzwords
words.extend(['cloud', 'net', 'deep', 'data', 'bot',
              'mind', 'lab', 'labs', 'bit', 'bubble',
              'hack', 'hub', 'crypto', 'cyber'])

# Attenuate ratio of buzzwords to normal words
words *= TECH_BUBBLE_FACTOR

# Append (the ten hundred most) common dictionary words
words.extend(open('ten_hundred_most_words.txt').read().splitlines())

# Remove contractions
words = [w for w in words if "'" not in w]

# Remove abbreviations like Mrs.
words = [w for w in words if "." not in w]

# Normalize case
words = [w.lower() for w in words]

# Remove duplicates
#words = list(set(words))


def name():
    tokens = [random.choice(words), random.choice(words), '.com']
    return ''.join(tokens)


def whois(name):
    cmd = 'whois {} | grep -v "No match for" | grep -i {} && echo That domain name is taken || echo "Congratulations, your startup name is NOT YET TAKEN!"'
    os.system(cmd.format(name, name))
    print ''


while True:
    startup = name()
    print 'is \033[32;1;1m{}\033[0m a good name (y/n)?'.format(startup)
    if raw_input().lower().startswith('y'):
        whois(startup)
