const fs = require("node:fs");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..", "..");
const SITE = path.join(ROOT, "airtac-viet-nam");

function files(dir) {
  const out = [];
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) out.push(...files(full));
    else if (item.isFile() && item.name.endsWith(".html")) out.push(full);
  }
  return out;
}

function existsTarget(fromFile, raw) {
  let href = raw.split("#")[0].split("?")[0];
  if (!href || href.startsWith("mailto:") || href.startsWith("tel:") || href.startsWith("javascript:")) return true;
  if (/^https?:\/\//i.test(href)) {
    if (!href.startsWith("https://fastgroup.vn/")) return true;
    href = href.replace("https://fastgroup.vn", "");
  }
  if (href.startsWith("//")) return true;

  let target;
  if (href.startsWith("/")) {
    target = path.join(ROOT, href.slice(1));
  } else {
    target = path.resolve(path.dirname(fromFile), href);
  }

  if (href.endsWith("/") || !path.extname(target)) target = path.join(target, "index.html");
  return fs.existsSync(target);
}

let bad = [];
for (const file of files(SITE)) {
  const html = fs.readFileSync(file, "utf8");
  for (const m of html.matchAll(/\b(?:href|src)="([^"]+)"/g)) {
    if (!existsTarget(file, m[1])) {
      bad.push({ file: path.relative(ROOT, file), link: m[1] });
    }
  }
}

console.log(JSON.stringify({ checkedFiles: files(SITE).length, badLinks: bad.length, examples: bad.slice(0, 20) }, null, 2));
process.exitCode = bad.length ? 1 : 0;
