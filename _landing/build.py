#!/usr/bin/env python3
"""Genera la landing di help.nx.geostru.ai in tutte le lingue supportate.

Uso: python3 _landing/build.py <out_dir>
Scrive <out_dir>/index.html (italiano) e <out_dir>/<lang>/index.html per le
altre lingue. Nessuna dipendenza esterna.
"""
import sys
from pathlib import Path

LANGS = ['it', 'en', 'de', 'fr', 'es', 'ro', 'pl']
FLAG = {'it': '🇮🇹', 'en': '🇬🇧', 'de': '🇩🇪', 'fr': '🇫🇷',
        'es': '🇪🇸', 'ro': '🇷🇴', 'pl': '🇵🇱'}

# ---------------------------------------------------------------- app e categorie

APPS = {
    'computo': dict(name='Computo NX', langs=['it'], desc={
        'it': 'Computo metrico estimativo + AI',
        'en': 'Bill of quantities and cost estimating + AI',
        'de': 'Mengen- und Kostenermittlung + KI',
        'fr': 'Métré et estimation des coûts + IA',
        'es': 'Mediciones y presupuestos + IA',
        'ro': 'Antemăsurătoare și deviz + AI',
        'pl': 'Przedmiar i kosztorys + AI'}),
    'rpd': dict(name='RPD NX', langs=['it', 'en'], desc={
        'it': 'Sovrastrutture stradali (AASHTO 1993, Ivanov, Westergaard)',
        'en': 'Road pavement design (AASHTO 1993, Ivanov, Westergaard)',
        'de': 'Straßenoberbau-Bemessung (AASHTO 1993, Ivanov, Westergaard)',
        'fr': 'Dimensionnement de chaussées (AASHTO 1993, Ivanov, Westergaard)',
        'es': 'Diseño de firmes (AASHTO 1993, Ivanov, Westergaard)',
        'ro': 'Dimensionarea structurilor rutiere (AASHTO 1993, Ivanov, Westergaard)',
        'pl': 'Projektowanie nawierzchni drogowych (AASHTO 1993, Ivanov, Westergaard)'}),
    'gdw': dict(name='GDW NX', langs=['it'], desc={
        'it': 'Muri di sostegno in gabbioni (NTC 2018)',
        'en': 'Gabion retaining walls (NTC 2018)',
        'de': 'Stützmauern aus Gabionen (NTC 2018)',
        'fr': 'Murs de soutènement en gabions (NTC 2018)',
        'es': 'Muros de contención de gaviones (NTC 2018)',
        'ro': 'Ziduri de sprijin din gabioane (NTC 2018)',
        'pl': 'Mury oporowe z gabionów (NTC 2018)'}),
    'liquiter': dict(name='LiquiTer NX', langs=['it', 'en'], desc={
        'it': 'Analisi liquefazione (Seed, Boulanger-Idriss)',
        'en': 'Liquefaction analysis (Seed, Boulanger-Idriss)',
        'de': 'Verflüssigungsanalyse (Seed, Boulanger-Idriss)',
        'fr': 'Analyse de liquéfaction (Seed, Boulanger-Idriss)',
        'es': 'Análisis de licuefacción (Seed, Boulanger-Idriss)',
        'ro': 'Analiza lichefierii (Seed, Boulanger-Idriss)',
        'pl': 'Analiza upłynnienia gruntu (Seed, Boulanger-Idriss)'}),
    'maps': dict(name='Maps NX', langs=['it', 'en'], desc={
        'it': 'Cartografia, quote dal modello del terreno, sezioni ed esportazione CAD',
        'en': 'Mapping, terrain-model elevations, sections and CAD export',
        'de': 'Kartografie, Höhen aus dem Geländemodell, Schnitte und CAD-Export',
        'fr': 'Cartographie, altitudes du modèle de terrain, coupes et export CAO',
        'es': 'Cartografía, cotas del modelo del terreno, secciones y exportación CAD',
        'ro': 'Cartografie, cote din modelul terenului, secțiuni și export CAD',
        'pl': 'Kartografia, wysokości z modelu terenu, przekroje i eksport CAD'}),
    'mre': dict(name='MRE NX', langs=['it', 'en'], desc={
        'it': 'Opere di sostegno in terra rinforzata: verifiche, tieback/compound',
        'en': 'Reinforced-soil retaining structures: checks, tieback/compound',
        'de': 'Stützbauwerke aus bewehrter Erde: Nachweise, Tieback/Compound',
        'fr': 'Ouvrages de soutènement en terre renforcée : vérifications, tieback/compound',
        'es': 'Estructuras de contención en tierra reforzada: verificaciones, tieback/compound',
        'ro': 'Lucrări de sprijin din pământ armat: verificări, tieback/compound',
        'pl': 'Konstrukcje oporowe z gruntu zbrojonego: weryfikacje, tieback/compound'}),
    'loadcap': dict(name='Loadcap NX', langs=['it', 'en'], desc={
        'it': 'Capacità portante e cedimenti delle fondazioni superficiali',
        'en': 'Bearing capacity and settlement of shallow foundations',
        'de': 'Tragfähigkeit und Setzungen von Flachgründungen',
        'fr': 'Capacité portante et tassements des fondations superficielles',
        'es': 'Capacidad portante y asientos de cimentaciones superficiales',
        'ro': 'Capacitatea portantă și tasările fundațiilor de suprafață',
        'pl': 'Nośność i osiadanie fundamentów bezpośrednich'}),
    'seismic': dict(name='PS Advanced NX', langs=['it'], desc={
        'it': 'Pericolosità sismica NTC 2018: parametri, spettri, coefficienti',
        'en': 'Seismic hazard to NTC 2018: parameters, spectra, coefficients',
        'de': 'Seismische Gefährdung nach NTC 2018: Parameter, Spektren, Beiwerte',
        'fr': 'Aléa sismique NTC 2018 : paramètres, spectres, coefficients',
        'es': 'Peligrosidad sísmica NTC 2018: parámetros, espectros, coeficientes',
        'ro': 'Hazard seismic NTC 2018: parametri, spectre, coeficienți',
        'pl': 'Zagrożenie sejsmiczne wg NTC 2018: parametry, spektra, współczynniki'}),
    'rsl': dict(name='RSL III', langs=['it', 'en'], desc={
        'it': 'Risposta sismica locale 1D',
        'en': '1D local seismic response',
        'de': 'Seismische 1D-Standortantwort',
        'fr': 'Réponse sismique locale 1D',
        'es': 'Respuesta sísmica local 1D',
        'ro': 'Răspuns seismic local 1D',
        'pl': 'Lokalna odpowiedź sejsmiczna 1D'}),
    'srs': dict(name='SRS NX', langs=['it', 'en'], desc={
        'it': 'Chiodatura corticale dei versanti (soil nailing) + rete di facciata',
        'en': 'Slope surface soil nailing + facing mesh',
        'de': 'Oberflächennahe Hangvernagelung (Soil Nailing) + Frontnetz',
        'fr': 'Clouage superficiel des talus (soil nailing) + grillage de parement',
        'es': 'Soil nailing superficial de taludes + malla de revestimiento',
        'ro': 'Ancorarea de suprafață a versanților (soil nailing) + plasă de fațadă',
        'pl': 'Gwoździowanie powierzchniowe skarp (soil nailing) + siatka okładzinowa'}),
    'slope': dict(name='Slope NX', langs=['it', 'en'], desc={
        'it': 'Stabilità dei pendii (LEM): Fellenius, Bishop, Janbu, Spencer, Morgenstern-Price',
        'en': 'Slope stability (LEM): Fellenius, Bishop, Janbu, Spencer, Morgenstern-Price',
        'de': 'Böschungsstabilität (LEM): Fellenius, Bishop, Janbu, Spencer, Morgenstern-Price',
        'fr': 'Stabilité des pentes (LEM) : Fellenius, Bishop, Janbu, Spencer, Morgenstern-Price',
        'es': 'Estabilidad de taludes (LEM): Fellenius, Bishop, Janbu, Spencer, Morgenstern-Price',
        'ro': 'Stabilitatea versanților (LEM): Fellenius, Bishop, Janbu, Spencer, Morgenstern-Price',
        'pl': 'Stateczność skarp (LEM): Fellenius, Bishop, Janbu, Spencer, Morgenstern-Price'}),
    'gms': dict(name='GMS NX', langs=['it'], desc={
        'it': 'Rilievo geomeccanico, stereonet, Markland',
        'en': 'Geomechanical survey, stereonet, Markland',
        'de': 'Gebirgsmechanische Aufnahme, Stereonetz, Markland',
        'fr': 'Levé géomécanique, stéréonet, Markland',
        'es': 'Levantamiento geomecánico, estereored, Markland',
        'ro': 'Releveu geomecanic, stereonet, Markland',
        'pl': 'Zdjęcie geomechaniczne, stereonet, Markland'}),
    'rockmechanics': dict(name='Rock Mechanics NX', langs=['it', 'en'], desc={
        'it': 'Classificazioni geomeccaniche (RMR·Q·SMR) + stabilità planare/cuneo',
        'en': 'Rock mass classifications (RMR·Q·SMR) + planar/wedge stability',
        'de': 'Gebirgsklassifikationen (RMR·Q·SMR) + Planar-/Keilstabilität',
        'fr': 'Classifications géomécaniques (RMR·Q·SMR) + stabilité plane/dièdre',
        'es': 'Clasificaciones geomecánicas (RMR·Q·SMR) + estabilidad planar/cuña',
        'ro': 'Clasificări geomecanice (RMR·Q·SMR) + stabilitate planară/pană',
        'pl': 'Klasyfikacje górotworu (RMR·Q·SMR) + stateczność płaska/klinowa'}),
    'rockplane': dict(name='RockPlane NX', langs=['it', 'en'], desc={
        'it': 'Stabilità pendii rocciosi planari (Hoek-Bray)',
        'en': 'Planar rock slope stability (Hoek-Bray)',
        'de': 'Stabilität ebener Felsböschungen (Hoek-Bray)',
        'fr': 'Stabilité des pentes rocheuses planes (Hoek-Bray)',
        'es': 'Estabilidad de taludes rocosos planares (Hoek-Bray)',
        'ro': 'Stabilitatea versanților stâncoși plani (Hoek-Bray)',
        'pl': 'Stateczność płaskich zboczy skalnych (Hoek-Bray)'}),
    'hid': dict(name='HID NX', langs=['it', 'en', 'de', 'fr', 'ro', 'es', 'pl'], desc={
        'it': 'Invarianza idraulica: dimensionamento dei sistemi di laminazione',
        'en': 'Hydraulic invariance: detention system design',
        'de': 'Hydraulische Invarianz: Bemessung von Rückhaltesystemen',
        'fr': 'Invariance hydraulique : dimensionnement des systèmes de rétention',
        'es': 'Invariancia hidráulica: diseño de sistemas de laminación',
        'ro': 'Invarianță hidraulică: dimensionarea sistemelor de retenție',
        'pl': 'Inwariancja hydrauliczna: wymiarowanie zbiorników retencyjnych'}),
    'hydrogeo': dict(name='Hydrogeo NX', langs=['it'], desc={
        'it': 'Idrogeologia, pluvio, deflusso',
        'en': 'Hydrogeology, rainfall, runoff',
        'de': 'Hydrogeologie, Niederschlag, Abfluss',
        'fr': 'Hydrogéologie, pluviométrie, ruissellement',
        'es': 'Hidrogeología, pluviometría, escorrentía',
        'ro': 'Hidrogeologie, pluviometrie, scurgere',
        'pl': 'Hydrogeologia, opady, odpływ'}),
    'runofflab': dict(name='Runoff Lab NX', langs=['it', 'en'], desc={
        'it': 'Curve di pioggia, IDF',
        'en': 'Rainfall curves, IDF',
        'de': 'Regenkurven, IDF',
        'fr': 'Courbes de pluie, IDF',
        'es': 'Curvas de lluvia, IDF',
        'ro': 'Curbe de ploaie, IDF',
        'pl': 'Krzywe deszczu, IDF'}),
    'dynprobe': dict(name='Dynamic Probing NX', langs=['it', 'en', 'ro', 'es', 'fr'], desc={
        'it': 'Prove penetrometriche DPL·DPM·DPH·DPSH + SPT in foro',
        'en': 'Dynamic probing DPL·DPM·DPH·DPSH + borehole SPT',
        'de': 'Rammsondierungen DPL·DPM·DPH·DPSH + SPT im Bohrloch',
        'fr': 'Essais de pénétration DPL·DPM·DPH·DPSH + SPT en forage',
        'es': 'Ensayos de penetración DPL·DPM·DPH·DPSH + SPT en sondeo',
        'ro': 'Penetrări dinamice DPL·DPM·DPH·DPSH + SPT în foraj',
        'pl': 'Sondowania dynamiczne DPL·DPM·DPH·DPSH + SPT w otworze'}),
    'trispace': dict(name='Trispace NX', langs=['it'], desc={
        'it': 'CAD web 2D/3D + drone → GEOROCK3D',
        'en': '2D/3D web CAD + drone → GEOROCK3D',
        'de': '2D/3D-Web-CAD + Drohne → GEOROCK3D',
        'fr': 'CAO web 2D/3D + drone → GEOROCK3D',
        'es': 'CAD web 2D/3D + dron → GEOROCK3D',
        'ro': 'CAD web 2D/3D + dronă → GEOROCK3D',
        'pl': 'CAD web 2D/3D + dron → GEOROCK3D'}),
    'geosection': dict(name='GeoSection NX', langs=['it', 'en'], desc={
        'it': 'Sezioni geologiche',
        'en': 'Geological cross-sections',
        'de': 'Geologische Profile',
        'fr': 'Coupes géologiques',
        'es': 'Cortes geológicos',
        'ro': 'Secțiuni geologice',
        'pl': 'Przekroje geologiczne'}),
    'stratigrapher': dict(name='Stratigrapher NX', langs=['it'], desc={
        'it': 'Colonne stratigrafiche',
        'en': 'Stratigraphic logs',
        'de': 'Schichtenverzeichnisse',
        'fr': 'Colonnes stratigraphiques',
        'es': 'Columnas estratigráficas',
        'ro': 'Coloane stratigrafice',
        'pl': 'Profile stratygraficzne'}),
}

