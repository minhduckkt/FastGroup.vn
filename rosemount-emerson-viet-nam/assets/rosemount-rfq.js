/* =====================================================================
   Form RFQ ky thuat cho brand portal (Fisher, Rosemount...) – trang Lien he.
   Cau hinh nam tren chinh the <form id="frfq">:
     data-source      ten nguon (cot "Nguon" trong Google Sheet), vd "Fisher", "Rosemount"
     data-proc-open   cac loai yeu cau tu mo khoi thong so (phan cach bang |)
     data-model-label / data-serial-label  nhan hien trong noi dung RFQ
   <script type="application/json" id="frfq-hints"> {"Loai yeu cau": "goi y"...} </script>
   Moi o thong so ky thuat co data-proc="Nhan hien thi" -> duoc gom vao noi dung.
   - Gui ve CUNG endpoint + cung dinh dang voi /assets/fg-rfq.js
     (token, source, model, qty, name, company, email, phone, message, page, ua)
     -> Apps Script / Google Sheet hien tai nhan duoc ngay, khong phai sua.
   - Doc ?model=... tren URL de dien san ma hang.
   - Loi mang -> mo email soan san (khong mat lead).
   ===================================================================== */
(function () {
  "use strict";
  var TOKEN = "fg-rfq-2026";
  var EMAIL = "minhduc@fastgroup.vn", TEL_TXT = "0938 888 958", ZALO = "https://zalo.me/0938888958";
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/, PHONE_RE = /^[0-9+()\s.\-]{8,20}$/;

  function $(id) { return document.getElementById(id); }
  function v(id) { var e = $(id); return e ? String(e.value || "").trim() : ""; }
  function esc(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function track(n, p) { if (window.gtag) { try { window.gtag("event", n, p || {}); } catch (e) {} } }

  function init() {
    var form = $("frfq");
    if (!form) return;
    var SOURCE = form.getAttribute("data-source") || "Không rõ";
    var OPEN = (form.getAttribute("data-proc-open") || "").split("|");
    var MODEL_L = form.getAttribute("data-model-label") || "Model / mã hàng";
    var SERIAL_L = form.getAttribute("data-serial-label") || "Serial / tag";
    var HINTS = {}; try { HINTS = JSON.parse(($("frfq-hints") || {}).textContent || "{}"); } catch (e) {}
    var born = Date.now();
    var msg = $("frfq-msg"), btn = form.querySelector("button[type=submit]");

    try {
      var m = (new URLSearchParams(location.search).get("model") || "").slice(0, 80);
      if (m) {
        $("frfq-model").value = m;
        var ctx = $("frfq-ctx"); if (ctx) { ctx.hidden = false; ctx.querySelector("b").textContent = m; }
      }
    } catch (e) {}

    var proc = $("frfq-proc");
    function sync() {
      var t = (form.querySelector("input[name=frfq-type]:checked") || {}).value || "";
      if (proc && OPEN.indexOf(t) >= 0) proc.open = true;
      var hint = $("frfq-hint"); if (hint) hint.textContent = HINTS[t] || "";
    }
    form.addEventListener("change", function (e) { if (e.target && e.target.name === "frfq-type") sync(); });
    sync();

    function show(kind, html) { msg.className = "fgq-msg on " + kind; msg.innerHTML = html; }
    function mark(id, bad) { var e = $(id); if (e) e.classList[bad ? "add" : "remove"]("fgq-bad"); }
    var HELP = 'Gửi ảnh nameplate / BOM qua <a href="' + ZALO + '" target="_blank" rel="noopener">Zalo ' + TEL_TXT + '</a> hoặc <a href="mailto:' + EMAIL + '">' + EMAIL + "</a>.";

    function compose() {
      var type = (form.querySelector("input[name=frfq-type]:checked") || {}).value || "";
      var docs = [].slice.call(form.querySelectorAll("input[name=frfq-doc]:checked")).map(function (x) { return x.value; });
      var L = ["LOẠI YÊU CẦU: " + (type || "(chưa chọn)"), "Nhóm thiết bị: " + (v("frfq-group") || "-"), MODEL_L + ": " + (v("frfq-model") || "-")];
      if (v("frfq-serial")) L.push(SERIAL_L + ": " + v("frfq-serial"));
      L.push("Số lượng: " + (v("frfq-qty") || "-"));
      var got = [].slice.call(form.querySelectorAll("[data-proc]")).filter(function (e) { return String(e.value || "").trim(); });
      if (got.length) { L.push("", "THÔNG SỐ KỸ THUẬT"); got.forEach(function (e) { L.push("- " + e.getAttribute("data-proc") + ": " + e.value.trim()); }); }
      L.push("", "Chứng từ / chứng chỉ: " + (docs.length ? docs.join(", ") : "CO, CQ"));
      L.push("Nơi giao hàng: " + (v("frfq-place") || "-"));
      L.push("Thời điểm cần hàng: " + (v("frfq-when") || "-"));
      if (v("frfq-note")) L.push("", "GHI CHÚ:", v("frfq-note"));
      return L.join("\n");
    }
    function anyProc() { return [].slice.call(form.querySelectorAll("[data-proc]")).some(function (e) { return String(e.value || "").trim(); }); }

    function mailto(d) {
      var body = ["Ho va ten: " + d.name, "Cong ty: " + d.company, "Email: " + d.email, "Dien thoai: " + d.phone, "", d.message].join("\n");
      location.href = "mailto:" + EMAIL + "?subject=" + encodeURIComponent("[RFQ " + SOURCE + "] " + (d.model || "Chua co ma") + " - " + (d.company || d.name)) + "&body=" + encodeURIComponent(body);
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      if (v("frfq-trap") || Date.now() - born < 1500) return;
      var d = { token: TOKEN, source: SOURCE, model: v("frfq-model"), qty: v("frfq-qty"), page: location.href, ua: navigator.userAgent,
        name: v("frfq-name"), company: v("frfq-company"), email: v("frfq-email"), phone: v("frfq-phone"), message: "" };
      var miss = [];
      if (d.name.length < 2) { mark("frfq-name", 1); miss.push("họ và tên"); } else mark("frfq-name", 0);
      if (!EMAIL_RE.test(d.email)) { mark("frfq-email", 1); miss.push("email hợp lệ"); } else mark("frfq-email", 0);
      if (!PHONE_RE.test(d.phone)) { mark("frfq-phone", 1); miss.push("số điện thoại / Zalo"); } else mark("frfq-phone", 0);
      if (!(d.model || v("frfq-serial") || anyProc() || v("frfq-note"))) { mark("frfq-model", 1); mark("frfq-note", 1); miss.push("mã hàng, thông số hoặc ghi chú"); }
      else { mark("frfq-model", 0); mark("frfq-note", 0); }
      if (miss.length) { show("err", "Vui lòng nhập: " + miss.join(", ") + "."); track("rfq_invalid", { source: SOURCE, fields: miss.join("|") }); return; }
      d.message = compose();
      var label = btn.textContent; btn.disabled = true; btn.classList.add("fgq-busy"); btn.textContent = "Đang gửi…";
      show("ok", "Đang gửi yêu cầu…");
      function done() { btn.disabled = false; btn.classList.remove("fgq-busy"); btn.textContent = label; }
      var EP = window.FG_RFQ_ENDPOINT;
      if (!EP) { done(); show("ok", "Đang mở phần mềm email với nội dung đã điền sẵn. " + HELP); mailto(d); return; }
      fetch(EP, { method: "POST", redirect: "follow", headers: { "Content-Type": "text/plain;charset=utf-8" }, body: JSON.stringify(d) })
        .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.text(); })
        .then(function (t) {
          var res = {}; try { res = JSON.parse(t); } catch (e) {}
          if (res.ok === false) throw new Error(res.error || "rejected");
          done(); form.reset(); sync();
          show("ok", "Đã nhận yêu cầu" + (res.ref ? " (mã <b>" + esc(res.ref) + "</b>)" : "") + ". Fast Group phản hồi trong ngày làm việc. " + HELP);
          track("generate_lead", { form: "rfq_" + SOURCE.toLowerCase(), source: SOURCE, model: d.model || "(none)" });
        })
        .catch(function () { done(); show("err", "Chưa gửi được qua web – đang mở email với nội dung đã điền sẵn. " + HELP); track("rfq_fallback_mailto", { source: SOURCE }); mailto(d); });
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
