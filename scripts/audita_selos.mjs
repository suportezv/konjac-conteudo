// Mede cada .selo de uma peça: tamanho, texto dentro do filete interno, fonte Archivo 800, tipo sem variação entre selos e massa do bloco de texto (VAZIO abaixo de 32% do selo).
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
      // Filete interno do selo.svg: r = 38,2% + 3,0% * cos(12 * angulo), crista em 0 grau. Exige 3% do selo de folga entre o canto do texto e o filete.
      const raioFilete = (ang) => (0.382 + 0.030 * Math.cos(12 * ang)) * R.width;
      const folgaMin = (s.classList.contains("v5") ? 0.01 : 0.03) * R.width; // familia v5 (CUP, congelada) foi entregue com folga de 1%
      let pior = 0, lim = 0, folga = Infinity, txt = "";
      s.querySelectorAll(".n,.l,.t,.lbl,.big").forEach((e) => {
        const range = document.createRange(); range.selectNodeContents(e);
        for (const q of range.getClientRects()) {
          for (const [x, y] of [[q.left, q.top], [q.right, q.top], [q.left, q.bottom], [q.right, q.bottom]]) {
            const d = Math.hypot(x - cx, y - cy);
            const r = raioFilete(Math.atan2(y - cy, x - cx));
            if (r - d < folga) { folga = r - d; pior = d; lim = r; }
          }
        }
        txt += " " + e.textContent.trim().replace(/\s+/g, " ");
      });
      lim = lim - folgaMin; // limite reportado ja desconta a folga
      const fams = new Set(); let pesoMin = 999; const tipos = {};
      let top = Infinity, bot = -Infinity;
      s.querySelectorAll(".n,.l,.t,.big").forEach((e) => {
        const cs = getComputedStyle(e); fams.add(cs.fontFamily.split(",")[0].replace(/"/g, "")); pesoMin = Math.min(pesoMin, +cs.fontWeight);
        const cls = [...e.classList].filter((c) => ["n", "l", "t", "big"].includes(c))[0]; tipos[cls] = Math.round(parseFloat(cs.fontSize));
        const q = e.getBoundingClientRect(); top = Math.min(top, q.top); bot = Math.max(bot, q.bottom);
      });
      const massa = Math.round(100 * (bot - top) / R.width); // altura do bloco de texto em % do selo (referencia da marca: 32 a 47%)
      const v5 = s.classList.contains("v5"); // familia congelada do CUP (19/set): nao entra na regra de massa nem de tipo misto
      out.push({ w: Math.round(R.width), pior: Math.round(pior), lim: Math.round(lim), peso: pesoMin, fam: [...fams].join("+"), fill: Math.round(100 * pior / lim), massa, tipos, v5, txt: txt.trim() });
    });
    return out;
  });
  const tam = [...new Set(r.map((x) => x.w))];
  // Um tamanho de tipo por classe na peça inteira: .n, .l, .t e .big não podem variar de selo para selo.
  const porClasse = {};
  for (const x of r) if (!x.v5) for (const [c, v] of Object.entries(x.tipos)) (porClasse[c] ||= new Set()).add(v);
  const misto = Object.entries(porClasse).filter(([, v]) => v.size > 1).map(([c, v]) => `.${c} ${[...v].join("/")}px`);
  const fora = r.filter((x) => x.pior > x.lim || x.peso < 800 || x.fam !== "Archivo" || (!x.v5 && x.massa < 32));
  console.log(`${path.basename(f)}: ${r.length} selos, tamanhos ${JSON.stringify(tam)}${tam.length > 1 ? "  <-- TAMANHOS DIFERENTES" : ""}${misto.length ? "  <-- TIPO MISTO " + misto.join(", ") : ""}`);
  for (const x of r) console.log(`   ${x.pior > x.lim ? "FORA " : (x.peso < 800 || x.fam !== "Archivo") ? "FONTE" : x.v5 ? "v5   " : x.massa < 32 ? "VAZIO" : "ok   "} ${x.w}px  texto ate ${x.pior}px / limite ${x.lim}px (${x.fill}%)  massa ${x.massa}%  ${Object.entries(x.tipos).map(([c, v]) => c + v).join(" ")}  ${x.fam} ${x.peso}  "${x.txt}"`);
  if (tam.length > 1 || fora.length || misto.length) falhas++;
  await p.close();
}
await b.close();
process.exit(falhas ? 1 : 0);
