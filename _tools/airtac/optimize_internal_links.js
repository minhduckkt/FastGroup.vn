const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const ROOT = path.resolve(__dirname, "..", "..");
const SITE = path.join(ROOT, "airtac-viet-nam");
const INDEX_JS = path.join(SITE, "assets", "search-index.js");
const CSS = path.join(SITE, "assets", "site.css");
const MARK = "data-fg-airtac-optimizer";

const groupConfig = {
  "Preparation Units": {
    tone: "t-prep",
    category: "bo-loc-dieu-ap-khi-nen/",
    categoryTitle: "Bộ lọc, điều áp và xử lý khí AirTAC",
    guide: "huong-dan/chon-bo-loc-dieu-ap-frl-airtac/",
    guideTitle: "Cách chọn bộ lọc điều áp FRL AirTAC",
    blog: "blog/bo-loc-dieu-ap-frl-airtac-gac-gafr-gar-gal/",
    blogTitle: "FRL AirTAC GAC, GAFR, GAR, GAL",
    rfqFields: ["mã series", "cỡ cổng", "dải áp", "cấp lọc", "kiểu xả nước", "lưu lượng yêu cầu"],
    whenUse: "Dùng cho cụm xử lý khí đầu nguồn, tủ khí nén, cụm van và xi lanh cần khí sạch, áp ổn định trước khi vận hành.",
    caution: "Không nên chọn FRL chỉ theo cỡ ren; lưu lượng, dải áp, cấp lọc và không gian bảo trì mới là các điểm cần đối chiếu.",
    priority: ["GAC Series", "GAFR Series", "GAR Series", "GAL Series", "GPFR Series", "GAF Series"]
  },
  "Control Components": {
    tone: "t-control",
    category: "van-dien-tu-khi-nen/",
    categoryTitle: "Van điện từ và van điều khiển AirTAC",
    guide: "huong-dan/chon-van-dien-tu-airtac/",
    guideTitle: "Cách chọn van điện từ AirTAC",
    blog: "blog/van-dien-tu-airtac-4v-3v-6d-7v/",
    blogTitle: "Van điện từ AirTAC 4V, 3V, 6D, 7V",
    rfqFields: ["mã van đầy đủ", "điện áp coil", "số cổng/vị trí", "cỡ cổng", "chuẩn ren", "manifold nếu có"],
    whenUse: "Phù hợp cho tủ điều khiển khí nén, cơ cấu xi lanh tác động đơn/kép, cụm cấp phôi và máy đóng gói.",
    caution: "Cùng một series van có thể khác điện áp coil, trạng thái trung tâm, kiểu pilot, cổng ren và phụ kiện manifold.",
    priority: ["4V100 Series", "4V200 Series", "4V300 Series", "4V400 Series", "3V100 Series", "3V200 Series", "3V300 Series", "6D/6DW Series", "7V Series"]
  },
  "Actuators": {
    tone: "t-actuator",
    category: "xi-lanh-khi-nen/",
    categoryTitle: "Xi lanh khí nén và cơ cấu chấp hành AirTAC",
    guide: "huong-dan/chon-xi-lanh-khi-nen-airtac/",
    guideTitle: "Cách chọn xi lanh khí nén AirTAC",
    blog: "blog/xi-lanh-khi-nen-airtac-cach-chon/",
    blogTitle: "Xi lanh khí nén AirTAC: bore, stroke và gá lắp",
    rfqFields: ["series", "bore", "stroke", "kiểu gá", "cảm biến từ", "ren cổng", "tải làm việc"],
    whenUse: "Dùng cho cơ cấu đẩy/kéo, kẹp gắp, bàn trượt, xoay và các cụm tự động cần chuyển động khí nén.",
    caution: "Khi thay thế xi lanh, kích thước lắp, bore/stroke, vị trí gá và cảm biến từ thường quan trọng hơn tên gọi series.",
    priority: ["SC Series", "SDA Series", "ACQ Series", "MAL Series", "HFC Series", "HRQ Series", "TR Series"]
  },
  "Fittings & Tubing & Accessories": {
    tone: "t-fitting",
    category: "dau-noi-ong-khi-nen/",
    categoryTitle: "Đầu nối, ống và phụ kiện khí nén AirTAC",
    guide: "huong-dan/chon-dau-noi-ong-khi-nen-airtac/",
    guideTitle: "Cách chọn đầu nối và ống khí nén AirTAC",
    blog: "blog/dau-noi-ong-khi-nen-airtac-fitting-tubing/",
    blogTitle: "Fitting, tube và speed controller AirTAC",
    rfqFields: ["đường kính ống", "chuẩn ren", "hình dạng đầu nối", "vật liệu", "hướng chỉnh lưu lượng", "số lượng"],
    whenUse: "Dùng để đấu nối đường khí, chỉnh tốc độ xi lanh, giảm ồn xả khí và hoàn thiện cụm lắp đặt trong máy.",
    caution: "Nhầm đường kính ống hoặc chuẩn ren PT/NPT là lỗi phổ biến; nên gửi ảnh fitting cũ hoặc kích thước đo thực tế.",
    priority: ["PC-", "PL-", "PY-", "PU-", "Speed Controller Series", "Silencer Series", "NPL Series"]
  },
  Guide: {
    tone: "t-guide",
    category: "thanh-truot-linear-guide/",
    categoryTitle: "Linear guide và thanh trượt AirTAC",
    guide: "huong-dan/chon-linear-guide-airtac/",
    guideTitle: "Cách chọn linear guide AirTAC",
    blog: "huong-dan/chon-linear-guide-airtac/",
    blogTitle: "Hướng dẫn chọn linear guide AirTAC",
    rfqFields: ["series", "chiều dài ray", "loại block", "tải/moment", "cấp chính xác", "điều kiện bôi trơn"],
    whenUse: "Phù hợp cho cơ cấu trượt, dẫn hướng chính xác, pick-and-place và cụm chuyển động cần độ cứng tốt.",
    caution: "Cần đối chiếu chiều cao block, vị trí lỗ bắt vít, chiều dài ray và tải moment trước khi thay thế.",
    priority: ["LSH Series", "LSD Series", "LRM Series", "LGC Series", "LRW Series"]
  }
};