CATEGORIES = [
    ('general', ['computo']),
    ('engineering', ['rpd']),
    ('geotech', ['gdw', 'liquiter', 'loadcap', 'mre', 'seismic', 'rsl', 'slope', 'srs']),
    ('rock', ['gms', 'rockmechanics', 'rockplane']),
    ('hydro', ['hid', 'hydrogeo', 'runofflab']),
    ('insitu', ['dynprobe']),
    ('topo', ['trispace']),
    ('geology', ['geosection', 'stratigrapher']),
]

CAT_NAMES = {
    'general':     dict(it='Generale', en='General', de='Allgemein', fr='Général', es='General', ro='General', pl='Ogólne'),
    'engineering': dict(it='Ingegneria', en='Engineering', de='Ingenieurwesen', fr='Ingénierie', es='Ingeniería', ro='Inginerie', pl='Inżynieria'),
    'geotech':     dict(it='Geotecnica e Geologia', en='Geotechnics &amp; Geology', de='Geotechnik &amp; Geologie', fr='Géotechnique et géologie', es='Geotecnia y geología', ro='Geotehnică și geologie', pl='Geotechnika i geologia'),
    'rock':        dict(it='Meccanica delle Rocce', en='Rock Mechanics', de='Felsmechanik', fr='Mécanique des roches', es='Mecánica de rocas', ro='Mecanica rocilor', pl='Mechanika skał'),
    'hydro':       dict(it='Idrogeologia e Idraulica', en='Hydrogeology &amp; Hydraulics', de='Hydrogeologie &amp; Hydraulik', fr='Hydrogéologie et hydraulique', es='Hidrogeología e hidráulica', ro='Hidrogeologie și hidraulică', pl='Hydrogeologia i hydraulika'),
    'insitu':      dict(it='Prove in Situ', en='In-Situ Tests', de='In-situ-Versuche', fr='Essais in situ', es='Ensayos in situ', ro='Încercări in situ', pl='Badania in situ'),
    'topo':        dict(it='Topografia', en='Topography', de='Topographie', fr='Topographie', es='Topografía', ro='Topografie', pl='Topografia'),
    'geology':     dict(it='Geologia', en='Geology', de='Geologie', fr='Géologie', es='Geología', ro='Geologie', pl='Geologia'),
}


