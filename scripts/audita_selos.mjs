// Mede cada .selo de uma peça: tamanho e se todo texto cabe dentro do filete interno.
// Uso: node scripts/audita_selos.mjs projects/<proj>/pecas/01.html [...]
import puppeteer from "/tmp/claude-0/-home-user-konjac-conteudo/03345242-190d-5668-9c5b-3d4d93ea8e2d/scratchpad/fonte/node_modules/puppeteer-core/lib/esm/puppeteer/puppeteer-core.js";
import path from "node:path";
const CH = "/root/.cache/hyperframes/chrome/chrome-headless-shell/linux-152.0.7977.30/chrome-headless-shell-linux64/chrome-headless-shell";
const b = await puppeteer.launch({ executablePath: CH, args: ["--no-sandbox", "--font-render-hinting=none"] });
let falhas = 0;
for (const f of process.argv.slice(2)) {
  const p = await b.newPage();
  await p.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
  await p.goto("file://" + path.resolve(f), { waitUntil: "networkidle0" });
  await p.evaluate(() => document.fonts.ready);
  const r = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll(".selo").forEach((s) => {
      const R = s.getBoundingClientRect();
      const cx = R.left + R.width / 2, cy = R.top + R.height / 2;
      const lim = 0.36 * R.width; // raio mínimo do filete interno (38,2% menos a onda)
      let pior = 0, txt = "";
      s.querySelectorAll(".n,.l,.t,.lbl,.big").forEach((e) => {
        const range = document.createRange(); range.selectNodeContents(e);
        for (const q of range.getClientRects()) {
          for (const [x, y] of [[q.left, q.top], [q.right, q.top], [q.left, q.bottom], [q.right, q.bottom]]) {
            const d = Math.hypot(x - cx, y - cy);
            if (d > pior) { pior = d; }
          }
        }
        txt += " " + e.textContent.trim().replace(/\s+/g, " ");
      });
      const peso = getComputedStyle(s.querySelector(".l,.t,.big") || s).fontWeight;
      out.push({ w: Math.round(R.width), pior: Math.round(pior), lim: Math.round(lim), peso, txt: txt.trim() });
    });
    return out;
  });
  const tam = [...new Set(r.map((x) => x.w))];
  const fora = r.filter((x) => x.pior > x.lim);
  console.log(`${path.basename(f)}: ${r.length} selos, tamanhos ${JSON.stringify(tam)}${tam.length > 1 ? "  <-- TAMANHOS DIFERENTES" : ""}`);
  for (const x of r) console.log(`   ${x.pior > x.lim ? "FORA " : "ok   "} ${x.w}px  texto ate ${x.pior}px / limite ${x.lim}px  peso ${x.peso}  "${x.txt}"`);
  if (tam.length > 1 || fora.length) falhas++;
  await p.close();
}
await b.close();
process.exit(falhas ? 1 : 0);
