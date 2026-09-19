const fs = require("node:fs");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..", "..");
const SITE = path.join(ROOT, "airtac-viet-nam");
const CSS = path.join(SITE, "assets", "site.css");
const MARK = "data-fg-airtac-priority";

const families = {
  control4v: {
    slugs: ["4v-5v", "4v100-series", "4v200-series", "4v300-series", "4v400-series"],
    tone: "t-control",
    kicker: "Series trọng điểm",
    heading: "Van điện từ AirTAC 4V cho tủ khí nén và máy tự động",
    lead: "Nhóm 4V thường được hỏi nhiều cho xi lanh tác động kép, cụm van trên máy đóng gói, jig gá và tủ điều khiển khí nén. Khi gửi RFQ, nên nêu rõ điện áp coil, cỡ cổng, chuẩn ren, số vị trí và có dùng manifold hay không.",
    points: [
      "4V100/4V200/4V300/4V400 khác nhau về cỡ thân, lưu lượng và cỡ cổng; không nên chọn chỉ theo hình ảnh.",
      "Mã 5/2 và 5/3 cần kiểm tra trạng thái trung tâm, kiểu pilot và phụ kiện coil.",
      "Với máy đang chạy, ảnh tem van, ảnh coil và ảnh manifold giúp Fast Group kiểm tra nhanh mã thay thế."
    ],
    links: [
      ["series/4v100-series/", "4V100 Series"],
      ["series/4v200-series/", "4V200 Series"],
      ["series/4v300-series/", "4V300 Series"],
      ["series/4v400-series/", "4V400 Series"],
      ["blog/van-dien-tu-airtac-4v-3v-6d-7v/", "Bài chọn van 4V/3V"]
    ]
  },
  control3v: {
    slugs: ["3v", "3v1-series", "3v100-series", "3v200-series", "3v300-series", "3v2-series", "3v3-series", "3v2m-series"],
    tone: "t-control",
    kicker: "Series trọng điểm",
    heading: "Van điện từ AirTAC 3V cho xi lanh tác động đơn và tín hiệu khí",
    lead: "Nhóm 3V phù hợp các mạch 3/2, điều khiển xi lanh tác động đơn, pilot khí hoặc các cụm cần on/off nhanh. Điểm cần xác nhận là điện áp coil, kiểu thường đóng/thường mở, cỡ cổng và lưu lượng thực tế.",
    points: [
      "3V100, 3V200 và 3V300 nên đối chiếu theo lưu lượng, kích thước thân van và cổng ren.",
      "Khi thay thế, cần kiểm tra kiểu van đang dùng là 3/2 hay biến thể manifold.",
      "Nếu dùng chung manifold với van khác, nên gửi ảnh mặt đế và số station để tránh nhầm phụ kiện."
    ],
    links: [
      ["series/3v100-series/", "3V100 Series"],
      ["series/3v200-series/", "3V200 Series"],
      ["series/3v300-series/", "3V300 Series"],
      ["series/3v2m-series/", "3V2M Series"],
      ["huong-dan/chon-van-dien-tu-airtac/", "Guide chọn van điện từ"]
    ]
  },
  prep: {
    slugs: ["gac-series", "gac100-series", "gafc-series", "gafc100-series", "gafr-series", "gafr100-series", "gaf-series", "gaf100-series", "gar-series", "gar100-series", "gal-series", "gal100-series", "gpfr-series"],
    tone: "t-prep",
    kicker: "Series trọng điểm",
    heading: "FRL AirTAC cho nguồn khí ổn định trước van và xi lanh",
    lead: "GAC, GAFR, GAF, GAR và GAL là các nhóm cần chọn theo lưu lượng, dải áp, cấp lọc, cỡ cổng và không gian bảo trì. Với hệ thống nhà máy, chọn đúng FRL giúp giảm tụt áp, nước ngưng và lỗi vận hành ở cụm van/xi lanh.",
    points: [
      "GAF là lọc, GAR là điều áp, GAL là tra dầu; GAFR/GAC là cụm kết hợp tùy nhu cầu lắp đặt.",
      "Cần đối chiếu lưu lượng danh định với mức tiêu thụ khí của máy, không chỉ so cỡ ren.",
      "Nếu cần hồ sơ nghiệm thu, nên nêu trước yêu cầu VAT, CO/CQ hoặc chứng từ theo lô hàng."
    ],
    links: [
      ["series/gac-series/", "GAC Series"],
      ["series/gafr-series/", "GAFR Series"],
      ["series/gaf-series/", "GAF Series"],
      ["series/gar-series/", "GAR Series"],
      ["series/gal-series/", "GAL Series"],
      ["blog/bo-loc-dieu-ap-frl-airtac-gac-gafr-gar-gal/", "Bài chọn FRL AirTAC"]
    ]
  },
  actuator: {
    slugs: ["nacq-series", "npb-series", "nfpa-cylinder-nsu-series", "tr-series", "tcl-tcm-series", "hfc-series", "hfcq-series", "hrq-series", "hrs-series", "rms-series", "rmt-series", "rmtl-series", "rmh-series"],
    tone: "t-actuator",
    kicker: "Series trọng điểm",
    heading: "Xi lanh và cơ cấu chấp hành AirTAC cho máy tự động",
    lead: "Nhóm xi lanh/cơ cấu chấp hành cần chọn theo bore, stroke, kiểu gá, cảm biến, tải và không gian lắp. Khi thay thế hàng cũ, ảnh tem, ảnh chân gá và kích thước lỗ bắt vít giúp giảm rủi ro sai mã.",
    points: [
      "Compact cylinder, guided cylinder, gripper và rotary table có tiêu chí chọn khác nhau; nên gửi rõ ứng dụng.",
      "Bore/stroke quyết định lực và hành trình, còn kiểu gá/cảm biến quyết định khả năng thay thế trực tiếp.",
      "Với gripper hoặc rotary table, cần nêu tải, moment, góc xoay hoặc kiểu kẹp nếu có."
    ],
    links: [
      ["series/nacq-series/", "NACQ Series"],
      ["series/npb-series/", "NPB Series"],
      ["series/tr-series/", "TR Series"],
      ["series/hfc-series/", "HFC Series"],
      ["series/hrq-series/", "HRQ Series"],
      ["blog/xi-lanh-khi-nen-airtac-cach-chon/", "Bài chọn xi lanh AirTAC"]
    ]
  },
  guide: {
    slugs: ["lsh-series", "lsd-series", "lrm-series", "lgc-series", "lrw-series"],
    tone: "t-guide",
    kicker: "Series trọng điểm",
    heading: "Linear guide AirTAC cho cơ cấu trượt chính xác",
    lead: "LSH, LSD, LRM, LGC và LRW cần đối chiếu chiều dài ray, loại block, tải/moment, preload, cấp chính xác và điều kiện bôi trơn. Đây là nhóm nên kiểm datasheet trước khi chốt mã vì kích thước lắp ảnh hưởng trực tiếp đến cơ cấu.",
    points: [
      "LSH thường dùng cho dẫn hướng tiêu chuẩn; LRM/LRW phù hợp cấu hình nhỏ gọn hoặc widened.",
      "Khi thay thế, cần đo chiều cao block, khoảng cách lỗ bắt vít, chiều dài ray và kiểu block.",
      "Nếu môi trường bụi hoặc tải lệch tâm, nên nêu rõ để kiểm tra tải moment và phương án bôi trơn."
    ],
    links: [
      ["series/lsh-series/", "LSH Series"],
      ["series/lsd-series/", "LSD Series"],
      ["series/lrm-series/", "LRM Series"],
      ["series/lgc-series/", "LGC Series"],
      ["series/lrw-series/", "LRW Series"],
      ["huong-dan/chon-linear-guide-airtac/", "Guide chọn linear guide"]
    ]
  }
};