def app_count(lang, n):
    words = {
        'it': lambda n: 'app',
        'en': lambda n: 'app' if n == 1 else 'apps',
        'de': lambda n: 'App' if n == 1 else 'Apps',
        'fr': lambda n: 'appli' if n == 1 else 'applis',
        'es': lambda n: 'app' if n == 1 else 'apps',
        'ro': lambda n: 'aplicație' if n == 1 else 'aplicații',
        'pl': lambda n: 'aplikacja' if n == 1 else ('aplikacje' if 2 <= n <= 4 else 'aplikacji'),
    }
    return f'{n} {words[lang](n)}'


# ---------------------------------------------------------------- stringhe

S = {
'it': dict(
    title='Manuali GeoStru NX',
    meta='Documentazione delle applicazioni web GeoStru NX: geotecnica, geologia, meccanica delle rocce, idraulica, topografia. Una piattaforma EngSoft.',
    lang_nav='Lingua',
    eyebrow='GeoStru AI · una piattaforma EngSoft',
    h1='Manuali GeoStru NX',
    lede1="<strong>GeoStru AI</strong> è la piattaforma cloud di <strong>ENGSOFT SRL</strong> che porta il calcolo geotecnico, geologico e idraulico nel browser: le applicazioni <strong>GeoStru NX</strong> coprono l'intero flusso di lavoro — dati, calcolo, relazione — con assistente AI integrato e senza installare nulla.",
    lede2='Si rivolgono a geologi, ingegneri, studi tecnici, imprese e pubbliche amministrazioni. Qui trovi la documentazione di ogni app, organizzata per categoria come sul <a href="https://www.geostru.ai/">sito geostru.ai</a>.',
    lede3="<strong>Lingue</strong>: i manuali si aprono in italiano; dove esistono traduzioni trovi le <strong>bandierine sulla scheda</strong>, che aprono il manuale nella lingua scelta — e in ogni manuale puoi cambiare lingua dal selettore nell'intestazione. Le schede senza bandierine sono per ora solo in italiano.",
    gd_count='spazio cloud · 3 piani',
    gd_p1="<strong>GeoDropbox</strong> è la piattaforma GIS cloud di GeoStru per l'archiviazione di documenti georeferenziati: centinaia di progetti su mappa, colonne stratigrafiche, gestione file e ricerca AI.",
    gd_p2='È integrato nelle app NX: trovi il pulsante <strong>GeoDropbox</strong> accanto a Salva/Apri e i progetti si aprono e si salvano direttamente nel cloud — sempre disponibili da qualsiasi postazione, condivisi con il tuo studio, con interfaccia in 7 lingue. In <strong>Computo NX</strong> abilita anche i <strong>Listini custom</strong>: carichi i tuoi listini fornitore e i prezzi storici e l\'app li usa per prezzare in tempo reale, con priorità sui prezzari regionali (<a href="/computo/listini-custom/">guida</a>).',
    gd_p3='L\'abbonamento copre lo <strong>spazio file</strong> ed è separato dai crediti delle app. Si acquista dalla sezione <em>Piani GeoDropbox</em> della pagina <a href="https://www.geostru.ai/it/pricing/"><strong>geostru.ai/pricing</strong></a> con il pulsante <em>Abbonati</em> del piano scelto:',
    per_month='mese', badge='Consigliato',
    plan_base='Ideale per il singolo professionista',
    plan_plus='Spazio ampio per studi e team su più progetti',
    plan_max='Massimo spazio per studi strutturati e modelli BIM/IFC',
    pricing_url='https://www.geostru.ai/it/pricing/',
    gdpr_title='Privacy e GDPR', gdpr_count='7 lingue',
    gdpr_p1='Il servizio è fornito da <strong>ENGSOFT SRL</strong>, titolare del trattamento per i dati di account e di utilizzo; dei contenuti che carichi resti titolare tu, e GeoStru li tratta come responsabile (art. 28 GDPR) solo su tua istruzione.',
    gdpr_p2='I dati sono ospitati in <strong>UE e Svizzera</strong>, cifrati in transito e isolati per cliente; i fornitori che ci supportano (Google, Stripe) operano con propri accordi sul trattamento. La sintesi divulgativa è disponibile in 7 lingue; il testo completo e vincolante è la Privacy Policy ufficiale.',
    gdpr_link='Sintesi GDPR →', policy_link='Privacy Policy completa →',
),
'en': dict(
    title='GeoStru NX Manuals',
    meta='Documentation for the GeoStru NX web applications: geotechnics, geology, rock mechanics, hydraulics, topography. An EngSoft platform.',
    lang_nav='Language',
    eyebrow='GeoStru AI · an EngSoft platform',
    h1='GeoStru NX Manuals',
    lede1='<strong>GeoStru AI</strong> is the cloud platform by <strong>ENGSOFT SRL</strong> that brings geotechnical, geological and hydraulic engineering to the browser: the <strong>GeoStru NX</strong> applications cover the whole workflow — data, analysis, report — with a built-in AI assistant and nothing to install.',
    lede2="They are built for geologists, engineers, design offices, contractors and public authorities. Here you'll find the documentation of every app, organised by category as on <a href=\"https://www.geostru.ai/\">geostru.ai</a>.",
    lede3="<strong>Languages</strong>: manuals open in Italian; where a translation exists you'll find <strong>flags on the card</strong> opening the manual in that language — and inside each manual you can switch language from the header selector. Cards without flags are Italian-only for now.",
    gd_count='cloud storage · 3 plans',
    gd_p1="<strong>GeoDropbox</strong> is GeoStru's cloud GIS platform for storing georeferenced documents: hundreds of projects on a map, stratigraphic logs, file management and AI search.",
    gd_p2='It is built into the NX apps: you\'ll find the <strong>GeoDropbox</strong> button next to Save/Open, and projects open and save directly in the cloud — always available from any workstation, shared with your office, with a 7-language interface. In <strong>Computo NX</strong> it also enables <strong>custom price lists</strong>: upload your supplier lists and historical prices and the app uses them for real-time pricing, with priority over the regional price books (<a href="/computo/listini-custom/">guide, in Italian</a>).',
    gd_p3='The subscription covers <strong>file storage</strong> and is separate from app credits. You can buy it from the <em>GeoDropbox Plans</em> section of <a href="https://www.geostru.ai/pricing/"><strong>geostru.ai/pricing</strong></a> using the <em>Subscribe</em> button of your plan:',
    per_month='month', badge='Recommended',
    plan_base='Ideal for the individual professional',
    plan_plus='Ample space for offices and teams on multiple projects',
    plan_max='Maximum space for structured offices and BIM/IFC models',
    pricing_url='https://www.geostru.ai/pricing/',
    gdpr_title='Privacy &amp; GDPR', gdpr_count='7 languages',
    gdpr_p1='The service is provided by <strong>ENGSOFT SRL</strong>, data controller for account and usage data; you remain the controller of the content you upload, which GeoStru processes as a processor (Art. 28 GDPR) only on your instructions.',
    gdpr_p2='Data is hosted in the <strong>EU and Switzerland</strong>, encrypted in transit and isolated per customer; the providers supporting us (Google, Stripe) operate under their own data processing agreements. The plain-language summary is available in 7 languages; the full, binding text is the official Privacy Policy.',
    gdpr_link='GDPR summary →', policy_link='Full Privacy Policy →',
),
'de': dict(
    title='GeoStru NX Handbücher',
    meta='Dokumentation der GeoStru NX Web-Anwendungen: Geotechnik, Geologie, Felsmechanik, Hydraulik, Topographie. Eine EngSoft-Plattform.',
    lang_nav='Sprache',
    eyebrow='GeoStru AI · eine EngSoft-Plattform',
    h1='GeoStru NX Handbücher',
    lede1='<strong>GeoStru AI</strong> ist die Cloud-Plattform von <strong>ENGSOFT SRL</strong>, die geotechnische, geologische und hydraulische Berechnungen in den Browser bringt: die <strong>GeoStru NX</strong>-Anwendungen decken den gesamten Arbeitsablauf ab — Daten, Berechnung, Bericht — mit integriertem KI-Assistenten und ohne Installation.',
    lede2='Sie richten sich an Geologen, Ingenieure, Planungsbüros, Bauunternehmen und Behörden. Hier finden Sie die Dokumentation jeder App, nach Kategorien geordnet wie auf <a href="https://www.geostru.ai/">geostru.ai</a>.',
    lede3='<strong>Sprachen</strong>: Die Handbücher öffnen sich auf Italienisch; wo eine Übersetzung existiert, finden Sie <strong>Flaggen auf der Karte</strong>, die das Handbuch in der gewählten Sprache öffnen — und in jedem Handbuch können Sie die Sprache über die Auswahl in der Kopfzeile wechseln. Karten ohne Flaggen sind vorerst nur auf Italienisch verfügbar.',
    gd_count='Cloud-Speicher · 3 Tarife',
    gd_p1='<strong>GeoDropbox</strong> ist die Cloud-GIS-Plattform von GeoStru zur Archivierung georeferenzierter Dokumente: Hunderte Projekte auf der Karte, Schichtenverzeichnisse, Dateiverwaltung und KI-Suche.',
    gd_p2='Es ist in die NX-Apps integriert: Neben Speichern/Öffnen finden Sie die Schaltfläche <strong>GeoDropbox</strong>, und Projekte werden direkt in der Cloud geöffnet und gespeichert — von jedem Arbeitsplatz verfügbar, mit Ihrem Büro geteilt, mit Benutzeroberfläche in 7 Sprachen. In <strong>Computo NX</strong> ermöglicht es zudem <strong>eigene Preislisten</strong>: Sie laden Ihre Lieferantenlisten und historischen Preise hoch und die App nutzt sie für die Preisermittlung in Echtzeit, mit Vorrang vor den regionalen Preisverzeichnissen (<a href="/computo/listini-custom/">Anleitung, auf Italienisch</a>).',
    gd_p3='Das Abonnement deckt den <strong>Dateispeicher</strong> ab und ist von den App-Credits getrennt. Es ist im Abschnitt <em>GeoDropbox-Tarife</em> der Seite <a href="https://www.geostru.ai/pricing/"><strong>geostru.ai/pricing</strong></a> über die Schaltfläche <em>Abonnieren</em> des gewünschten Tarifs erhältlich:',
    per_month='Monat', badge='Empfohlen',
    plan_base='Ideal für Einzelanwender',
    plan_plus='Viel Speicher für Büros und Teams mit mehreren Projekten',
    plan_max='Maximaler Speicher für größere Büros und BIM/IFC-Modelle',
    pricing_url='https://www.geostru.ai/pricing/',
    gdpr_title='Datenschutz &amp; DSGVO', gdpr_count='7 Sprachen',
    gdpr_p1='Der Dienst wird von <strong>ENGSOFT SRL</strong> bereitgestellt, Verantwortlicher für Konto- und Nutzungsdaten; für die von Ihnen hochgeladenen Inhalte bleiben Sie Verantwortlicher, GeoStru verarbeitet sie als Auftragsverarbeiter (Art. 28 DSGVO) nur auf Ihre Weisung.',
    gdpr_p2='Die Daten werden in der <strong>EU und der Schweiz</strong> gehostet, bei der Übertragung verschlüsselt und pro Kunde isoliert; die uns unterstützenden Anbieter (Google, Stripe) arbeiten mit eigenen Auftragsverarbeitungsverträgen. Die verständliche Zusammenfassung ist in 7 Sprachen verfügbar; der vollständige, verbindliche Text ist die offizielle Datenschutzerklärung.',
    gdpr_link='DSGVO-Zusammenfassung →', policy_link='Vollständige Datenschutzerklärung →',
),
'fr': dict(
    title='Manuels GeoStru NX',
    meta='Documentation des applications web GeoStru NX : géotechnique, géologie, mécanique des roches, hydraulique, topographie. Une plateforme EngSoft.',
    lang_nav='Langue',
    eyebrow='GeoStru AI · une plateforme EngSoft',
    h1='Manuels GeoStru NX',
    lede1="<strong>GeoStru AI</strong> est la plateforme cloud d'<strong>ENGSOFT SRL</strong> qui amène le calcul géotechnique, géologique et hydraulique dans le navigateur : les applications <strong>GeoStru NX</strong> couvrent tout le flux de travail — données, calcul, rapport — avec assistant IA intégré et sans rien installer.",
    lede2="Elles s'adressent aux géologues, ingénieurs, bureaux d'études, entreprises et administrations publiques. Vous trouverez ici la documentation de chaque application, organisée par catégorie comme sur <a href=\"https://www.geostru.ai/\">geostru.ai</a>.",
    lede3="<strong>Langues</strong> : les manuels s'ouvrent en italien ; lorsqu'une traduction existe, vous trouverez des <strong>drapeaux sur la fiche</strong> qui ouvrent le manuel dans la langue choisie — et dans chaque manuel vous pouvez changer de langue depuis le sélecteur de l'en-tête. Les fiches sans drapeaux sont pour l'instant uniquement en italien.",
    gd_count='espace cloud · 3 offres',
    gd_p1="<strong>GeoDropbox</strong> est la plateforme SIG cloud de GeoStru pour l'archivage de documents géoréférencés : des centaines de projets sur carte, colonnes stratigraphiques, gestion de fichiers et recherche IA.",
    gd_p2="Il est intégré aux applications NX : vous trouverez le bouton <strong>GeoDropbox</strong> à côté d'Enregistrer/Ouvrir, et les projets s'ouvrent et s'enregistrent directement dans le cloud — toujours disponibles depuis n'importe quel poste, partagés avec votre bureau, avec une interface en 7 langues. Dans <strong>Computo NX</strong>, il active aussi les <strong>listes de prix personnalisées</strong> : chargez vos listes fournisseurs et vos prix historiques et l'application les utilise pour chiffrer en temps réel, en priorité sur les bordereaux régionaux (<a href=\"/computo/listini-custom/\">guide, en italien</a>).",
    gd_p3="L'abonnement couvre l'<strong>espace fichiers</strong> et est distinct des crédits des applications. Il s'achète dans la section <em>Offres GeoDropbox</em> de la page <a href=\"https://www.geostru.ai/pricing/\"><strong>geostru.ai/pricing</strong></a> avec le bouton <em>S'abonner</em> de l'offre choisie :",
    per_month='mois', badge='Recommandé',
    plan_base='Idéal pour le professionnel indépendant',
    plan_plus='Espace généreux pour bureaux et équipes multi-projets',
    plan_max='Espace maximal pour les structures importantes et les modèles BIM/IFC',
    pricing_url='https://www.geostru.ai/pricing/',
    gdpr_title='Confidentialité et RGPD', gdpr_count='7 langues',
    gdpr_p1='Le service est fourni par <strong>ENGSOFT SRL</strong>, responsable du traitement pour les données de compte et d\'utilisation ; vous restez responsable des contenus que vous importez, que GeoStru traite en tant que sous-traitant (art. 28 RGPD) uniquement sur vos instructions.',
    gdpr_p2="Les données sont hébergées dans l'<strong>UE et en Suisse</strong>, chiffrées en transit et isolées par client ; les fournisseurs qui nous accompagnent (Google, Stripe) opèrent avec leurs propres accords de traitement. Le résumé de vulgarisation est disponible en 7 langues ; le texte complet et contraignant est la politique de confidentialité officielle.",
    gdpr_link='Résumé RGPD →', policy_link='Politique de confidentialité complète →',
),
'es': dict(
    title='Manuales GeoStru NX',
    meta='Documentación de las aplicaciones web GeoStru NX: geotecnia, geología, mecánica de rocas, hidráulica, topografía. Una plataforma EngSoft.',
    lang_nav='Idioma',
    eyebrow='GeoStru AI · una plataforma EngSoft',
    h1='Manuales GeoStru NX',
    lede1='<strong>GeoStru AI</strong> es la plataforma en la nube de <strong>ENGSOFT SRL</strong> que lleva el cálculo geotécnico, geológico e hidráulico al navegador: las aplicaciones <strong>GeoStru NX</strong> cubren todo el flujo de trabajo — datos, cálculo, informe — con asistente de IA integrado y sin instalar nada.',
    lede2='Están dirigidas a geólogos, ingenieros, estudios técnicos, empresas y administraciones públicas. Aquí encontrarás la documentación de cada aplicación, organizada por categorías como en <a href="https://www.geostru.ai/">geostru.ai</a>.',
    lede3='<strong>Idiomas</strong>: los manuales se abren en italiano; donde existe una traducción encontrarás <strong>banderas en la tarjeta</strong> que abren el manual en ese idioma — y dentro de cada manual puedes cambiar de idioma con el selector de la cabecera. Las tarjetas sin banderas están por ahora solo en italiano.',
    gd_count='almacenamiento en la nube · 3 planes',
    gd_p1='<strong>GeoDropbox</strong> es la plataforma GIS en la nube de GeoStru para archivar documentos georreferenciados: cientos de proyectos en el mapa, columnas estratigráficas, gestión de archivos y búsqueda con IA.',
    gd_p2='Está integrado en las apps NX: encontrarás el botón <strong>GeoDropbox</strong> junto a Guardar/Abrir, y los proyectos se abren y se guardan directamente en la nube — siempre disponibles desde cualquier puesto, compartidos con tu estudio, con interfaz en 7 idiomas. En <strong>Computo NX</strong> habilita además los <strong>listados de precios personalizados</strong>: subes tus listas de proveedores y precios históricos y la app los usa para valorar en tiempo real, con prioridad sobre los cuadros de precios regionales (<a href="/computo/listini-custom/">guía, en italiano</a>).',
    gd_p3='La suscripción cubre el <strong>espacio de archivos</strong> y es independiente de los créditos de las apps. Se adquiere en la sección <em>Planes GeoDropbox</em> de la página <a href="https://www.geostru.ai/pricing/"><strong>geostru.ai/pricing</strong></a> con el botón <em>Suscribirse</em> del plan elegido:',
    per_month='mes', badge='Recomendado',
    plan_base='Ideal para el profesional individual',
    plan_plus='Espacio amplio para estudios y equipos con varios proyectos',
    plan_max='Máximo espacio para estudios estructurados y modelos BIM/IFC',
    pricing_url='https://www.geostru.ai/pricing/',
    gdpr_title='Privacidad y RGPD', gdpr_count='7 idiomas',
    gdpr_p1='El servicio lo presta <strong>ENGSOFT SRL</strong>, responsable del tratamiento de los datos de cuenta y de uso; tú sigues siendo el responsable de los contenidos que subes, que GeoStru trata como encargado (art. 28 RGPD) solo según tus instrucciones.',
    gdpr_p2='Los datos se alojan en la <strong>UE y Suiza</strong>, cifrados en tránsito y aislados por cliente; los proveedores que nos apoyan (Google, Stripe) operan con sus propios acuerdos de tratamiento. El resumen divulgativo está disponible en 7 idiomas; el texto completo y vinculante es la Política de privacidad oficial.',
    gdpr_link='Resumen RGPD →', policy_link='Política de privacidad completa →',
),
'ro': dict(
    title='Manuale GeoStru NX',
    meta='Documentația aplicațiilor web GeoStru NX: geotehnică, geologie, mecanica rocilor, hidraulică, topografie. O platformă EngSoft.',
    lang_nav='Limbă',
    eyebrow='GeoStru AI · o platformă EngSoft',
    h1='Manuale GeoStru NX',
    lede1='<strong>GeoStru AI</strong> este platforma cloud a <strong>ENGSOFT SRL</strong> care aduce calculul geotehnic, geologic și hidraulic în browser: aplicațiile <strong>GeoStru NX</strong> acoperă întregul flux de lucru — date, calcul, raport — cu asistent AI integrat și fără nicio instalare.',
    lede2='Se adresează geologilor, inginerilor, birourilor de proiectare, firmelor și administrațiilor publice. Aici găsești documentația fiecărei aplicații, organizată pe categorii ca pe <a href="https://www.geostru.ai/">geostru.ai</a>.',
    lede3='<strong>Limbi</strong>: manualele se deschid în italiană; unde există o traducere găsești <strong>steaguri pe card</strong> care deschid manualul în limba aleasă — iar în fiecare manual poți schimba limba din selectorul din antet. Cardurile fără steaguri sunt deocamdată doar în italiană.',
    gd_count='spațiu cloud · 3 planuri',
    gd_p1='<strong>GeoDropbox</strong> este platforma GIS cloud a GeoStru pentru arhivarea documentelor georeferențiate: sute de proiecte pe hartă, coloane stratigrafice, gestionarea fișierelor și căutare AI.',
    gd_p2='Este integrat în aplicațiile NX: găsești butonul <strong>GeoDropbox</strong> lângă Salvează/Deschide, iar proiectele se deschid și se salvează direct în cloud — mereu disponibile de la orice stație, partajate cu biroul tău, cu interfață în 7 limbi. În <strong>Computo NX</strong> activează și <strong>listele de prețuri personalizate</strong>: încarci listele furnizorilor și prețurile istorice, iar aplicația le folosește pentru evaluare în timp real, cu prioritate față de listele regionale (<a href="/computo/listini-custom/">ghid, în italiană</a>).',
    gd_p3='Abonamentul acoperă <strong>spațiul de fișiere</strong> și este separat de creditele aplicațiilor. Se achiziționează din secțiunea <em>Planuri GeoDropbox</em> a paginii <a href="https://www.geostru.ai/pricing/"><strong>geostru.ai/pricing</strong></a> cu butonul <em>Abonează-te</em> al planului ales:',
    per_month='lună', badge='Recomandat',
    plan_base='Ideal pentru profesionistul individual',
    plan_plus='Spațiu generos pentru birouri și echipe cu mai multe proiecte',
    plan_max='Spațiu maxim pentru birouri structurate și modele BIM/IFC',
    pricing_url='https://www.geostru.ai/pricing/',
    gdpr_title='Confidențialitate și GDPR', gdpr_count='7 limbi',
    gdpr_p1='Serviciul este furnizat de <strong>ENGSOFT SRL</strong>, operator pentru datele de cont și de utilizare; rămâi operator al conținutului pe care îl încarci, pe care GeoStru îl prelucrează ca persoană împuternicită (art. 28 GDPR) numai la instrucțiunile tale.',
    gdpr_p2='Datele sunt găzduite în <strong>UE și Elveția</strong>, criptate în tranzit și izolate per client; furnizorii care ne susțin (Google, Stripe) operează cu propriile acorduri de prelucrare. Rezumatul informativ este disponibil în 7 limbi; textul complet și obligatoriu este Politica de confidențialitate oficială.',
    gdpr_link='Rezumat GDPR →', policy_link='Politica de confidențialitate completă →',
),
'pl': dict(
    title='Podręczniki GeoStru NX',
    meta='Dokumentacja aplikacji internetowych GeoStru NX: geotechnika, geologia, mechanika skał, hydraulika, topografia. Platforma EngSoft.',
    lang_nav='Język',
    eyebrow='GeoStru AI · platforma EngSoft',
    h1='Podręczniki GeoStru NX',
    lede1='<strong>GeoStru AI</strong> to platforma chmurowa firmy <strong>ENGSOFT SRL</strong>, która przenosi obliczenia geotechniczne, geologiczne i hydrauliczne do przeglądarki: aplikacje <strong>GeoStru NX</strong> obejmują cały przepływ pracy — dane, obliczenia, raport — z wbudowanym asystentem AI i bez instalacji.',
    lede2='Są przeznaczone dla geologów, inżynierów, biur projektowych, firm i administracji publicznej. Znajdziesz tu dokumentację każdej aplikacji, uporządkowaną według kategorii tak jak na <a href="https://www.geostru.ai/">geostru.ai</a>.',
    lede3='<strong>Języki</strong>: podręczniki otwierają się po włosku; tam, gdzie istnieje tłumaczenie, na karcie znajdziesz <strong>flagi</strong> otwierające podręcznik w wybranym języku — a w każdym podręczniku możesz zmienić język w selektorze u góry strony. Karty bez flag są na razie dostępne tylko po włosku.',
    gd_count='przestrzeń w chmurze · 3 plany',
    gd_p1='<strong>GeoDropbox</strong> to chmurowa platforma GIS GeoStru do archiwizacji dokumentów georeferencyjnych: setki projektów na mapie, profile stratygraficzne, zarządzanie plikami i wyszukiwanie AI.',
    gd_p2='Jest zintegrowany z aplikacjami NX: obok Zapisz/Otwórz znajdziesz przycisk <strong>GeoDropbox</strong>, a projekty otwierają się i zapisują bezpośrednio w chmurze — zawsze dostępne z dowolnego stanowiska, współdzielone z Twoim biurem, z interfejsem w 7 językach. W <strong>Computo NX</strong> umożliwia też <strong>własne cenniki</strong>: wgrywasz cenniki dostawców i ceny historyczne, a aplikacja używa ich do wyceny w czasie rzeczywistym, z pierwszeństwem przed cennikami regionalnymi (<a href="/computo/listini-custom/">przewodnik, po włosku</a>).',
    gd_p3='Subskrypcja obejmuje <strong>przestrzeń na pliki</strong> i jest niezależna od kredytów aplikacji. Można ją kupić w sekcji <em>Plany GeoDropbox</em> na stronie <a href="https://www.geostru.ai/pricing/"><strong>geostru.ai/pricing</strong></a> przyciskiem <em>Subskrybuj</em> wybranego planu:',
    per_month='mies.', badge='Polecany',
    plan_base='Idealny dla samodzielnego specjalisty',
    plan_plus='Duża przestrzeń dla biur i zespołów przy wielu projektach',
    plan_max='Maksymalna przestrzeń dla rozbudowanych biur i modeli BIM/IFC',
    pricing_url='https://www.geostru.ai/pricing/',
    gdpr_title='Prywatność i RODO', gdpr_count='7 języków',
    gdpr_p1='Usługę świadczy <strong>ENGSOFT SRL</strong>, administrator danych konta i danych o korzystaniu; pozostajesz administratorem przesyłanych treści, które GeoStru przetwarza jako podmiot przetwarzający (art. 28 RODO) wyłącznie zgodnie z Twoimi instrukcjami.',
    gdpr_p2='Dane są hostowane w <strong>UE i Szwajcarii</strong>, szyfrowane podczas przesyłania i odizolowane dla każdego klienta; wspierający nas dostawcy (Google, Stripe) działają na podstawie własnych umów powierzenia. Przystępne podsumowanie jest dostępne w 7 językach; pełnym i wiążącym tekstem jest oficjalna Polityka prywatności.',
    gdpr_link='Podsumowanie RODO →', policy_link='Pełna Polityka prywatności →',
),
}

