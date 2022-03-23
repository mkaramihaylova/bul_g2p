#!/usr/bin/env python3

""" Predicts transcription based on g2p. """

import argparse
import bul_g2p
import csv


def main(args: argparse.Namespace) -> None:
    with open(args.input, "r") as file:
        with open(args.output, "w") as column_1:
            source = csv.reader(file, delimiter="\t")
            for graphemes, phonemes in source:
                print(bul_g2p.g2p(graphemes), file=column_1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input file path")
    parser.add_argument("output", help="prediction file path")
    main(parser.parse_args())