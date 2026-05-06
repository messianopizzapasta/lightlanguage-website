(function () {
  var depth = parseInt(document.documentElement.getAttribute("data-locale-depth") || "0", 10);
  var up = depth ? "../" : "";

  var LANG_MAP = {
    en: up || "./",
    de: up + "de/",
    es: up + "es/",
    fr: up + "fr/",
    it: up + "it/",
    pt: up + "pt/",
  };

  var sel = document.getElementById("lang-switch");
  if (sel) {
    sel.addEventListener("change", function () {
      var dest = LANG_MAP[sel.value];
      if (dest) window.location.href = dest;
    });
  }

  document.querySelectorAll(".faq-item button").forEach(function (btn) {
    var item = btn.closest(".faq-item");
    var panel = item && item.querySelector(".faq-panel");
    if (panel) {
      var id = "faq-panel-" + Math.random().toString(36).slice(2, 9);
      panel.id = id;
      btn.setAttribute("aria-expanded", "false");
      btn.setAttribute("aria-controls", id);
    }
    btn.addEventListener("click", function () {
      var it = btn.closest(".faq-item");
      var open = it.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });
})();