const categoryBySlug = {
  "bo-loc-dieu-ap-khi-nen": "Preparation Units",
  "van-dien-tu-khi-nen": "Control Components",
  "xi-lanh-khi-nen": "Actuators",
  "dau-noi-ong-khi-nen": "Fittings & Tubing & Accessories",
  "thanh-truot-linear-guide": "Guide"
};

function readIndex() {
  const code = fs.readFileSync(INDEX_JS, "utf8");
  const context = { window: {} };
  vm.createContext(context);
  vm.runInContext(code, context);
  return context.window.AT_INDEX || [];
}

function esc(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function stripTags(value) {
  return String(value || "").replace(/<[^>]*>/g, "").replace(/\s+/g, " ").trim();
}

function fileList(dir) {
  const out = [];
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) out.push(...fileList(full));
    else if (item.isFile() && item.name === "index.html") out.push(full);
  }
  return out;
}

function depthFor(rel) {
  const parts = rel.split(path.sep);
  return parts.length - 1;
}

function prefixFor(rel) {
  const depth = depthFor(rel);
  if (depth <= 0) return "";
  return "../".repeat(depth);
}

function url(prefix, target) {
  return `${prefix}${target}`;
}

function getTitle(html) {
  const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
  return stripTags(h1 ? h1[1] : "");
}

function getDescription(html) {
  const meta = html.match(/<meta name="description" content="([^"]*)"/i);
  return meta ? meta[1] : "";
}

function getSeriesLink(html) {
  const m = html.match(/<a href="\.\.\/\.\.\/series\/([^/]+)\/">([^<]+)<\/a>/i);
  return m ? { slug: m[1], title: stripTags(m[2]), url: `series/${m[1]}/` } : null;
}

function groupFromHtml(html, rel) {
  const top = rel.split(path.sep)[0];
  if (categoryBySlug[top]) return categoryBySlug[top];
  const category = html.match(/<a href="\.\.\/\.\.\/([^"/]+)\/">([^<]+AirTAC)<\/a>/i)
    || html.match(/<a href="\.\.\/([^"/]+)\/">([^<]+AirTAC)<\/a>/i);
  if (category && categoryBySlug[category[1]]) return categoryBySlug[category[1]];
  const productJson = html.match(/"category":\s*"([^"]+)"/);
  if (productJson && groupConfig[productJson[1]]) return productJson[1];
  for (const [slug, group] of Object.entries(categoryBySlug)) {
    if (html.includes(`/${slug}/`) || html.includes(`../${slug}/`) || html.includes(`../../${slug}/`)) return group;
  }
  return "Control Components";
}

function currentUrlFromRel(rel) {
  return rel.replace(/\\/g, "/").replace(/index\.html$/, "");
}

function groupFromIndex(rel, index) {
  const current = currentUrlFromRel(rel);
  const hit = index.find((item) => item.u === current);
  return hit && groupConfig[hit.g] ? hit.g : null;
}

