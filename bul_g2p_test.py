#!/usr/bin/env python3

"""Unit tests for Bulgarian G2P."""

import unittest

import bul_g2p


class G2PTest(unittest.TestCase):
    def rewrites(self, istring: str, expected_ostring: str) -> None:
 
        ostring = bul_g2p.g2p(istring)
        self.assertEqual(ostring, expected_ostring)


    def test_abdication(self):
        self.rewrites("абдикацията", "abdikatsijatə")

    def test_senior(self):
        self.rewrites("абитуриентският", "abiturienskijat")

    def test_authority(self):
        self.rewrites("авторитетният", "aftoritetnijat")

    def test_bombard(self):
        self.rewrites("бомбардиралото", "bombardiraɫoto")

    def test_dinner(self):
        self.rewrites("вечеряхте", "vetʃerjaxte")

    def test_homem(self):
        self.rewrites("въвежданията", "vəvɛʒdanijatə")

    def test_husbandry(self):
        self.rewrites("господарствай", "ɡospodarstvaj")

    def test_border(self):
        self.rewrites("граничещото", "ɡranitʃeʃtoto")

    def test_chew(self):
        self.rewrites("дъвчете", "dəftʃete")

    def test_extract(self):
        self.rewrites("извличайте", "izvlitʃajte")

    def test_crowning(self):
        self.rewrites("коронясващото", "koronjasvaʃtoto")

    def test_callers(self):
        self.rewrites("наричащите", "naritʃaʃtite")

    def test_resulted(self):
        self.rewrites("произтечеха", "proistɛtʃexə")

    def test_cry(self):
        self.rewrites("разплачат", "raspɫatʃat")

    def test_slept(self):
        self.rewrites("спяхме", "spjaxme")

    def test_go(self):
        self.rewrites("тръгваш", "trəgvaʃ")

    def test_bite(self):
        self.rewrites("хапех", "xapex")

    def test_hear(self):
        self.rewrites("чу", "tʃu")


        
if __name__ == "__main__":
    unittest.main()
