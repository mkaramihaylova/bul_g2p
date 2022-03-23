#!/usr/bin/env python3

""" Calculates g2p word error rate. """


import argparse


def main(args: argparse.Namespace) -> None:
    with open(args.target, "r") as target_file:
        with open(args.prediction, "r") as prediction_file:

            target_word_list = []
            prediction_word_list = []

            for line in target_file:
                target_word_list.append(line)
            for line in prediction_file:
                prediction_word_list.append(line)

            num_not_equal = sum(
                word1 != word2
                for word1, word2 in zip(target_word_list, prediction_word_list)
            )

        wer = (num_not_equal / len(target_word_list)) * 100
        print("WER =", wer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="target file path")
    parser.add_argument("prediction", help="prediction file path")
    main(parser.parse_args())