function removeOptimizerBlocks(html) {
  return html.replace(/<section\b(?=[^>]*data-fg-airtac-optimizer)[\s\S]*?<\/section>/g, "");
}

function pageType(rel) {
  const parts = rel.split(path.sep);
  if (parts[0] === "san-pham" && parts.length > 2) return "product";
  if (parts[0] === "series" && parts.length > 2) return "series";
  if (parts[0] === "blog" && parts.length > 2) return "blog";
  if (parts[0] === "huong-dan" && parts.length > 2) return "guide";
  if (parts.length === 2 && categoryBySlug[parts[0]]) return "category";
  if (parts[0] === "tra-cuu-part-number") return "search";
  if (parts[0] === "lien-he") return "contact";
  if (parts[0] === "blog") return "blog-index";
  if (parts[0] === "huong-dan") return "guide-index";
  if (parts.length === 1) return "home";
  return "other";
}

function groupEntries(index, group, type) {
  return index.filter((item) => item.g === group && (!type || item.t === type));
}

function prioritized(entries, cfg, count, currentUrl = "") {
  const seen = new Set();
  const picked = [];
  for (const name of cfg.priority) {
    const hit = entries.find((item) => item.n === name || item.c === name || item.n.startsWith(name));
    if (hit && hit.u !== currentUrl && !seen.has(hit.u)) {
      picked.push(hit);
      seen.add(hit.u);
    }
  }
  for (const hit of entries) {
    if (picked.length >= count) break;
    if (hit.u !== currentUrl && !seen.has(hit.u)) {
      picked.push(hit);
      seen.add(hit.u);
    }
  }
  return picked.slice(0, count);
}

function linkGrid(prefix, links) {
  return `<div class="airtac-link-grid">${links.map((item) => (
    `<a href="${esc(url(prefix, item.u))}"><span>${esc(item.kicker || item.t || item.g || "AirTAC")}</span><strong>${esc(item.n || item.title)}</strong><small>${esc(item.d || "")}</small></a>`
  )).join("")}</div>`;
}

function quickPath(prefix, group, title, series) {
  const cfg = groupConfig[group];
  const links = [
    { u: cfg.category, n: cfg.categoryTitle, t: "Danh mục", d: "Mở toàn bộ nhóm sản phẩm cùng chức năng." },
    { u: cfg.guide, n: cfg.guideTitle, t: "Hướng dẫn", d: "Đọc nhanh các điểm cần xác nhận trước khi chốt mã." },
    { u: cfg.blog, n: cfg.blogTitle, t: "Bài viết", d: "Xem thêm ngữ cảnh chọn hàng và gửi RFQ." },
    { u: "tra-cuu-part-number/", n: "Tra cứu part number AirTAC", t: "Tra mã", d: "Tìm theo series, model hoặc nhóm sản phẩm." },
    { u: "lien-he/", n: "Gửi RFQ cho Fast Group", t: "RFQ", d: "Gửi mã hàng, số lượng và yêu cầu chứng từ." }
  ];
  if (series) links.splice(1, 0, { u: series.url, n: `${series.title} AirTAC`, t: "Series", d: `Xem sản phẩm, datasheet và các trang liên quan của ${series.title}.` });
  return `<section class="section airtac-deep-links ${cfg.tone}" ${MARK}="quick-path"><div class="container"><div class="section-heading"><div class="kicker">Liên kết nội bộ</div><h2>Xem tiếp sau ${esc(title)}</h2><p>Những trang dưới đây giúp đối chiếu nhóm sản phẩm, đọc hướng dẫn chọn mã và gửi RFQ đúng thông tin.</p></div>${linkGrid(prefix, links)}</div></section>`;
}

function decisionBlock(prefix, group, title, seriesLinks, currentUrl = "") {
  const cfg = groupConfig[group];
  const cards = prioritized(seriesLinks, cfg, 6, currentUrl);
  return `<section class="section section-soft airtac-decision ${cfg.tone}" ${MARK}="decision"><div class="container split"><div><div class="section-heading"><div class="kicker">Ngữ cảnh chọn hàng</div><h2>Khi nào nên chọn ${esc(title)}</h2></div><p>${esc(cfg.whenUse)}</p><p>${esc(cfg.caution)}</p><h3>Thông tin nên chuẩn bị</h3><ul class="check-list">${cfg.rfqFields.map((x) => `<li>${esc(x)}</li>`).join("")}</ul></div><div class="tech-panel"><h3>Series cùng nhóm nên đối chiếu</h3>${linkGrid(prefix, cards.map((x) => ({ ...x, kicker: "Series" })))}<a class="button button-primary" href="${esc(url(prefix, "lien-he/"))}">Gửi RFQ AirTAC</a></div></div></section>`;
}

