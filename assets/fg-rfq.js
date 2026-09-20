/* =====================================================================
   FAST GROUP — form RFQ dùng chung cho fastgroup.vn và các brand portal
   =====================================================================
   MỘT file này phục vụ mọi site. Muốn đổi endpoint, sửa thông tin hãng,
   sửa mẫu nội dung RFQ hay giao diện form thì chỉ sửa ở đây.

   ---------------------------------------------------------------------
   CÁCH 1 — gắn form vào một chỗ cụ thể (trang Liên hệ):

     <div data-fg-rfq data-fg-source="Qlight"></div>
     <script src="/assets/fg-rfq.js" defer></script>

   CÁCH 2 — tự gắn vào mọi trang sản phẩm (không sửa từng trang):
     Khai biến nguồn trong file JS dùng chung của portal rồi nạp file này.
     Script tự đọc JSON-LD Product, lấy mã hàng, chèn form trước footer,
     điền sẵn mẫu nội dung RFQ theo hãng và hiện panel thông tin hãng.

     window.FG_RFQ_SOURCE = 'Qlight';
     (function(){var s=document.createElement('script');
       s.src='/assets/fg-rfq.js';document.head.appendChild(s);})();

   ---------------------------------------------------------------------
   Thuộc tính của khối:
     data-fg-source  Tên nguồn — khoá của bảng BRANDS bên dưới, đồng thời
                     là cột "Nguồn" trong Google Sheet
     data-fg-model   (tuỳ chọn) mã hàng đang xem
     data-fg-skin    "portal" (mặc định) hoặc "main" cho fastgroup.vn
     data-fg-title   (tuỳ chọn) tiêu đề khối
     data-fg-note    (tuỳ chọn) một dòng mô tả dưới tiêu đề
     data-fg-aside   "1" để hiện thêm panel thông tin hãng bên cạnh form
                     (trang sản phẩm tự bật; trang Liên hệ đã có panel riêng)

   Quy tắc nội dung:
     - Không trang nào có placeholder trong ô nhập.
     - Có mã hàng  -> ô Nội dung được điền sẵn mẫu RFQ của hãng đó.
     - Không mã hàng -> mọi ô để trắng.
   ===================================================================== */
