import os

__all__ = ['xorshift128plus', 'xorshift128plus_seed1', 'xorshift128plus_seed2']

seed = [
    int.from_bytes(os.urandom(8), 'big'),
    int.from_bytes(os.urandom(8), 'big')
]


def xorshift128plus():
    global seed

    s0 = (seed[0] ^ (s0 << 23)) & 0xffffffffffffffff
    seed = [seed[1], seed[1] ^ s0 ^ (seed[1] >> 18) ^ (s0 >> 5)]

    return seed[1] + s0


def xorshift128plus_seed1(seed1):
    seed[0] = seed1


def xorshift128plus_seed2(seed2):
    seed[1] = seed2