function faqBlock(prefix, group, title) {
  const cfg = groupConfig[group];
  return `<section class="section airtac-faq" ${MARK}="faq"><div class="container"><div class="section-heading"><div class="kicker">FAQ</div><h2>Câu hỏi nhanh về ${esc(title)}</h2></div><div class="faq-list"><details class="faq-item"><summary>Cần thông tin gì để báo giá nhanh?</summary><p>Nên gửi ${esc(cfg.rfqFields.slice(0, 4).join(", "))}, số lượng, nơi giao hàng và yêu cầu chứng từ. Nếu thay thế hàng cũ, ảnh tem và ảnh vị trí lắp sẽ giúp kiểm tra nhanh hơn.</p></details><details class="faq-item"><summary>Fast Group có hỗ trợ chứng từ không?</summary><p>Fast Group Engineering cung cấp AirTAC chính hãng và có thể chuẩn bị hóa đơn VAT, CO/CQ hoặc chứng từ theo điều kiện từng đơn hàng khi khách nêu rõ từ đầu.</p></details><details class="faq-item"><summary>Nên xem trang nào trước khi gửi RFQ?</summary><p>Hãy mở <a href="${esc(url(prefix, cfg.category))}">nhóm sản phẩm</a>, <a href="${esc(url(prefix, cfg.guide))}">hướng dẫn chọn mã</a> và trang series liên quan để đối chiếu datasheet, kích thước và phụ kiện.</p></details></div></div></section>`;
}

function categoryPath(prefix, group) {
  const cfg = groupConfig[group];
  return `<section class="section airtac-category-path ${cfg.tone}" ${MARK}="category-path"><div class="container"><div class="section-heading"><div class="kicker">Luồng tra cứu</div><h2>Từ danh mục đến RFQ</h2><p>Khách hàng thường đi theo luồng: chọn nhóm sản phẩm, mở series phù hợp, kiểm datasheet, rồi gửi mã đầy đủ để báo giá.</p></div><div class="airtac-process"><div><strong>1. Chọn đúng nhóm</strong><p>${esc(cfg.whenUse)}</p></div><div><strong>2. Đối chiếu series</strong><p>${esc(cfg.caution)}</p></div><div><strong>3. Gửi RFQ đủ dữ liệu</strong><p>Cần ${esc(cfg.rfqFields.slice(0, 5).join(", "))} và số lượng.</p></div></div>${linkGrid(prefix, [
    { u: cfg.guide, n: cfg.guideTitle, t: "Hướng dẫn", d: "Checklist chọn mã theo nhóm." },
    { u: cfg.blog, n: cfg.blogTitle, t: "Bài viết", d: "Ngữ cảnh mua hàng và lỗi cần tránh." },
    { u: "tra-cuu-part-number/", n: "Tra cứu part number AirTAC", t: "Tra mã", d: "Tìm nhanh series và model." },
    { u: "lien-he/", n: "Gửi RFQ AirTAC", t: "Liên hệ", d: "Gửi mã hàng, số lượng và chứng từ cần có." }
  ])}</div></section>`;
}

function globalNavBlock(prefix) {
  return `<section class="section section-soft airtac-category-path t-control" ${MARK}="global-path"><div class="container"><div class="section-heading"><div class="kicker">Điều hướng AirTAC</div><h2>Tra cứu theo nhu cầu kỹ thuật</h2><p>Mở nhanh danh mục, hướng dẫn và trang RFQ để đi từ nhu cầu kỹ thuật đến mã hàng cần báo giá.</p></div>${linkGrid(prefix, [
    { u: "van-dien-tu-khi-nen/", n: "Van điện từ AirTAC", t: "Danh mục", d: "4V, 3V, 6D, 7V, manifold và coil." },
    { u: "xi-lanh-khi-nen/", n: "Xi lanh khí nén AirTAC", t: "Danh mục", d: "Bore, stroke, kiểu gá, cảm biến và tải." },
    { u: "bo-loc-dieu-ap-khi-nen/", n: "FRL và xử lý khí AirTAC", t: "Danh mục", d: "GAC, GAFR, GAR, GAL, lọc và điều áp." },
    { u: "dau-noi-ong-khi-nen/", n: "Fitting, ống và phụ kiện", t: "Danh mục", d: "PC, PL, PU, speed controller và silencer." },
    { u: "tra-cuu-part-number/", n: "Tra cứu part number", t: "Tra mã", d: "Tìm theo series, model hoặc nhóm sản phẩm." },
    { u: "lien-he/", n: "Gửi RFQ AirTAC", t: "Liên hệ", d: "Gửi mã hàng và yêu cầu chứng từ." }
  ])}</div></section>`;
}

