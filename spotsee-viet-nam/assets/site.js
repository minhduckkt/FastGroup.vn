/* SpotSee Viet Nam — tra ma, loc bang, bo chon Thermax. Sinh tu _tools/spotsee/static/site.js */
(function () {
  "use strict";
  var IDX = window.SS_INDEX || [];
  function norm(s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d"); }
  function key(s) { return norm(s).replace(/[^a-z0-9]/g, ""); }
  function esc(s) { return String(s || "").replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function score(it, q) {
    var n = key(q); if (!n) return 0;
    var k = key(it.c);
    if (k === n) return 100;
    if (k.indexOf(n) === 0) return 85;
    if (k.indexOf(n) >= 0) return 60;
    var words = norm(q).split(/\s+/).filter(Boolean);
    var hay = norm([it.c, it.d, it.t, it.k].join(" "));
    if (key(hay).indexOf(n) >= 0) return 45;
    var ok = words.every(function (w) { return hay.indexOf(w) >= 0; });
    if (ok) return it.t === "Dòng sản phẩm" || it.t === "Nhóm" || it.t === "Ứng dụng" ? 50 : 40;
    return 0;
  }
  function ranked(q, limit) {
    return IDX.map(function (it) { return { it: it, s: score(it, q) }; })
      .filter(function (x) { return x.s > 0; })
      .sort(function (a, b) { return b.s - a.s || a.it.c.length - b.it.c.length; })
      .slice(0, limit || 12);
  }

  /* --- o tra ma o hero --- */
  var hero = document.getElementById("heroq"), ac = document.getElementById("heroAc");
  if (hero && ac) {
    var draw = function () {
      var q = hero.value.trim();
      if (!q) { ac.classList.remove("on"); ac.innerHTML = ""; return; }
      var hits = ranked(q, 7);
      var base = hero.form ? hero.form.getAttribute("action") : "";
      ac.innerHTML = hits.map(function (x) {
        var it = x.it;
        return '<a href="' + it.u + '"><span class="code">' + esc(it.c) + '</span><span class="d">' + esc(it.d) + '</span><span class="mt">' + esc(it.t) + "</span></a>";
      }).join("") + '<a class="all" href="' + base + "?q=" + encodeURIComponent(q) + '">Xem tất cả kết quả</a>';
      ac.classList.add("on");
    };
    hero.addEventListener("input", draw);
    document.addEventListener("click", function (e) { if (!ac.contains(e.target) && e.target !== hero) ac.classList.remove("on"); });
  }

  /* --- trang tra ma --- */
  var box = document.getElementById("siteSearch"), out = document.getElementById("searchResults");
  if (box && out) {
    var params = new URLSearchParams(location.search);
    box.value = params.get("q") || "";
    var render = function () {
      var q = box.value.trim();
      if (!q) {
        out.innerHTML = '<p class="empty">Nhập mã hàng hoặc tên dòng. Ví dụ: 50000-SWQ, WM 8/46, SL298, 01ETHM0065, HemoTemp, FreezeSafe 2.</p>';
        return;
      }
      var hits = ranked(q, 40);
      out.innerHTML = hits.length ? hits.map(function (x) {
        var it = x.it;
        return '<article><div class="t">' + esc(it.t) + '</div><h3><a href="' + it.u + '">' + esc(it.c) + "</a></h3><p>" + esc(it.d) + "</p></article>";
      }).join("") : '<p class="empty">Không thấy mã phù hợp. Kiểm tra lại cách viết mã, hoặc gửi yêu cầu báo giá để Fast Group tra giúp trong catalog gốc của SpotSee.</p>';
    };
    box.addEventListener("input", render);
    render();
  }

  /* --- loc bang ma hang --- */
  Array.prototype.forEach.call(document.querySelectorAll("input[data-filter]"), function (inp) {
    var id = inp.getAttribute("data-filter");
    var tbl = document.getElementById(id);
    var cnt = document.querySelector('[data-count="' + id + '"]');
    if (!tbl) return;
    var rows = Array.prototype.slice.call(tbl.tBodies[0].rows);
    var txt = rows.map(function (r) { return norm(r.textContent); });
    inp.addEventListener("input", function () {
      var ws = norm(inp.value).split(/\s+/).filter(Boolean), n = 0;
      rows.forEach(function (r, i) {
        var ok = ws.every(function (w) { return txt[i].indexOf(w) >= 0; });
        r.style.display = ok ? "" : "none"; if (ok) n++;
      });
      if (cnt) cnt.textContent = n + " mã";
    });
  });

  /* --- bo chon Thermax --- */
  var tt = document.getElementById("txTemp"), tf = document.getElementById("txFmt"), tb = document.getElementById("txTable"), tc = document.getElementById("txCount");
  if (tt && tf && tb) {
    var trs = Array.prototype.slice.call(tb.tBodies[0].rows);
    var run = function () {
      var t = parseFloat(tt.value), f = tf.value, n = 0;
      trs.forEach(function (r) {
        var cs = r.getAttribute("data-c").split(",").map(Number);
        var ok = (!f || r.getAttribute("data-fmt") === f) && (isNaN(t) || (t >= cs[0] - 1 && t <= cs[cs.length - 1] + 1));
        r.style.display = ok ? "" : "none"; if (ok) n++;
        Array.prototype.forEach.call(r.querySelectorAll(".cells span"), function (s) {
          s.classList.toggle("hit", !isNaN(t) && Math.abs(Number(s.textContent) - t) <= 3);
        });
      });
      if (tc) tc.textContent = n + " dải phù hợp";
    };
    tt.addEventListener("input", run); tf.addEventListener("change", run); run();
  }

  /* --- thu vien anh san pham --- */
  Array.prototype.forEach.call(document.querySelectorAll(".gallery"), function (g) {
    var main = g.querySelector(".main img"); if (!main) return;
    var bs = g.querySelectorAll(".thumbs button");
    Array.prototype.forEach.call(bs, function (b) {
      b.addEventListener("click", function () {
        main.src = b.getAttribute("data-src");
        main.removeAttribute("width"); main.removeAttribute("height");
        Array.prototype.forEach.call(bs, function (x) { x.setAttribute("aria-current", x === b ? "true" : "false"); });
      });
    });
  });

  /* --- chip loc nhanh + #q= tren URL (thu vien tai lieu) --- */
  Array.prototype.forEach.call(document.querySelectorAll(".chip[data-set]"), function (b) {
    b.addEventListener("click", function () {
      var inp = document.querySelector('input[data-filter="' + b.getAttribute("data-set") + '"]');
      if (!inp) return;
      inp.value = b.getAttribute("data-val"); inp.dispatchEvent(new Event("input"));
      Array.prototype.forEach.call(document.querySelectorAll('.chip[data-set="' + b.getAttribute("data-set") + '"]'), function (x) { x.classList.toggle("on", x === b); });
    });
  });
  (function () {
    var m = /[#&]q=([^&]+)/.exec(location.hash); if (!m) return;
    var inp = document.querySelector("input[data-filter]"); if (!inp) return;
    inp.value = decodeURIComponent(m[1].replace(/\+/g, " ")); inp.dispatchEvent(new Event("input"));
  })();

  /* --- loc bai viet theo chuyen muc (trang Kien thuc) --- */
  Array.prototype.forEach.call(document.querySelectorAll("[data-catfilter] .chip"), function (b) {
    b.addEventListener("click", function () {
      var c = b.getAttribute("data-cat");
      Array.prototype.forEach.call(document.querySelectorAll(".posts-hub>div[data-cat]"), function (d) { d.style.display = !c || d.getAttribute("data-cat") === c ? "" : "none"; });
      Array.prototype.forEach.call(b.parentNode.querySelectorAll(".chip"), function (x) { x.classList.toggle("on", x === b); });
    });
  });
})();
