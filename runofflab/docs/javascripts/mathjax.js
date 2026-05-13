// MathJax v3 config — wired for mkdocs-material with `navigation.instant`.
// Caricato PRIMA di tex-mml-chtml.js in extra_javascript (mkdocs.yml), così la
// global window.MathJax viene letta da MathJax al boot.
//
// document$ è l'observable di mkdocs-material che emette su ogni navigazione
// (anche quelle SPA-style abilitate da navigation.instant). Senza la
// subscription, MathJax tipset solo la prima pagina e tutte le altre mostrano
// il LaTeX grezzo (sintomo riportato dal cliente: formule visibili come
// "\[ ... \]" letterale invece che renderizzate).
window.MathJax = {
    tex: {
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["\\[", "\\]"], ["$$", "$$"]],
        processEscapes: true,
        processEnvironments: true
    },
    options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
    }
};

document$.subscribe(() => {
    if (window.MathJax && MathJax.typesetPromise) {
        try {
            MathJax.startup.output.clearCache && MathJax.startup.output.clearCache();
            MathJax.typesetClear && MathJax.typesetClear();
            MathJax.texReset && MathJax.texReset();
            MathJax.typesetPromise();
        } catch (e) {
            console.warn('[MathJax] retypeset failed:', e);
        }
    }
});
