// Config MathJax 3 per MkDocs Material + pymdownx.arithmatex (generic: true).
// Senza questo file MathJax 3 NON processa i delimitatori \( ... \) e \[ ... \]
// — solo $ ... $ — e le formule restano testo grezzo nella pagina.
//
// Riferimento: https://squidfunk.github.io/mkdocs-material/reference/math/
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// pymdownx.arithmatex con generic:true emette span/div con class="arithmatex".
// Su "navigation.instant" il DOM viene rimpiazzato senza reload: dobbiamo
// chiedere a MathJax di ricaricare gli elementi dopo ogni navigazione.
document$.subscribe(() => {
  if (typeof MathJax !== 'undefined' && MathJax.typesetPromise) {
    MathJax.typesetPromise();
  }
});
