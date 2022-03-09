#!/usr/bin/env python3

"""Unit tests for Bulgarian G2P."""

import unittest

import bul_g2p


class G2PTest(unittest.TestCase):
    def rewrites(self, istring: str, expected_ostring: str) -> None:
        """Asserts that the g2p rule produces the correct output.
        Args:
            istring: the input string
            expected_ostring: the expected output string.
        """
        ostring = bul_g2p.g2p(istring)
        self.assertEqual(ostring, expected_ostring)

    def test_abdication(self):
        self.rewrites("абдикацията", "abd̪ikat͡sijat̪ə")

    def test_senior(self):
        self.rewrites("абитуриентският", "abit̪uriɛnskijat̪")

    def test_authority(self):
        self.rewrites("авторитетният", "aft̪orit̪ɛt̪nijat̪")

    def test_bombard(self):
        self.rewrites("бомбардиралото", "bombard̪iraɫot̪o")

    def test_dinner(self):
        self.rewrites("вечеряхте", "vɛt͡ʃɛrjaxt̪ɛ")

    def test_homem(self):
        self.rewrites("въвежданията", "vəvɛʒd̪anijat̪ə")

    def test_husbandry(self):
        self.rewrites("господарствай", "ɡospod̪arst̪vaj")

    def test_border(self):
        self.rewrites("граничещото", "ɡranit͡ʃɛʃt̪ot̪o")

    def test_chew(self):
        self.rewrites("дъвчете", "d̪əft͡ʃɛt̪ɛ")

    def test_extract(self):
        self.rewrites("извличайте", "izvlit͡ʃajt̪ɛ")

    def test_crowning(self):
        self.rewrites("коронясващото", "koronjasvaʃt̪ot̪o")

    def test_callers(self):
        self.rewrites("наричащите", "nərit͡ʃaʃt̪it̪ɛ")

    def test_resulted(self):
        self.rewrites("произтечеха", "proist̪ɛt͡ʃɛxə")

    def test_cry(self):
        self.rewrites("разплачат", "rəspɫat͡ʃət̪")


        
if __name__ == "__main__":
    unittest.main()
