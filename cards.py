#!/usr/bin/env python3

import sys
import random
import timeit

ITERATIONS = 1000000
DECKS = 1
DECK_SIZE = 52
GOOD_CARDS = 4  # per deck
NUM_HANDS = 4
HAND_SIZE = 5
WIN_CONDITION = 2  # number of good cards wanted in a hand

def deal(deck, num_hands, hand_size):
    #breakpoint()
    deck, leftovers = deck[:num_hands*hand_size], deck[num_hands*hand_size:]
    hands = [deck[i::num_hands] for i in range(num_hands)]
    return hands, leftovers

def play():
    #deck = [1] * GOOD_CARDS + [0] * (DECK_SIZE - GOOD_CARDS)
    #deck = deck * DECKS
    #random.shuffle(deck)
    deck = [0] * (DECKS * DECK_SIZE)
    for i in random.sample(range(len(deck)), DECKS * GOOD_CARDS):
        deck[i] = 1
    hands, deck = deal(deck, NUM_HANDS, HAND_SIZE)
    #breakpoint()
    #print(hands)
    hand_sums = list(map(sum, hands))
    #print(hand_sums)
    winners = list(map(lambda x: x >= WIN_CONDITION, hand_sums))
    #print(winners)
    num_winners = sum(winners)
    return num_winners

def main():
    num_winners = 0
    start = timeit.default_timer()
    for i in range(ITERATIONS):
        num_winners += play()
    end = timeit.default_timer()
    print(f'{num_winners} winners in {ITERATIONS} iterations')
    print(f'{100*num_winners/ITERATIONS}% chance of _____')
    print(f'ran in {end - start} seconds')
    #breakpoint()

if __name__ == '__main__':
    sys.exit(main())
