"""Controllo dopo la costruzione: nessun segno di blocco riservato deve arrivare nel sito pubblicato.

Uso: python3 _shared/tools/controlla_riservato.py _site
Esce con 1 (e il workflow non pubblica) se in un file del sito compare un segno «<!-- riservato» in qualunque forma:
così com'è, con l'HTML che lo trasforma in &lt;, o dentro l'indice di ricerca JSON (\\u003c).
"""

import pathlib
import re
import sys

SEGNI = re.compile(
    r"(<|&lt;|&#60;|\\u003c|\\x3c)!--\s*/?\s*riservato",
    re.IGNORECASE,
)
ESTENSIONI = {".html", ".htm", ".json", ".js", ".xml", ".txt", ".md"}


def main(radice: str) -> int:
    trovati = []
    for f in pathlib.Path(radice).rglob("*"):
        if f.is_file() and f.suffix.lower() in ESTENSIONI:
            testo = f.read_text(encoding="utf-8", errors="ignore")
            if SEGNI.search(testo):
                trovati.append(str(f))
    if trovati:
        print("ERRORE: segni di blocchi riservati nel sito costruito, pubblicazione bloccata:")
        for t in trovati:
            print("  " + t)
        return 1
    print("Controllo riservato: nessun segno nel sito.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "_site"))
