// Renderiza um HTML de peça (1080x1350) em PNG com o Chrome headless.
import puppeteer from "/tmp/claude-0/-home-user-konjac-conteudo/03345242-190d-5668-9c5b-3d4d93ea8e2d/scratchpad/fonte/node_modules/puppeteer-core/lib/esm/puppeteer/puppeteer-core.js";
import path from "node:path";
const [,, entrada, saida] = process.argv;
const CH = "/root/.cache/hyperframes/chrome/chrome-headless-shell/linux-152.0.7977.30/chrome-headless-shell-linux64/chrome-headless-shell";
const b = await puppeteer.launch({ executablePath: CH, args: ["--no-sandbox", "--font-render-hinting=none"] });
const p = await b.newPage();
await p.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
await p.goto("file://" + path.resolve(entrada), { waitUntil: "networkidle0" });
await p.evaluate(() => document.fonts.ready);
const fontes = await p.evaluate(() => [...document.fonts].filter(f => f.status === "loaded").map(f => f.family + " " + f.weight));
await p.screenshot({ path: saida, type: "png", clip: { x: 0, y: 0, width: 1080, height: 1350 } });
await b.close();
console.log("ok", saida, "| fontes carregadas:", fontes.length);
