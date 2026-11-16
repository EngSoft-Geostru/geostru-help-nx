"""Toglie dalle pagine pubblicate i blocchi riservati all'assistente AI.

Una pagina del manuale può contenere, nella sezione a cui si riferiscono, parti scritte solo per l'assistente:

    <!-- riservato -->
    ... testo per l'assistente AI ...
    <!-- /riservato -->

L'hook gira su `on_page_markdown`, cioè prima che la pagina diventi HTML: il testo tolto non arriva né alla pagina né
all'indice di ricerca, che si costruisce dalle pagine già ripulite. Vale per tutte le lingue, perché il plugin i18n
fa passare ogni pagina di ogni lingua da questo evento.

A prova di errore: se nella pagina c'è un segno spaiato (un'apertura senza chiusura, una chiusura senza apertura, due
aperture di fila) non si prova a indovinare dove finisce il riservato. La pagina esce «in revisione», senza testo.
Dopo la costruzione, `_shared/tools/controlla_riservato.py` blocca la pubblicazione se nel sito compare ancora un segno.

Si attiva nel mkdocs.yml del prodotto con:

    hooks:
      - ../_shared/hooks/riservato.py

I manuali che hanno parti riservate le tengono in un repository privato e qui arrivano già ripuliti: questo hook è la
rete di sicurezza contro un blocco finito nel repository pubblico per errore.
"""

import logging
import re

log = logging.getLogger("mkdocs.hooks.riservato")

# Tollera spazi e maiuscole: <!--riservato-->, <!-- Riservato -->, <!-- /riservato -->.
SEGNO = re.compile(r"<!--\s*(/?)\s*riservato\s*-->", re.IGNORECASE)

IN_REVISIONE = (
    "# Pagina in revisione\n\n"
    "Questa pagina è in corso di aggiornamento e tornerà disponibile a breve.\n"
)


def ripulisci(testo: str):
    """Restituisce (testo senza blocchi riservati, None) oppure (None, motivo) se i segni non sono appaiati."""
    pezzi = []
    pos = 0
    aperto = None
    for m in SEGNO.finditer(testo):
        chiusura = m.group(1) == "/"
        if not chiusura:
            if aperto is not None:
                return None, "due aperture di fila"
            pezzi.append(testo[pos:m.start()])
            aperto = m
        else:
            if aperto is None:
                return None, "chiusura senza apertura"
            aperto = None
        pos = m.end()
    if aperto is not None:
        return None, "apertura senza chiusura"
    pezzi.append(testo[pos:])
    return "".join(pezzi), None


def on_page_markdown(markdown, page, config, files, **kwargs):
    if not SEGNO.search(markdown):
        return markdown
    pulito, motivo = ripulisci(markdown)
    if pulito is None:
        # Non un warning: con --strict fermerebbe la costruzione di tutti i manuali per una pagina sola.
        log.info("pagina %s in revisione: segni riservati non appaiati (%s)", page.file.src_uri, motivo)
        return IN_REVISIONE
    return pulito
