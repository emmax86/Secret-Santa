#!/usr/local/bin/python
import sys
from collections import namedtuple
from random import shuffle, choice
import itertools

Person = namedtuple('Person', ['Name'])

def valid(a, b):
    for i, j in itertools.izip(a, b):
        if i == j: return False
    return True

def main():
    people = set([Person(Name=l.strip()) for l in sys.stdin.readlines()])
    if people < 3:
        print "What a shit Secret Santa"
        return
    sending = set(people)
    receiving = set(people)

    pairings = dict()

    while len(sending) > 3:
        # Get a random recipient
        recipient = choice(tuple(receiving))

        # Get a random sender from the pool of senders, other than the recipient
        sender = sending.difference(set([recipient])).pop()
        # Remove these people from the list of potential partners
        receiving.remove(recipient)
        sending.remove(sender)

        # Pair the two
        pairings[recipient] = sender

    receiving = list(receiving)
    sending = list(sending)
    while not valid(receiving, sending):
        shuffle(receiving)
    for i in range(len(sending)):
        pairings[receiving[i]] = sending[i]

    for key, value in pairings.iteritems():
        print "{0} buys a gift for {1}".format(key.Name, value.Name)


if __name__ == '__main__':
    main()
