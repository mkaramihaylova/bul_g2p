#!/usr/bin/env python3

"""Unit tests for Bulgarian g2p."""

import unittest

import bul_g2p


class G2PTest(unittest.TestCase):
    def rewrites(self, istring: str, expected_ostring: str) -> None:

        ostring = bul_g2p.g2p(istring)
        self.assertEqual(ostring, expected_ostring)

    def test_abdication(self):
        self.rewrites("абдикацията", "abdikatsijatə")

    def test_authority(self):
        self.rewrites("авторитетният", "aftoritɛtnijat")

    def test_bombard(self):
        self.rewrites("бомбардиралото", "bombardiraɫoto")

    def test_dinner(self):
        self.rewrites("вечеряхте", "vɛtʃɛrjaxtɛ")

    def test_homem(self):
        self.rewrites("въвежданията", "vəvɛʒdanijatə")

    def test_husbandry(self):
        self.rewrites("господарствай", "ɡospodarstvaj")

    def test_border(self):
        self.rewrites("граничещото", "ɡranitʃɛʃtoto")

    def test_chew(self):
        self.rewrites("дъвчете", "dəftʃɛtɛ")

    def test_extract(self):
        self.rewrites("извличайте", "izvlitʃajtɛ")

    def test_crowning(self):
        self.rewrites("коронясващото", "koronjasvaʃtoto")

    def test_callers(self):
        self.rewrites("наричащите", "naritʃaʃtitɛ")

    def test_resulted(self):
        self.rewrites("произтечеха", "proistɛtʃɛxə")

    def test_cry(self):
        self.rewrites("разплачат", "raspɫatʃat")

    def test_lied(self):
        self.rewrites("лъженията", "ɫəʒɛnijatə")

    def test_produce(self):
        self.rewrites("възпроизвеждащото", "vəsproizvɛʒdaʃtoto")

    def test_contribute(self):
        self.rewrites("допринасящата", "doprinasjaʃtatə")

    def test_sweep(self):
        self.rewrites("замитал", "zamitaɫ")

    def test_sent(self):
        self.rewrites("пращалата", "praʃtaɫatə")

    def test_divine(self):
        self.rewrites("предсказвалият", "prɛtskazvalijat")

    def test_spread(self):
        self.rewrites("разпростирахте", "rasprostiraxtɛ")


if __name__ == "__main__":
    unittest.main()
