#!/usr/bin/env python3

"""Bulgarian g2p rules."""

import pynini

from pynini.lib import rewrite


_g = pynini.union(
    "а",
    "б",
    "в",
    "г",
    "д",
    "е",
    "ж",
    "з",
    "и",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "щ",
    "ъ",
    "ь",
    "ю",
    "я",
)
_p = pynini.union(
    "a",
    "ə",
    "b",
    "v",
    "ɡ",
    "d",
    "ɛ",
    "ʒ",
    "z",
    "i",
    "j",
    "k",
    "l",
    "ɫ",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "t̪",
    "u",
    "f",
    "x",
    "ts",
    "tʃ",
    "ʃ",
    "ʃt",
    "ju",
    "ja",
)

SIGMA_STAR = pynini.union(_g, _p).closure().optimize()

G2P = (
    pynini.cdrewrite(
        pynini.cross("а", "a")
        | pynini.cross("б", "b")
        | pynini.cross("в", "v")
        | pynini.cross("г", "ɡ")
        | pynini.cross("д", "d")
        | pynini.cross("е", "ɛ")
        | pynini.cross("ж", "ʒ")
        | pynini.cross("з", "z")
        | pynini.cross("и", "i")
        | pynini.cross("й", "j")
        | pynini.cross("к", "k")
        | pynini.cross("л", "ɫ")
        | pynini.cross("м", "m")
        | pynini.cross("н", "n")
        | pynini.cross("р", "r")
        | pynini.cross("п", "p")
        | pynini.cross("с", "s")
        | pynini.cross("т", "t")
        | pynini.cross("у", "u")
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
    @ pynini.cdrewrite(
        pynini.cross("a", "ə"), "", pynini.union("[EOS]"), SIGMA_STAR
    ).optimize()
    @ pynini.cdrewrite(
        pynini.cross("u", "o"),
        pynini.union("[BOS]"),
        pynini.union("b", "v", "d", "n", "x", "ʃ"),
        SIGMA_STAR,
    ).optimize()
    @ pynini.cdrewrite(
        pynini.cross("b", "p"), "a", pynini.union("s", "x"), SIGMA_STAR
    ).optimize()
    @ pynini.cdrewrite(
        pynini.cross("v", "f"), "ə", "tʃ", SIGMA_STAR
    ).optimize()
    @ pynini.cdrewrite(
        pynini.cross("v", "f"), "a", pynini.union("s", "t", "k"), SIGMA_STAR
    ).optimize()
    @ pynini.cdrewrite(
        pynini.cross("ɫ", "l"), "", pynini.union("ɛ", "i"), SIGMA_STAR
    ).optimize()
    @ pynini.cdrewrite(
        pynini.cross("z", "s"), pynini.union("a", "ə"), "p", SIGMA_STAR
    ).optimize()
    @ pynini.cdrewrite(
        pynini.cross("z", "s"),
        "i",
        pynini.union("ɫ", "t", "s", "tʃ"),
        SIGMA_STAR,
    ).optimize()
    @ pynini.cdrewrite(pynini.cross("d", "t"), "ɛ", "s", SIGMA_STAR).optimize()
).optimize()


def g2p(istring: str) -> str:
    return rewrite.one_top_rewrite(istring, G2P)
