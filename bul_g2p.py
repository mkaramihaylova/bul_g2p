#!/usr/bin/env python3

"""Bulgarian g2p rules."""

import pynini

from pynini.lib import rewrite


_g = pynini.union("а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н" "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ь", "ю", "я")
_p = pynini.union("a", "ə", "b", "v", "g", "d", "d̪" "ɛ", "e", "ʒ", "z", "i", "j", "k", "l", "ɫ", "m", "n", "o", "p", "r", "s", "t", "t̪", "u", "f", "x", "ts", "tʃ", "ʃ", "ʃt", "ju", "ja")

SIGMA_STAR = pynini.union(_g,_p).closure().optimize()

G2P = (
    pynini.cdrewrite(
        pynini.cross("г", "g")
        | pynini.cross("д", "d")
        | pynini.cross("е", "e")
        | pynini.cross("ж", "ʒ")
        | pynini.cross("и", "i")
        | pynini.cross("й", "j")
        | pynini.cross("к", "k")
        | pynini.cross("м", "m")
        | pynini.cross("н", "n")
        | pynini.cross("р", "r")
        | pynini.cross("п", "p")
        | pynini.cross("с", "s")
        | pynini.cross("т", "t")
        | pynini.cross("ф", "f")
        | pynini.cross("ц", "ts")
        | pynini.cross("ч", "tʃ")
        | pynini.cross("ш", "ʃ")
        | pynini.cross("щ", "ʃt")
        | pynini.cross("ъ", "ə")
        | pynini.cross("х", "x")
        | pynini.cross("ь", "j")
        | pynini.cross("ю", "ju")
        | pynini.cross("я", "ja")
        | pynini.cross("о", "o"),
        "",
        "",
        SIGMA_STAR,
    )
    @ pynini.cdrewrite(pynini.cross("а", "ə"), "", pynini.union("[EOS]"), SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("а", "a"), "", "", SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("у", "u"), pynini.union("[BOS]"), pynini.union("м", "с", "ч"), SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("у", "o"), pynini.union("[BOS]"), "", SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("у", "u"), "", "", SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("б", "p"), "а", pynini.union("с", "х"), SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("б", "b"), "", "", SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("в", "f"), "ъ", "ч", SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("в", "f"), "а", pynini.union("с", "т", "к"), SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("в", "v"), "", "", SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("л", "l"), "", pynini.union("е", "и", "й"), SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("л", "ɫ"), "", "", SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("з", "s"), pynini.union("а", "ъ"), "п", SIGMA_STAR).optimize()
    @ pynini.cdrewrite(pynini.cross("з", "z"), "", "", SIGMA_STAR).optimize()
)


def g2p(istring: str) -> str:
    return rewrite.one_top_rewrite(istring, G2P)
