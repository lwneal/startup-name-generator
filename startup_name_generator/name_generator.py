#
# Startup name generator
#
import os
import random
import requests
import time
import math
import distutils

from . import gpt_describe_name

words = []

# Add memorable, easy-to-pronounce cute animals
words.extend(['cat', 'dog', 'hamster', 'bat', 'puppy',
              'kitten', 'bear', 'rabbit', 'monkey',
              'fox', 'panda', 'chimp', 'goat', 'zebra',
              'pig', 'cow', 'horse', 'lion', 'tiger',
              'elephant', 'giraffe', 'rhino', 'hippo',
              'wolf', 'deer', 'duck', 'goose', 'chicken',
              'turkey', 'penguin', 'owl', 'dolphin', 'whale',
              'shark', 'fish', 'octopus', 'crab', 'lobster',
              'frog', 'snake', 'lizard', 'ant', 'bee',
              'butterfly', 'dragonfly', 'spider', 'mosquito',
              'scorpion', 'worm', 'beetle', 'snail', 'slug',
              'mouse', 'rat', 'squirrel', 'chipmunk', 'rabbit',
              'hamster', 'gerbil', 'mole', 'gopher', 'weasel',
              'skunk', 'raccoon', 'badger', 'otter', 'mink',
              'fox', 'wolf', 'coyote', 'lynx', 'bobcat',
              'leopard', 'lion', 'tiger', 'cheetah', 'jaguar',
              'panther', 'cougar', 'kangaroo', 'koala', 'wombat',
              'wallaby', 'possum', 'platypus', 'opossum', 'kookaburra',
              'emu', 'ostrich', 'rhea', 'kiwi', 'penguin',
              'albatross', 'pelican', 'heron', 'egret', 'vulture',
              'ostrich', 'stork', 'swan', 'goose', 'duck',
              'chicken', 'turkey', 'parrot', 'puppy', 'sloth'])

# Add startup buzzwords (NOTE: Refresh yearly)
words.extend(['net', 'space', 'com', 'soft', 'my', 'list'])
words.extend(['flix', 'book', 'face', 'byte', 'pal'])
words.extend(['drop', 'zen', 'box', 'force', 'door'])
words.extend(['joy', 'crowd', 'crate', 'air', 'tap', 'dash'])
words.extend(['go', 'eco', 'snap', 'life', 'ly', 'zip'])
words.extend(['mash', 'gig', 'ship', 'one', 'sky'])
words.extend(['coin', 'cash', 'bird', 'flow', 'source'])
words.extend(['smart', 'pin', 'zoom', 'base', 'flare'])
words.extend(['block', 'chain', 'ape', 'swap', 'crypto'])
words.extend(['dream', 'bot', 'bits', 'eye', 'magic'])

# Add tech buzzwords (NOTE: Refresh monthly)
words.extend(['cloud', 'net', 'deep', 'data', 'bot',
              'mind', 'lab', 'labs', 'bit', 'bubble',
              'hack', 'hub', 'crypto', 'cyber', 'auth',
              'zoom', 'herd', 'mask', 'clear', 'flux',
              'meta', 'uni', 'sea', 'tech', 'tron',
              'word', 'bit', 'bits', 'space'])

# Attenuate ratio of buzzwords to normal words based on macroeconomic conditions
def compute_tech_bubble_factor(jerome_powell_height_m=1.78, berkshire_hathaway_pe_ratio=8.45, elon_musk_number_of_children=7.0):
    return int(jerome_powell_height_m + math.cos(berkshire_hathaway_pe_ratio * (time.time() / elon_musk_number_of_children * 10e8)) + 0.5)

words *= compute_tech_bubble_factor()

# Append (the ten hundred most) common dictionary words
filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ten_hundred_most_words.txt')
words.extend(open(filename).read().split() * 3)

# Append additional words extracted from a state-of-the-art deep neural network
filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'neural_network_words.txt')
words.extend(open(filename).read().split())

# Remove contractions
words = [w for w in words if "'" not in w]

# Remove abbreviations like Mrs.
words = [w for w in words if "." not in w]

# Normalize case
words = [w.lower() for w in words]


def name(extra_keywords=None):
    if extra_keywords:
        selected_words = words[:]
        for i in range(1000):
            selected_words.extend(extra_keywords)
    else:
        selected_words = words
    tokens = [random.choice(selected_words), random.choice(selected_words), '.com']
    return ''.join(tokens)


def whois(name):
    if not distutils.spawn.find_executable("whois"):
        print("Error: whois is not installed, cannot check for domain {}".format(name))
        return
    taken_msg = 'That domain name is taken'
    available_msg = 'Congratulations, your startup name is available!'
    cmd = 'whois {} | grep -v "No match for" | grep -i {} && echo {} || echo "{}"'
    os.system(cmd.format(name, name, taken_msg, available_msg))
    print('')


def name_with_description():
    new_name = name()
    description = gpt_describe_name.describe_name(new_name)
    return new_name, description
