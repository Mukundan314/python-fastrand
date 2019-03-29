import os

__all__ = ['pcg32', 'pcg32bounded', 'pcg32inc', 'pcg32_seed']

state = int.from_bytes(os.urandom(8), 'big')
inc = 0xda3e39cb94b95bdb


def pcg32():
    """Generate a random (32 bit) integer using PCG."""
    global state

    xorshifted = (((state >> 18) ^ state) >> 27) & 0xffffffff
    rot = state >> 59
    state = (state * 0x5851f42d4c957f2d + inc) & 0xffffffffffffffff

    return (xorshifted >> rot) | ((xorshifted << (-rot & 31)) & 0xffffffff)


def pcg32bounded(bound):
    """Generate a random integer in the interval [0, bound] using PCG."""
    random32bits = pcg32()
    multiresult = random32bits * bound

    if (multiresult & 0xffffffff) < bound:
        threshold = ((bound - 1) ^ 0xffffffff) % bound
        while (multiresult & 0xffffffff) < threshold:
            random32bits = pcg32()
            multiresult = random32bits * bound

    return multiresult >> 32


def pcg32inc(new_inc):
    "Change the increment parameter of the PCG generator."
    global inc
    inc = new_inc | 1


def pcg32_seed(cls, new_seed):
    "Change the seed of thw PVG generator."
    global seed
    state = new_seed
