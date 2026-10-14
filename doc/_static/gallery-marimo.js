// Swap a gallery example's static chart and code for a live marimo notebook.
// The iframe is only created on the first click, so marimo is not loaded
// unless a reader asks for it.
document.addEventListener("DOMContentLoaded", () => {
  const button = document.querySelector(".gallery-marimo-toggle");
  const staticExample = document.querySelector(".gallery-static-example");
  const marimoExample = document.querySelector(".gallery-marimo-example");
  if (!button || !staticExample || !marimoExample) {
    return;
  }

  button.addEventListener("click", () => {
    if (!marimoExample.firstChild) {
      const iframe = document.createElement("iframe");
      iframe.src = button.dataset.marimoSrc;
      iframe.title = "Interactive marimo notebook";
      iframe.setAttribute(
        "sandbox",
        "allow-scripts allow-same-origin allow-downloads allow-popups allow-forms"
      );
      iframe.allow = "microphone";
      iframe.allowFullscreen = true;
      marimoExample.appendChild(iframe);
    }

    const showMarimo = marimoExample.hidden;
    marimoExample.hidden = !showMarimo;
    staticExample.hidden = showMarimo;
    button.textContent = showMarimo ? "Show static example" : "Open in marimo";
  });
});
