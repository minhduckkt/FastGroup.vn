/* TESCOM portal: loc chip theo nhom con + tim nhanh tren trang tra cuu */
(function () {
  'use strict';
  function ready(fn) { if (document.readyState !== 'loading') fn(); else document.addEventListener('DOMContentLoaded', fn); }
  ready(function () {
    var chips = document.querySelectorAll('.tc-chip');
    if (chips.length) {
      var cards = document.querySelectorAll('.tc-grid .product-card');
      Array.prototype.forEach.call(chips, function (b) {
        b.addEventListener('click', function () {
          var f = b.getAttribute('data-f');
          Array.prototype.forEach.call(chips, function (x) { x.classList.toggle('is-on', x === b); x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
          Array.prototype.forEach.call(cards, function (c) { c.hidden = !!f && c.getAttribute('data-sub') !== f; });
        });
      });
    }
    var q = document.getElementById('tc-q');
    if (q) {
      var rows = document.querySelectorAll('.tc-table tbody tr'), cnt = document.getElementById('tc-count');
      var norm = function (s) { return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd'); };
      var data = Array.prototype.map.call(rows, function (r) { return norm(r.getAttribute('data-q')); });
      var run = function () {
        var terms = norm(q.value).split(/\s+/).filter(Boolean), n = 0;
        Array.prototype.forEach.call(rows, function (r, i) {
          var ok = terms.every(function (t) { return data[i].indexOf(t) !== -1; });
          r.hidden = !ok; if (ok) n++;
        });
        cnt.textContent = n + ' / ' + rows.length + ' dòng';
      };
      q.addEventListener('input', run);
      try { var m = new URLSearchParams(location.search).get('q'); if (m) q.value = m; } catch (e) {}
      run();
    }
  });
})();