function esc(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function removePriorityBlocks(html) {
  return html.replace(/<section\b(?=[^>]*data-fg-airtac-priority)[\s\S]*?<\/section>/g, "");
}

function prefixForSeries() {
  return "../../";
}

function linkGrid(family, currentSlug) {
  const prefix = prefixForSeries();
  const links = family.links
    .filter(([url]) => url !== `series/${currentSlug}/`)
    .slice(0, 5)
    .map(([url, label]) => `<a href="${esc(prefix + url)}"><span>Đối chiếu</span><strong>${esc(label)}</strong><small>Mở để so mã, datasheet và lựa chọn thay thế.</small></a>`)
    .join("");
  return `<div class="airtac-priority-links">${links}<a href="${prefix}lien-he/"><span>RFQ</span><strong>Gửi yêu cầu báo giá AirTAC</strong><small>Gửi mã hàng, số lượng, chứng từ và ảnh tem nếu có.</small></a></div>`;
}

function block(family, currentSlug) {
  return `<section class="section section-soft airtac-priority ${family.tone}" ${MARK}="series"><div class="container split"><div><div class="section-heading"><div class="kicker">${esc(family.kicker)}</div><h2>${esc(family.heading)}</h2><p>${esc(family.lead)}</p></div><ul class="check-list">${family.points.map((point) => `<li>${esc(point)}</li>`).join("")}</ul></div><div class="tech-panel"><h3>Trang nên đối chiếu</h3>${linkGrid(family, currentSlug)}</div></div></section>`;
}

function insertBeforeOptimizer(html, addition) {
  const optimizerIndex = html.indexOf("<section", html.indexOf("data-fg-airtac-optimizer"));
  if (optimizerIndex >= 0) return html.slice(0, optimizerIndex) + addition + html.slice(optimizerIndex);
  return html.replace("</main>", `${addition}</main>`);
}

function appendCss() {
  const css = fs.readFileSync(CSS, "utf8");
  if (css.includes("AirTAC priority series enrichment")) return false;
  const extra = `

/* AirTAC priority series enrichment */
.airtac-priority .section-heading p{max-width:760px}
.airtac-priority-links{display:grid;grid-template-columns:1fr;gap:1px;margin-bottom:16px}
.airtac-priority-links a{display:block;padding:14px 16px;background:#fff;border:1px solid var(--line);transition:border-color .18s ease,box-shadow .18s ease}
.airtac-priority-links a:hover{border-color:var(--tone,var(--blue));box-shadow:0 10px 24px rgba(39,50,55,.08)}
.airtac-priority-links span{display:block;margin-bottom:6px;color:var(--muted);font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.airtac-priority-links strong{display:block;color:var(--ink);line-height:1.32}
.airtac-priority-links small{display:block;margin-top:6px;color:var(--muted);font-size:.88rem;line-height:1.42}
`;
  fs.writeFileSync(CSS, css + extra, "utf8");
  return true;
}

function main() {
  let changed = 0;
  const touched = [];
  for (const family of Object.values(families)) {
    for (const slug of family.slugs) {
      const file = path.join(SITE, "series", slug, "index.html");
      if (!fs.existsSync(file)) continue;
      const html = fs.readFileSync(file, "utf8");
      const cleaned = removePriorityBlocks(html);
      const next = insertBeforeOptimizer(cleaned, block(family, slug));
      if (next !== html) {
        fs.writeFileSync(file, next, "utf8");
        changed += 1;
        touched.push(`series/${slug}/`);
      }
    }
  }
  const cssChanged = appendCss();
  console.log(JSON.stringify({ changedHtmlFiles: changed, cssChanged, touched }, null, 2));
}

main();