(function () {
  'use strict';

  /* ========================= CẤU HÌNH ================================ */

  /** URL Web app của Google Apps Script, kết thúc bằng /exec.
   *  Để trống = form mở phần mềm email của khách (vẫn không mất lead). */
  var ENDPOINT = 'https://script.google.com/macros/s/AKfycbyKugavYly5X-TpXnAVTJRg93l6xH7K2j9P0E-z2VpPJVaTEgoiPNXRW1-VY3K9YlhLNg/exec';

  /** Mỗi portal có thể dùng tài khoản Google riêng để KHÔNG chung hạn ngạch
   *  gửi thư. Khai trong trang đó, trước khi nạp file này:
   *      window.FG_RFQ_ENDPOINT = 'https://script.google.com/.../exec';
   *  Portal nào không khai thì dùng ENDPOINT mặc định ở trên. */
  function endpoint() {
    return (typeof window !== 'undefined' && window.FG_RFQ_ENDPOINT) || ENDPOINT;
  }

  /** Phải khớp với FORM_TOKEN trong Apps Script. */
  var TOKEN = 'fg-rfq-2026';

  /** Liên hệ chung của Fast Group. Nếu sau này có email riêng theo hãng
   *  (alias Zoho), khai thêm khoá `email` trong từng mục của BRANDS. */
  var CONTACT = {
    email:   'minhduc@fastgroup.vn',
    tel:     '+84938888958',
    telTxt:  '0938 888 958',
    zalo:    'https://zalo.me/0938888958',
    zaloTxt: '0938 888 958',
    office:  '150/41 Nguyễn Cư Trinh, P. Cầu Ông Lãnh, TP. Hồ Chí Minh',
    office2: '51 Lê Văn Lộc, P. Vũng Tàu, TP. Hồ Chí Minh'
  };

  /* ------------------- THÔNG TIN HÃNG THEO TỪNG PORTAL ---------------- */
  /* Khoá phải khớp chính xác giá trị data-fg-source.
     tpl = mẫu nội dung RFQ, {model} sẽ được thay bằng mã hàng. */

  var BRANDS = {
    'Qlight': {
      maker:  'Qlight Co., Ltd',
      origin: 'Hàn Quốc',
      scope:  'Đèn tháp tín hiệu, đèn cảnh báo và còi báo công nghiệp, gồm cả dòng phòng nổ (Ex-proof)',
      role:   'Nhà phân phối được Qlight ủy quyền tại Việt Nam',
      proof:  'Certificate of Distributor do Qlight Co., Ltd. cấp',
      tpl: 'Vui lòng báo giá Qlight {model}.\n' +
           'Điện áp: \n' +
           'Màu: \n' +
           'Kiểu lắp (trụ / tường / trực tiếp): \n' +
           'Yêu cầu chứng từ: CO, CQ\n' +
           'Nơi giao hàng: \n' +
           'Thời điểm cần hàng: '
    },
    'WIKA': {
      maker:  'WIKA Alexander Wiegand SE & Co. KG',
      origin: 'Đức',
      scope:  'Thiết bị đo áp suất, nhiệt độ, mức, lưu lượng, đo lực và thiết bị hiệu chuẩn',
      role:   'Nhà cung cấp WIKA chính hãng tại Việt Nam',
      proof:  '',
      tpl: 'Vui lòng báo giá WIKA {model}.\n' +
           'Dải đo và đơn vị: \n' +
           'Ren / kết nối quá trình: \n' +
           'Môi chất và nhiệt độ làm việc: \n' +
           'Yêu cầu chứng từ: CO, CQ\n' +
           'Nơi giao hàng: \n' +
           'Thời điểm cần hàng: '
    },
    'Rosemount': {
      maker:  'Emerson Electric Co. (thương hiệu Rosemount)',
      origin: 'Hoa Kỳ',
      scope:  'Thiết bị đo lường quá trình: transmitter áp suất, lưu lượng, mức, nhiệt độ và hệ phân tích khí – lỏng',
      role:   'Nhà cung cấp độc lập thiết bị Rosemount chính hãng tại Việt Nam',
      proof:  'Không trực thuộc và không được Emerson ủy quyền làm đại diện chính thức.',
      tpl: 'Vui lòng báo giá {model}.\n' +
           'Môi chất: \n' +
           'Dải đo: \n' +
           'Nhiệt độ và áp suất làm việc: \n' +
           'Kết nối process (ren / mặt bích, tiêu chuẩn, vật liệu): \n' +
           'Tín hiệu ra (4-20 mA HART / Fieldbus / WirelessHART): \n' +
           'Chứng chỉ yêu cầu (SIL, ATEX / IECEx): \n' +
           'Yêu cầu chứng từ: CO, CQ, EN 10204 3.1 MTC\n' +
           'Số lượng: \n' +
           'Nơi giao hàng: \n' +
           'Thời điểm cần hàng: '
    },
    'Endress+Hauser': {
      maker:  'Endress+Hauser Group',
      origin: 'Thụy Sĩ',
      scope:  'Thiết bị đo lường quá trình: lưu lượng, mức, áp suất, nhiệt độ và phân tích',
      role:   'Nhà cung cấp Endress+Hauser chính hãng tại Việt Nam',
      proof:  '',
      tpl: 'Vui lòng báo giá Endress+Hauser {model}.\n' +
           'Môi chất: \n' +
           'Nhiệt độ và áp suất làm việc: \n' +
           'Kết nối quá trình (ren / mặt bích): \n' +
           'Tín hiệu ra (4-20 mA / HART / PROFIBUS): \n' +
           'Chứng nhận phòng nổ (ATEX / IECEx) nếu cần: \n' +
           'Yêu cầu chứng từ: CO, CQ\n' +
           'Nơi giao hàng: \n' +
           'Thời điểm cần hàng: '
    },
    'Diffu-Therm': {
      maker:  'Helmut Klumpf Technische Chemie KG',
      origin: 'Herten, Đức',
      scope:  'Vật tư kiểm tra không phá hủy: chất thẩm thấu PT, bột từ MT, hệ UV huỳnh quang',
      role:   'Nhà cung cấp Diffu-Therm chính hãng tại Việt Nam',
      proof:  '',
      tpl: 'Vui lòng báo giá Diffu-Therm {model}.\n' +
           'Phương pháp kiểm tra (PT / MT / UV): \n' +
           'Quy cách (bình xịt / can / bột): \n' +
           'Yêu cầu chứng từ: SDS, CO, CQ\n' +
           'Nơi giao hàng: \n' +
           'Thời điểm cần hàng: '
    },
    'Site mẹ': {
      maker:  'Fast Group Engineering',
      origin: 'Việt Nam',
      scope:  'Phân phối thiết bị công nghiệp chính hãng cho dự án dầu khí, điện, hóa dầu và sản xuất',
      role:   'Nhà phân phối và đại lý cung cấp hàng chính hãng tại Việt Nam',
      proof:  '',
      tpl: 'Vui lòng báo giá {model}.\n' +
           'Thông số / cấu hình: \n' +
           'Yêu cầu chứng từ: CO, CQ\n' +
           'Nơi giao hàng: \n' +
           'Thời điểm cần hàng: '
    }
  };

  var FALLBACK = {
    maker: 'Fast Group Engineering', origin: 'Việt Nam',
    scope: 'Phân phối thiết bị công nghiệp chính hãng', role: '', proof: '',
    tpl: 'Vui lòng báo giá {model}.\nYêu cầu chứng từ: CO, CQ\nNơi giao hàng: \nThời điểm cần hàng: '
  };

  /* ========================= CSS BỔ SUNG ============================= */

  var CSS =
    '.fgq-req{color:#d33;margin-left:2px}' +
    '.fgq-wrap{display:grid;grid-template-columns:minmax(0,1.65fr) minmax(0,1fr);gap:26px;align-items:start}' +
    '@media (max-width:900px){.fgq-wrap{grid-template-columns:1fr}}' +
    '.fgq-brand{margin:0 0 18px;padding:13px 16px;border-radius:8px;font-size:.92rem;line-height:1.6;' +
      'background:var(--blue-tint,var(--brand-soft,var(--wika-blue-soft,var(--soft,#f1f5f9))));' +
      'color:var(--ink,#101923)}' +
    '.fgq-brand b{display:block;font-size:1rem;margin-bottom:2px}' +
    '.fgq-brand span{color:var(--muted,#5d6b7a)}' +
    '.fgq-ctx{margin:0 0 18px;padding:11px 14px;border-radius:8px;font-size:.92rem;line-height:1.5;' +
      'border:1px dashed var(--line-strong,var(--line,#d9e1ea));color:var(--ink,#101923)}' +
    '.fgq-ctx b{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.02em}' +
    '.fgq-ctx span{color:var(--muted,#5d6b7a)}' +
    '.fgq-msg{margin:16px 0 0;padding:12px 14px;border-radius:8px;font-size:.94rem;line-height:1.55;display:none}' +
    '.fgq-msg.on{display:block}' +
    '.fgq-msg.ok{background:#e9f7ef;color:#14663a;border:1px solid #bce3cd}' +
    '.fgq-msg.err{background:#fdeceb;color:#8c1f1f;border:1px solid #f3c4c2}' +
    '.fgq-msg a{font-weight:700;text-decoration:underline;color:inherit}' +
    '.fgq-bad{border-color:#d9534f !important;background:#fffafa !important}' +
    '.fgq-trap{position:absolute !important;left:-9999px !important;width:1px;height:1px;overflow:hidden}' +
    '.fgq-busy{opacity:.6;cursor:progress}' +
    '.fgq-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}' +
    '.fgq-grid .fgq-full{grid-column:1/-1}' +
    '@media (max-width:640px){.fgq-grid{grid-template-columns:1fr}}' +
    '.fgq-side{display:grid;gap:12px}' +
    '.fgq-card{padding:16px 18px;border:1px solid var(--line,#d9e1ea);border-radius:8px;background:#fff}' +
    '.fgq-card h4{margin:0 0 6px;font-size:.78rem;font-weight:700;letter-spacing:.07em;' +
      'text-transform:uppercase;color:var(--muted,#5d6b7a)}' +
    '.fgq-card p{margin:0;font-size:.95rem;line-height:1.6;color:var(--ink,#101923)}' +
    '.fgq-card a{color:var(--ink,#101923);font-weight:600;text-decoration:none}' +
    '.fgq-card a:hover{text-decoration:underline}' +
    '.fgq-card.role{background:var(--blue-tint,var(--brand-soft,var(--wika-blue-soft,var(--soft,#f1f5f9))));' +
      'border-color:transparent}';

  /* ========================= BỘ SKIN ================================= */

  var SKINS = {
    portal: {
      form: 'form-panel', head: 'section-heading', kick: 'kicker',
      grid: 'form-grid',  field: 'field', full: 'field full',
      acts: 'form-actions', btn: 'button button-primary', alt: 'button button-secondary'
    },
    main: {
      form: 'rfq-form', head: '', kick: 'eyebrow',
      grid: 'fgq-grid', field: 'field', full: 'field fgq-full',
      acts: '', btn: 'btn btn-accent', alt: 'btn btn-line'
    }
  };

  var FIELDS = [
    { k: 'name',    label: 'Họ và tên',        type: 'text',     ac: 'name',         req: 1, full: 0 },
    { k: 'company', label: 'Công ty',          type: 'text',     ac: 'organization', req: 0, full: 0 },
    { k: 'email',   label: 'Email',            type: 'email',    ac: 'email',        req: 1, full: 0 },
    { k: 'phone',   label: 'Số điện thoại',    type: 'tel',      ac: 'tel',          req: 1, full: 0 },
    { k: 'qty',     label: 'Số lượng',         type: 'text',     ac: 'off',          req: 0, full: 0 },
    { k: 'message', label: 'Nội dung yêu cầu', type: 'textarea', ac: 'off',          req: 1, full: 1 }
  ];

  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var PHONE_RE = /^[0-9+()\s.\-]{8,20}$/;
  var seq = 0;

  /* ========================= HÀM PHỤ ================================= */

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function track(name, params) {
    if (window.gtag) { try { window.gtag('event', name, params || {}); } catch (e) {} }
  }

  function injectCSS() {
    if (document.getElementById('fgq-css')) return;
    var st = document.createElement('style');
    st.id = 'fgq-css'; st.textContent = CSS;
    (document.head || document.documentElement).appendChild(st);
  }

  /** Đọc JSON-LD Product để lấy mã hàng và tên sản phẩm. */
  function readProduct() {
    var out = { sku: '', name: '' };
    var nodes = document.querySelectorAll('script[type="application/ld+json"]');
    for (var i = 0; i < nodes.length; i++) {
      var data;
      try { data = JSON.parse(nodes[i].textContent); } catch (e) { continue; }
      var list = (Array.isArray(data) ? data : [data]);
      if (data && data['@graph']) list = list.concat(data['@graph']);
      for (var j = 0; j < list.length; j++) {
        var o = list[j];
        if (o && o['@type'] === 'Product') {
          out.sku  = out.sku  || o.sku || o.mpn || '';
          out.name = out.name || o.name || '';
        }
      }
      if (out.sku) break;
    }
    return out;
  }

  /* --------------------- PANEL THÔNG TIN HÃNG ------------------------ */

  function asideHTML(source, b) {
    var h = '<aside class="fgq-side">';
    if (b.role) {
      h += '<div class="fgq-card role"><h4>Vai trò của Fast Group</h4><p>' + esc(b.role) +
           (b.proof ? '<br><span style="color:var(--muted,#5d6b7a);font-size:.88rem">' + esc(b.proof) + '</span>' : '') +
           '</p></div>';
    }
    h += '<div class="fgq-card"><h4>Hãng sản xuất</h4><p><b>' + esc(b.maker) + '</b>' +
         (b.origin ? '<br><span style="color:var(--muted,#5d6b7a);font-size:.9rem">Xuất xứ: ' + esc(b.origin) + '</span>' : '') +
         '</p></div>';
    h += '<div class="fgq-card"><h4>Hotline / Zalo</h4><p>' +
         '<a href="tel:' + CONTACT.tel + '" data-fg="call">' + CONTACT.telTxt + '</a> · ' +
         '<a href="' + CONTACT.zalo + '" target="_blank" rel="noopener" data-fg="zalo">Zalo</a></p></div>';
    h += '<div class="fgq-card"><h4>Email</h4><p><a href="mailto:' + CONTACT.email +
         '" data-fg="mail">' + CONTACT.email + '</a></p></div>';
    h += '<div class="fgq-card"><h4>Văn phòng</h4><p>' + esc(CONTACT.office) +
         '<br><span style="color:var(--muted,#5d6b7a);font-size:.9rem">' + esc(CONTACT.office2) + '</span></p></div>';
    h += '</aside>';
    return h;
  }

  /* ========================= DỰNG FORM =============================== */

  function build(box) {
    var skin   = SKINS[box.getAttribute('data-fg-skin') || 'portal'] || SKINS.portal;
    var source = box.getAttribute('data-fg-source') || 'Không rõ';
    var model  = (box.getAttribute('data-fg-model') || '').trim();
    var title  = box.getAttribute('data-fg-title') || 'Gửi yêu cầu báo giá';
    var note   = box.getAttribute('data-fg-note') || '';
    var side   = box.getAttribute('data-fg-aside') === '1';
    var b      = BRANDS[source] || FALLBACK;
    var id     = 'fgq' + (++seq);

    /* nội dung soạn sẵn: chỉ khi đang hỏi giá một mã cụ thể */
    var draft = model ? b.tpl.replace(/\{model\}/g, model) : '';

    var h = '<form class="' + skin.form + '" id="' + id + '" novalidate>';

    if (skin.head) {
      h += '<div class="' + skin.head + '">' +
           '<div class="' + skin.kick + '">RFQ ' + esc(source) + '</div>' +
           '<h2>' + esc(title) + '</h2>' +
           (note ? '<p>' + esc(note) + '</p>' : '') + '</div>';
    } else {
      h += '<span class="' + skin.kick + '">RFQ ' + esc(source) + '</span>' +
           '<h3 style="margin:6px 0 16px">' + esc(title) + '</h3>' +
           (note ? '<p style="margin:-8px 0 18px;color:var(--muted)">' + esc(note) + '</p>' : '');
    }

    /* dải thông tin hãng — luôn có, để form nào cũng gắn đúng hãng */
    h += '<p class="fgq-brand"><b>' + esc(b.maker) + (b.origin ? ' · ' + esc(b.origin) : '') + '</b>' +
         '<span>' + esc(b.scope) + '</span></p>';

    if (model) {
      h += '<p class="fgq-ctx">Đang hỏi giá mã <b>' + esc(model) + '</b> ' +
           '<span>— đã gửi kèm và đã soạn sẵn nội dung bên dưới, anh/chị chỉ cần điền số lượng ' +
           'và các thông số còn trống.</span></p>';
    }

    h += '<div class="' + skin.grid + '">';
    for (var i = 0; i < FIELDS.length; i++) {
      var f = FIELDS[i], fid = id + '-' + f.k;
      var req = f.req || (f.k === 'qty' && model);          // có mã hàng thì bắt buộc số lượng
      h += '<div class="' + (f.full ? skin.full : skin.field) + '">' +
           '<label for="' + fid + '">' + esc(f.label) +
           (req ? '<span class="fgq-req">*</span>' : '') + '</label>' +
           (f.type === 'textarea'
             ? '<textarea id="' + fid + '" rows="8" autocomplete="off">' + esc(draft) + '</textarea>'
             : '<input id="' + fid + '" type="' + f.type + '" autocomplete="' + f.ac + '">') +
           '</div>';
    }
    h += '</div>';

    h += '<div class="fgq-trap" aria-hidden="true">' +
         '<label for="' + id + '-trap">Bỏ trống ô này</label>' +
         '<input id="' + id + '-trap" type="text" tabindex="-1" autocomplete="off"></div>';

    h += (skin.acts ? '<div class="' + skin.acts + '">' : '<div style="margin-top:20px;display:flex;gap:12px;flex-wrap:wrap">') +
         '<button class="' + skin.btn + '" type="submit">Gửi yêu cầu báo giá</button>' +
         '<a class="' + skin.alt + '" href="tel:' + CONTACT.tel + '" data-fg="call">Gọi ' + CONTACT.telTxt + '</a>' +
         '</div>';

    h += '<div class="fgq-msg" id="' + id + '-msg" role="status" aria-live="polite"></div></form>';

    box.innerHTML = side ? '<div class="fgq-wrap">' + h + asideHTML(source, b) + '</div>' : h;
    wire(document.getElementById(id), { source: source, model: model, id: id, hasModel: !!model });
  }

  /* ========================= XỬ LÝ GỬI =============================== */

  function wire(form, cfg) {
    if (!form) return;
    var msg  = document.getElementById(cfg.id + '-msg');
    var btn  = form.querySelector('button[type=submit]');
    var born = Date.now();

    function el(k)  { return document.getElementById(cfg.id + '-' + k); }
    function val(k) { var e = el(k); return e ? e.value.trim() : ''; }
    function mark(k, bad) { var e = el(k); if (e) e.classList[bad ? 'add' : 'remove']('fgq-bad'); }
    function show(kind, html) { msg.className = 'fgq-msg on ' + kind; msg.innerHTML = html; }

    var HELP = 'Hoặc gọi <a href="tel:' + CONTACT.tel + '">' + CONTACT.telTxt + '</a>' +
               ' / nhắn <a href="' + CONTACT.zalo + '" target="_blank" rel="noopener">Zalo</a>.';

    function mailtoFallback(d) {
      var body = [
        'Ho va ten: ' + d.name,
        'Cong ty: ' + d.company,
        'Email: ' + d.email,
        'So dien thoai: ' + d.phone,
        d.model ? 'Ma hang: ' + d.model : '',
        d.qty ? 'So luong: ' + d.qty : '',
        'Nguon: ' + d.source,
        '', 'Noi dung:', d.message
      ].filter(Boolean).join('\n');

      window.location.href = 'mailto:' + CONTACT.email +
        '?subject=' + encodeURIComponent('[RFQ] ' + (d.model || 'Chua co ma') + ' - ' + (d.company || d.name)) +
        '&body=' + encodeURIComponent(body);
    }

    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (val('trap')) return;
      if (Date.now() - born < 1500) return;

      var d = {
        token: TOKEN, source: cfg.source, model: cfg.model,
        page: location.href, ua: navigator.userAgent,
        name: val('name'), company: val('company'), email: val('email'),
        phone: val('phone'), qty: val('qty'), message: val('message')
      };

      var miss = [];
      if (d.name.length < 2)       { mark('name', 1);    miss.push('họ và tên'); }     else mark('name', 0);
      if (!EMAIL_RE.test(d.email)) { mark('email', 1);   miss.push('email hợp lệ'); }  else mark('email', 0);
      if (!PHONE_RE.test(d.phone)) { mark('phone', 1);   miss.push('số điện thoại'); } else mark('phone', 0);
      if (cfg.hasModel && !d.qty)  { mark('qty', 1);     miss.push('số lượng'); }      else mark('qty', 0);
      if (d.message.length < 5)    { mark('message', 1); miss.push('nội dung yêu cầu'); } else mark('message', 0);

      if (miss.length) {
        show('err', 'Vui lòng nhập: ' + miss.join(', ') + '.');
        track('rfq_invalid', { source: cfg.source, fields: miss.join('|') });
        return;
      }

      var label = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.classList.add('fgq-busy'); btn.textContent = 'Đang gửi…'; }
      show('ok', 'Đang gửi yêu cầu…');
      function done() {
        if (btn) { btn.disabled = false; btn.classList.remove('fgq-busy'); btn.textContent = label; }
      }

      var EP = endpoint();
      if (!EP) {
        done();
        show('ok', 'Đang mở phần mềm email của bạn với nội dung đã điền sẵn. ' + HELP);
        track('rfq_fallback_mailto', { source: cfg.source });
        mailtoFallback(d);
        return;
      }

      /* Apps Script không xử lý được CORS preflight, nên bắt buộc gửi
         text/plain (yêu cầu "đơn giản", không sinh OPTIONS); phía server
         parse JSON từ e.postData.contents. */
      fetch(EP, {
        method: 'POST', redirect: 'follow',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(d)
      })
        .then(function (r) {
          if (!r.ok) throw new Error('HTTP ' + r.status);
          return r.text();
        })
        .then(function (t) {
          var res = {};
          try { res = JSON.parse(t); } catch (e) {}
          if (res.ok === false) throw new Error(res.error || 'rejected');
          done();
          form.reset();
          show('ok', 'Đã nhận yêu cầu' + (res.ref ? ' (mã <b>' + esc(res.ref) + '</b>)' : '') +
                     '. Fast Group sẽ phản hồi trong giờ làm việc. ' + HELP);
          track('generate_lead', { form: 'rfq', source: cfg.source, model: cfg.model || '(none)' });
        })
        .catch(function () {
          done();
          show('err', 'Chưa gửi được qua web. Đang mở phần mềm email của bạn với nội dung đã điền sẵn. ' + HELP);
          track('rfq_fallback_mailto', { source: cfg.source });
          mailtoFallback(d);
        });
    });
  }

  /* ================= TỰ GẮN VÀO TRANG SẢN PHẨM ======================= */

  function autoMount() {
    if (!window.FG_RFQ_SOURCE) return;
    if (document.querySelector('[data-fg-rfq]')) return;

    var p = readProduct();
    if (!p.sku) return;                          // không phải trang sản phẩm

    var foot = document.querySelector('footer');
    if (!foot || !foot.parentNode) return;

    var sec = document.createElement('section');
    sec.className = 'section';
    sec.id = 'rfq';
    var box = document.createElement('div');
    box.setAttribute('data-fg-rfq', '');
    box.setAttribute('data-fg-source', window.FG_RFQ_SOURCE);
    box.setAttribute('data-fg-model', p.sku);
    box.setAttribute('data-fg-aside', '1');
    box.setAttribute('data-fg-title', 'Yêu cầu báo giá ' + (p.name || p.sku));
    box.setAttribute('data-fg-note',
      'Nội dung đã soạn sẵn theo mã hàng — anh/chị điền số lượng và các thông số còn trống rồi gửi.');

    var wrap = document.createElement('div');
    wrap.className = 'container';
    wrap.appendChild(box);
    sec.appendChild(wrap);
    foot.parentNode.insertBefore(sec, foot);
  }

  /* ========================= KHỞI ĐỘNG =============================== */

  function init() {
    autoMount();
    var boxes = document.querySelectorAll('[data-fg-rfq]');
    if (!boxes.length) return;
    injectCSS();
    for (var i = 0; i < boxes.length; i++) {
      if (boxes[i].getAttribute('data-fg-done')) continue;
      boxes[i].setAttribute('data-fg-done', '1');
      build(boxes[i]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
