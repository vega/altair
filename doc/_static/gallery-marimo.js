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
  const editorTooltip = button.title;

  // The title comes from the example docstring, so the button can only be
  // placed next to it after the page has been rendered.
  const title = button.closest("section")?.querySelector("h1");
  if (title) {
    const titleRow = document.createElement("div");
    titleRow.className = "gallery-title-row";
    title.before(titleRow);
    titleRow.append(title, button);
  }

  button.addEventListener("click", () => {
    if (!marimoExample.querySelector("iframe")) {
      // marimo's page can take a few seconds to load inside the iframe. We
      // can't see its real progress, so the bar slows down as it nears 90%
      // and only runs to the end once the page has loaded.
      const progress = document.createElement("div");
      progress.className = "gallery-marimo-progress";
      progress.setAttribute("role", "progressbar");
      progress.setAttribute("aria-label", "Loading marimo notebook");
      marimoExample.appendChild(progress);
      const growing = progress.animate([{ width: "0%" }, { width: "90%" }], {
        duration: 4000,
        easing: "cubic-bezier(0.1, 0.6, 0.3, 1)",
        fill: "forwards",
      });

      const iframe = document.createElement("iframe");
      iframe.addEventListener(
        "load",
        () => {
          growing.commitStyles();
          growing.cancel();
          progress
            .animate(
              [
                { width: progress.style.width, opacity: 1 },
                { width: "100%", opacity: 1, offset: 0.6 },
                { width: "100%", opacity: 0 },
              ],
              { duration: 500, easing: "ease-out", fill: "forwards" }
            )
            .finished.then(() => progress.remove());
        },
        { once: true }
      );
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
    button.textContent = showMarimo ? "Back to static page" : "Try this example";
    button.title = showMarimo
      ? "Return to the static chart and code."
      : editorTooltip;
  });
});