function optimizeHtml(html, rel, index) {
  const original = html;
  html = removeOptimizerBlocks(html);
  const type = pageType(rel);
  if (type === "other") return { html, changed: html !== original };

  const prefix = prefixFor(rel);
  const group = groupFromIndex(rel, index) || groupFromHtml(html, rel);
  const cfg = groupConfig[group];
  const title = getTitle(html) || "trang AirTAC này";
  const series = getSeriesLink(html);
  const groupSeries = groupEntries(index, group, "Series");
  const currentUrl = currentUrlFromRel(rel);

  let additions = "";
  if (type === "product") {
    additions = quickPath(prefix, group, title, series)
      + decisionBlock(prefix, group, series ? series.title : title, groupSeries, series ? series.url : currentUrl)
      + faqBlock(prefix, group, title);
  } else if (type === "series") {
    additions = decisionBlock(prefix, group, title.replace(/\s+AirTAC$/, ""), groupSeries, currentUrl)
      + quickPath(prefix, group, title, null)
      + faqBlock(prefix, group, title);
  } else if (type === "category") {
    additions = categoryPath(prefix, group)
      + decisionBlock(prefix, group, cfg.categoryTitle.replace(" AirTAC", ""), groupSeries, "")
      + faqBlock(prefix, group, cfg.categoryTitle);
  } else if (type === "guide" || type === "blog") {
    additions = quickPath(prefix, group, title, null)
      + faqBlock(prefix, group, title);
  } else if (["home", "search", "contact", "blog-index", "guide-index"].includes(type)) {
    additions = globalNavBlock(prefix);
  }

  if (!additions || !html.includes("</main>")) return { html, changed: html !== original };
  const next = html.replace("</main>", `${additions}</main>`);
  return { html: next, changed: next !== original };
}

function appendCss() {
  const css = fs.readFileSync(CSS, "utf8");
  if (css.includes("AirTAC internal optimizer")) return false;
  const extra = `

/* AirTAC internal optimizer */
.airtac-deep-links,.airtac-decision,.airtac-faq,.airtac-category-path{position:relative}
.airtac-link-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:2px}
.airtac-link-grid a{display:block;min-height:132px;padding:20px;background:#fff;border:1px solid var(--line);transition:border-color .18s ease,box-shadow .18s ease}
.airtac-link-grid a:hover{border-color:var(--tone,var(--blue));box-shadow:0 10px 28px rgba(39,50,55,.08)}
.airtac-link-grid span{display:block;margin-bottom:8px;color:var(--muted);font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.airtac-link-grid strong{display:block;color:var(--ink);line-height:1.32}
.airtac-link-grid small{display:block;margin-top:8px;color:var(--muted);font-size:.9rem;line-height:1.45}
.airtac-process{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:2px;margin:0 0 28px}
.airtac-process>div{background:#fff;border:1px solid var(--line);padding:22px}
.airtac-process strong{display:block;color:var(--ink);margin-bottom:8px}
.airtac-process p{margin:0;color:var(--ink-soft)}
.airtac-decision .tech-panel .airtac-link-grid{grid-template-columns:1fr;gap:1px;margin-bottom:16px}
.airtac-decision .tech-panel .airtac-link-grid a{min-height:0;padding:14px 16px}
@media (max-width:980px){.airtac-link-grid,.airtac-process{grid-template-columns:1fr 1fr}}
@media (max-width:640px){.airtac-link-grid,.airtac-process{grid-template-columns:1fr}.airtac-link-grid a{min-height:0}}
`;
  fs.writeFileSync(CSS, css + extra, "utf8");
  return true;
}

function main() {
  const index = readIndex();
  const files = fileList(SITE);
  let changed = 0;
  for (const file of files) {
    const rel = path.relative(SITE, file);
    const html = fs.readFileSync(file, "utf8");
    const result = optimizeHtml(html, rel, index);
    if (result.changed) {
      fs.writeFileSync(file, result.html, "utf8");
      changed += 1;
    }
  }
  const cssChanged = appendCss();
  console.log(JSON.stringify({ changedHtmlFiles: changed, cssChanged, totalHtmlFiles: files.length }, null, 2));
}

main();
