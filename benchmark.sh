#!/bin/sh

echo "_random.Random().random"
python -m timeit -u nsec -s "import _random;random=_random.Random()" "int(random.random() * 1000)"
echo

echo "fastrand.pcg32"
python -m timeit -u nsec -s "import fastrand" "fastrand.pcg32() % 1001"
echo

echo "fastrand.pcg32bounded"
python -m timeit -u nsec -s "import fastrand" "fastrand.pcg32bounded(1001)"
echo

echo "os.urandom"
python -m timeit -u nsec -s "import os" "int.from_bytes(os.urandom(2), 'big') % 1001"
echo

echo "pyfastrand.pcg32"
python -m timeit -u nsec -s "import pyfastrand" "pyfastrand.pcg32() % 1001"
echo

echo "pyfastrand.pcg32bounded"
python -m timeit -u nsec -s "import pyfastrand" "pyfastrand.pcg32bounded(1001)"
echo

echo "random.randint"
python -m timeit -u nsec -s "import random" "random.randint(0, 1000)"
echo

echo "random.random"
python -m timeit -u nsec -s "import random" "int(random.random() * 1000)"
