#!/usr/bin/python3
import pdb

import atheris
import sys

with atheris.instrument_imports():
    from base58 import b58encode, b58decode


@atheris.instrument_func
def TestOneInput(data):
    encoded = b58encode(data)
    decoded = b58decode(encoded)

    if data != decoded:
        pdb.set_trace()
        raise RuntimeError("Encoded and decoded data are not equal")


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
