# python-fastrand

A pure python clone of [lemire/fastrand](https://github.com/lemire/fastrand)

## Installation

With `pip`:

```shell
pip install python-fastrand
```

From source:

```
git clone https://github.com/mukundan314/python-fastrand.git
cd python-fastrand
python setup.py install
```

## Usage

All methods are compatible with the ones in [lemire/fastrand](https://github.com/lemire/fastrand) provided in the `pyfastrand` module

```
>>> import pyfastrand
>>> pyfastrand.pcg32bounded(1000)
498
>>> pyfastrand.pcg32()
1547545700
```

## Benchmarks

Speed of functions when gernerating a random number in the range of 0 to 1000

```shell
$ bash benchmark.sh
_random.Random().random
2000000 loops, best of 5: 156 nsec per loop

fastrand.pcg32
2000000 loops, best of 5: 137 nsec per loop

fastrand.pcg32bounded
5000000 loops, best of 5: 78.2 nsec per loop

os.urandom
500000 loops, best of 5: 865 nsec per loop

pyfastrand.pcg32
500000 loops, best of 5: 634 nsec per loop

pyfastrand.pcg32bounded
500000 loops, best of 5: 749 nsec per loop

random.randint
500000 loops, best of 5: 822 nsec per loop

random.random
2000000 loops, best of 5: 169 nsec per loop
```