CSS = """
    :root{
      --blue:#1e3a5f; --gold:#d4a017; --ink:#1e293b; --muted:#64748b;
      --bg:#f8fafc; --card:#fff; --border:#e2e8f0; --tint:#eef3f8;
    }
    *{box-sizing:border-box}
    body{font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;max-width:960px;margin:0 auto;padding:2rem 1.2rem 2rem;color:var(--ink);background:var(--bg);line-height:1.55}
    a{color:var(--blue)}
    a:focus-visible{outline:2px solid var(--gold);outline-offset:2px;border-radius:4px}

    /* Hero */
    .eyebrow{font-size:.72rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
    h1{font-weight:800;letter-spacing:-0.02em;color:var(--blue);margin:.25rem 0 .8rem;font-size:clamp(1.7rem,4.5vw,2.4rem)}
    .lede{color:var(--ink);max-width:46rem;margin:0}
    .lede + .lede{margin-top:.6rem;color:var(--muted)}

    /* Categorie */
    .cat{margin-top:2.6rem}
    .cat-head{display:flex;align-items:baseline;gap:.6rem;border-bottom:1px solid var(--border);padding-bottom:.45rem}
    .cat-head::before{content:"";align-self:stretch;width:4px;border-radius:2px;background:var(--gold)}
    .cat-head h2{margin:0;font-size:.95rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--blue)}
    .cat-head .count{font-size:.78rem;color:var(--muted)}
    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem;margin-top:1rem}
    .card{position:relative;background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.1rem 1.2rem .9rem;transition:border-color .12s,box-shadow .12s;display:flex;flex-direction:column;gap:.5rem}
    .card:hover{border-color:var(--blue);box-shadow:0 4px 14px rgba(0,0,0,.07)}
    .card h3{margin:0;font-size:1rem;font-weight:700}
    .card h3 a{color:inherit;text-decoration:none}
    .card h3 a::after{content:"";position:absolute;inset:0;border-radius:10px}
    .card:focus-within{border-color:var(--blue)}
    .card p{margin:0;color:var(--muted);font-size:.84rem;line-height:1.5;min-height:3em;flex:1}
    @media (min-width:640px){.card{min-height:168px}}
    .langs{position:relative;z-index:1;display:flex;gap:.35rem;flex-wrap:wrap;margin-top:.15rem}
    .langs.standalone{margin-top:.9rem}
    .langs a{font-size:.72rem;font-weight:700;letter-spacing:.04em;padding:1px 6px;border-radius:4px;background:#f1f5f9;color:#475569;text-decoration:none;border:1px solid var(--border);transition:background .1s,color .1s}
    .langs a:hover{background:var(--blue);color:#fff;border-color:var(--blue)}
    .langs.switcher{justify-content:flex-end;margin:0 0 1.4rem}
    .langs.switcher a.active{background:var(--blue);color:#fff;border-color:var(--blue)}

    /* Sezioni discorsive (GeoDropbox, GDPR) */
    .sect-p{max-width:52rem;font-size:.92rem;margin:.9rem 0 0}
    .links{margin-top:1rem;display:flex;gap:1.4rem;flex-wrap:wrap}
    .links a{font-weight:700;font-size:.88rem}
    .plan{position:relative;background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.1rem 1.2rem .9rem;text-decoration:none;color:inherit;transition:border-color .12s,box-shadow .12s;display:flex;flex-direction:column;gap:.3rem}
    .plan:hover{border-color:var(--blue);box-shadow:0 4px 14px rgba(0,0,0,.07)}
    .plan h3{margin:0;font-size:1rem;font-weight:700}
    .plan .size{margin:0;font-weight:700;color:var(--blue);font-size:.9rem}
    .plan p{margin:0;color:var(--muted);font-size:.84rem;flex:1}
    .plan .badge{position:absolute;top:-.6rem;right:.8rem;background:var(--gold);color:#fff;font-size:.66rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;padding:2px 8px;border-radius:99px}

    footer{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--border);color:#94a3b8;font-size:.8rem;text-align:center;line-height:1.7}
    footer a{color:var(--blue);font-weight:600}
    @media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""


def landing_url(lang):
    return '/' if lang == 'it' else f'/{lang}/'


def manual_url(slug, lang):
    """URL del manuale nella lingua della pagina, se tradotto; altrimenti IT."""
    if lang != 'it' and lang in APPS[slug]['langs']:
        return f'/{slug}/{lang}/'
    return f'/{slug}/'


def card_html(slug, lang):
    app = APPS[slug]
    chips = ''
    if len(app['langs']) > 1:
        links = ''.join(
            f'<a href="/{slug}/{l}/" hreflang="{l}">{FLAG[l]} {l.upper()}</a>'
            if l != 'it' else f'<a href="/{slug}/" hreflang="it">{FLAG["it"]} IT</a>'
            for l in app['langs'])
        chips = f'\n        <span class="langs">{links}</span>'
    return (f'      <div class="card"><h3><a href="{manual_url(slug, lang)}">{app["name"]}</a></h3>'
            f'<p>{app["desc"][lang]}</p>{chips}</div>')


def render(lang):
    s = S[lang]
    def sw_link(l):
        cls = ' class="active"' if l == lang else ''
        return f'<a href="{landing_url(l)}" hreflang="{l}"{cls}>{FLAG[l]} {l.upper()}</a>'
    switcher = ''.join(sw_link(l) for l in LANGS)
    alternates = '\n'.join(
        f'  <link rel="alternate" hreflang="{l}" href="https://help.nx.geostru.ai{landing_url(l)}" />'
        for l in LANGS) + '\n  <link rel="alternate" hreflang="x-default" href="https://help.nx.geostru.ai/" />'

    sections = []
    for key, slugs in CATEGORIES:
        cards = '\n'.join(card_html(sl, lang) for sl in slugs)
        sections.append(f'''  <section class="cat">
    <div class="cat-head"><h2>{CAT_NAMES[key][lang]}</h2><span class="count">{app_count(lang, len(slugs))}</span></div>
    <div class="grid">
{cards}
    </div>
  </section>''')
    cats = '\n\n'.join(sections)

    plans = f'''    <div class="grid">
      <a class="plan" href="{s['pricing_url']}">
        <h3>Storage Base</h3>
        <p class="size">25 GB · €12/{s['per_month']}</p>
        <p>{s['plan_base']}</p>
      </a>
      <a class="plan" href="{s['pricing_url']}">
        <span class="badge">{s['badge']}</span>
        <h3>Storage Plus</h3>
        <p class="size">150 GB · €39/{s['per_month']}</p>
        <p>{s['plan_plus']}</p>
      </a>
      <a class="plan" href="{s['pricing_url']}">
        <h3>Storage Max</h3>
        <p class="size">750 GB · €99/{s['per_month']}</p>
        <p>{s['plan_max']}</p>
      </a>
    </div>'''

    gdpr_url = '/gdpr/' if lang == 'it' else f'/gdpr/{lang}/'
    gdpr_chips = ''.join(
        f'<a href="/gdpr/{l}/" hreflang="{l}">{FLAG[l]} {l.upper()}</a>'
        if l != 'it' else f'<a href="/gdpr/" hreflang="it">{FLAG["it"]} IT</a>'
        for l in LANGS)

    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <title>{s['title']}</title>
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <meta name="description" content="{s['meta']}" />
{alternates}
  <style>{CSS}  </style>
</head>
<body>
  <header>
    <nav class="langs switcher" aria-label="{s['lang_nav']}">{switcher}</nav>
    <p class="eyebrow">{s['eyebrow']}</p>
    <h1>{s['h1']}</h1>
    <p class="lede">{s['lede1']}</p>
    <p class="lede">{s['lede2']}</p>
    <p class="lede">{s['lede3']}</p>
  </header>

{cats}

  <section class="cat">
    <div class="cat-head"><h2>GeoDropbox</h2><span class="count">{s['gd_count']}</span></div>
    <p class="sect-p">{s['gd_p1']}</p>
    <p class="sect-p">{s['gd_p2']}</p>
    <p class="sect-p">{s['gd_p3']}</p>
{plans}
  </section>

  <section class="cat">
    <div class="cat-head"><h2>{s['gdpr_title']}</h2><span class="count">{s['gdpr_count']}</span></div>
    <p class="sect-p">{s['gdpr_p1']}</p>
    <p class="sect-p">{s['gdpr_p2']}</p>
    <div class="links">
      <a href="{gdpr_url}">{s['gdpr_link']}</a>
      <a href="https://www.geostru.ai/en/privacy-policy/">{s['policy_link']}</a>
    </div>
    <span class="langs standalone">{gdpr_chips}</span>
  </section>

  <footer>
    <strong>ENGSOFT SRL</strong> · Str. Sarmisegetuza nr. 17-19, Cluj-Napoca, România ·
    CUI 30277934 · Nr. Reg. Com. J2012001517126 · <a href="mailto:info@geostru.ai">info@geostru.ai</a><br>
    © <script>document.write(new Date().getFullYear())</script> GeoStru —
    <a href="https://www.geostru.ai">www.geostru.ai</a> · <a href="{gdpr_url}">Privacy (GDPR)</a>
  </footer>
</body>
</html>
'''


def main():
    if len(sys.argv) != 2:
        sys.exit('uso: build.py <out_dir>')
    out = Path(sys.argv[1])
    for lang in LANGS:
        dest = out / 'index.html' if lang == 'it' else out / lang / 'index.html'
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(lang), encoding='utf-8')
        print(f'{lang}: {dest}')


if __name__ == '__main__':
    main()
