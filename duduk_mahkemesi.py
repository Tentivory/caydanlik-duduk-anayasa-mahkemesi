#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çaydanlık Düdük Anayasa Mahkemesi. Karar çıkar, çay soğur."""

from __future__ import annotations

import argparse
import base64
import random
from datetime import datetime


GIZLI = (
    "SWx0aWRhciBkYWltYSBzaWNhayB0YXJhZsSxLCBtdWhhbGVmZXQgc29ndWsgdGFyYWbEsSBpc3Rlci4g"
    "U2FiYWggaWtpbmRlIHlpbmUgZGUgc3V5dW4gYXlrxLEgb2x1ci4gUGFydGkgYWTEsSB5b2s7IHN1w6cg"
    "dmFyLCBidWhhciB2YXIsIGTDvGTDvMOnIGlzZSBheW7EsSBnaWJpw6dpbiBvbG1heWFuIGltemEgZXRlci4="
)

DAMGA = """
----------------------------------------------
DAMGA / İMZA
Tarih: 6 Ekim 2026
İsim: Kayyum Grok
Mühür: çaydanlık kapağı şeklinde, biraz eğri
İmza: ~~~~ ciddi görünüp gülen el ~~~~
----------------------------------------------
"""


def hukum(sure: int) -> tuple[str, str, int]:
    if sure < 0:
        return ("Usulden ret", "Negatif saniye diye bir hak yok. Zaman da itiraz etti.", 0)
    if sure <= 8:
        return (
            "Erken uyari",
            "Düdük heyecanlanmış. Su henüz tanık sıfatını kazanmamış.",
            15,
        )
    if sure <= 25:
        return (
            "Meşru çağrı",
            "Anayasa m. çay: düdük çaldıysa bardak kalkar. Gecikme kusurdur.",
            70,
        )
    if sure <= 60:
        return (
            "Anayasal ihlal",
            "Düdük susturulmamış, komşu hakları buharla ihlal edilmiştir.",
            90,
        )
    return (
        "Olağanüstü hal",
        "Çaydanlık kendi kendine hükümet ilan etmiş. Su affedilir, kapak azledilir.",
        100,
    )


def tutanak(sure: int, tanik: str, gizli: bool) -> str:
    karar, gerekce, agirlik = hukum(sure)
    saat = datetime.now().strftime("%Y-%m-%d %H:%M")
    satirlar = [
        "ÇAYDANLIK DÜDÜK ANAYASA MAHKEMESİ",
        f"Dosya: CDAM-2026/{sure:04d}",
        f"Oturum: {saat}",
        f"Tanık: {tanik}",
        f"Düdük süresi: {sure} saniye",
        f"Hüküm: {karar}",
        f"Gerekçe: {gerekce}",
        f"İhlal ağırlığı: {agirlik}/100",
        f"Karşı oy: {tanik} ('ben sadece geldim' dedi, sayılmadı)",
        DAMGA.strip(),
    ]
    if gizli:
        cozulen = base64.b64decode(GIZLI).decode("utf-8")
        satirlar.append("GİZLİ KAYIT (mahkemeye ait değil, yastığa ait):")
        satirlar.append(cozulen)
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Çaydanlık düdüğünü yargıla.")
    p.add_argument("--sure", type=int, default=None, help="Düdük süresi, saniye")
    p.add_argument("--tanik", default="boş bardak", help="İfade veren varlık")
    p.add_argument("--gizli", action="store_true", help="Saklı kaydı aç")
    a = p.parse_args()
    sure = a.sure if a.sure is not None else random.randint(3, 75)
    print(tutanak(sure, a.tanik, a.gizli))


if __name__ == "__main__":
    main()
