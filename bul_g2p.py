#!/usr/bin/env python3

"""Bulgarian g2p rules."""

import pynini

from pynini.lib import rewrite
from pynini.lib import pynutil
from pynini.lib import rewrite

#grapheme and phoneme inventories
_g = pynini.union("а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ь", "ю", "я")
_p = pynini.union("a", "ə", "b", "v", "ɡ", "d", "d̪" "ɛ", "ʒ", "z", "i", "j", "k", "l", "ɫ", "m", "n", "o", "p", "r", "s", "t", "t̪", "u", "f", "x", "t͡s", "t͡ʃ", "ʃ", "ʃt", "ju", "ja")

_sigma_star = pynini.union(_g,_p).closure().optimize()

_r1 = pynini.cdrewrite(
    pynini.string_map([
        ("г", "g"),
        ("д", "d̪"),
        ("е", "ɛ"),
        ("ж", "ʒ"),
        ("и", "i"),
        ("й", "j"),
        ("к", "k"),
        ("м", "m"),
        ("н", "n"),
        ("п", "p"),
        ("р", "r"),
        ("c", "s"),
        ("т", "t̪"),
        ("ф", "f"),
        ("ц", "t͡s"),
        ("ч", "t͡ʃ"),
        ("ш", "ʃ"),
        ("щ", "ʃt̪"),
        ("ъ", "ə"),
        ("ь", "j"),
        ("ю", "ju"),
        ("я", "ja")
    ]),
    "",
    "",
    _sigma_star,
).optimize()



_r2 = pynini.cdrewrite(pynini.cross("а", "ə"), "т", "т", _sigma_star).optimize()
_r3 = pynini.cdrewrite(pynini.cross("а", "ə"), "", pynini.union("т[EOS]", "[EOS]"), _sigma_star).optimize()

_r4 = pynini.cdrewrite(pynini.cross("у", "u"), "[BOS]", pynini.union("м", "с", "ч"), _sigma_star).optimize()
_r5 = pynini.cdrewrite(pynini.cross("у", "o"), "[BOS]", "", _sigma_star).optimize()
_r6 = pynini.cdrewrite(pynini.cross("у", "u"), "", "", _sigma_star).optimize()

_r7 = pynini.cdrewrite(pynini.cross("б", "p"), "a", pynini.union("с", "x"), _sigma_star).optimize()
_r8 = pynini.cdrewrite(pynini.cross("б", "b"), "", "", _sigma_star).optimize()

_r9 = pynini.cdrewrite(pynini.cross("в", "f"), "a", pynini.union("с", "т", "к"), _sigma_star).optimize()
_r10 = pynini.cdrewrite(pynini.cross("в", "f"), "ъ", "ч", _sigma_star).optimize()
_r11 = pynini.cdrewrite(pynini.cross("в", "v"), "", "", _sigma_star).optimize()

_r12 = pynini.cdrewrite(pynini.cross("л", "l"), "", pynini.union("e", "и", "й"), _sigma_star).optimize()
_r13 = pynini.cdrewrite(pynini.cross("л", "ɫ"), "", "", _sigma_star).optimize()

_r14 = pynini.cdrewrite(pynini.cross("з", "s"), pynini.union("a", "ъ"), "п", _sigma_star).optimize()


_rules = _r1 @ _r2 @ _r3 @ _r4 @ _r5 @ _r6 @ _r7 @ _r8 @ _r9 @ _r10 @ _r11 @ _r12 @ _r13 @ _r14

_g2p = pynini.closure(_g) @ _rules @ pynini.closure(_p)
_g2p.optimize()

def g2p(string: str) -> str:
  return rewrite.one_top_rewrite(string, _g2p)