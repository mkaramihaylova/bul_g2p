#!/usr/bin/env python3

""" Predicts transcription based on g2p. """

import argparse
import csv


def main(args: argparse.Namespace) -> None:
    with open(args.input, "r") as file:
        with open(args.output, "w") as column_1:
            source = csv.reader(file, delimiter="\t")
            for graphemes, phonemes in source:
                print("".join(phonemes.split()), file=column_1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input file path")
    parser.add_argument("output", help="no space file path")
    main(parser.parse_args())