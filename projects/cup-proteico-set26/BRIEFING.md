# CUP Proteico · 8 posts de feed, estático e motion (set/2026)

Framework de motion: **HyperFrames** (`motion/`, ver seção "Motion" abaixo). Estáticos: peças em HTML. Render: HTML + `design-system/feed.css` → PNG 1080x1350 com `scripts/render_peca.mjs` (Chrome headless; `npm i puppeteer-core` uma vez).

```bash
for n in 01 02 03 04 05 06 07 08; do node scripts/render_peca.mjs projects/cup-proteico-set26/pecas/$n.html projects/cup-proteico-set26/out/$n.png; done
```

## Origem

Briefing "Letícia - Konjac CUP 17/09" (Google Doc `1kJIZRggGVRdrI1TKvQXfmDU1uU2IHuBAhKBYHZVwE84`), 8 posts estáticos do Konjac Massa® CUP Proteico. Referências entregues antes (5 peças) foram avaliadas contra o briefing oficial e o design system e refeitas do zero. As imagens embutidas no Doc não são legíveis pela leitura de Drive: as peças 04, 05 e 08 foram propostas só a partir do texto e da marca.

## O que foi decidido como referência da marca (detalhe na seção 11 do `assets/brand/BRAND.md`)

- Nome nas peças: **Konjac Massa® CUP Proteico** (briefing oficial e cópia do site). "High-Protein" fica visível na foto do copo.
- Claims só da tabela nutricional publicada no site (porção 62 g, sabor frango): 32 g de proteína vegetal, 64% do VD de proteína, 6,7 g de fibras (27% VD), pronto em 3 minutos, sem óleo adicionado, produto vegano.
- Cortados: "baixo em calorias" (227 kcal), "baixo carbo" (21 g de carboidratos e promessa da linha Low Carb), "55% da proteína do dia" (estimativa; o rótulo diz 64%), "único macarrão do Brasil", comparação depreciativa com whey, "sem glúten" (contém glúten).
- Fotos do produto: recortes oficiais da galeria do site (`img/cup_<sabor>.png`), texto de embalagem legível. A imagem "destaque" do site tem texto corrompido por upscale de IA e não pode ser usada.
- Alimentos genéricos (ovo, pasta de amendoim, frango) gerados por IA em fundo transparente, prompts no `img/README.md`.
- Selo de dado nutricional é o componente central, no padrão que a marca já usa no Instagram.

## Peça a peça

| # | Título | Fundo | Copo | Nota |
|---|---|---|---|---|
| 01 | Mais proteína que 100 g de frango. | claro | frango | comparação 31 g x 32 g explícita |
| 02 | O campeão da proteína. | claro | cogumelo | escada crescente; 6,7 g e 3 min na base do copo |
| 03 | Não é shake. Não é barrinha. É refeição. | roxo | vegetais | sem CTA de rodapé, nome no topo |
| 04 | Tudo isso dentro de um copo. | claro | carne | v2: copo menos afunilado, lista contida, sem peso |
| 05 | Só precisa de água quente. | claro | frango | proposta; o briefing só tinha imagens |
| 06 | Entrega 64% do valor diário de proteína. | roxo | frango | 64% no lugar de 55%; v2: nota sem "62 g" |
| 07 | Para quem é o CUP Proteico? | claro | cogumelo | 8 perfis saindo do copo; caneta com asterisco |
| 08 | Quanto você precisa comer para chegar a 32 g? | claro | vegetais | v2: selo fora do rótulo, legenda sem "69 g" |

## Versão 2 (19/set/2026, retorno do cliente)

- Tirar site e @ do Instagram de todas as peças (rodapé removido).
- "62 g" lido como proteína: o peso da porção saiu de 01 (legenda e nota), 04 (legenda), 06 (nota) e 08 (legenda "69 g"). Onde precisava nomear a porção, ficou "1 copo (uma porção)".
- 04 mal diagramada: copo desenhado com afunilamento de 26 px por lado, lista com largura que cabe na base, produto e legenda sem colisão.
- 08: o selo "32 g" cobria o rótulo do copo; foi para a borda superior do painel roxo.
- Auditoria das 8 em tamanho real depois das mudanças (nota da 01 vazava à direita por `white-space:nowrap`; corrigida).

## Motion

Oito vídeos 1080x1350 de 8 s (30 fps, H.264 + AAC) em `motion/finais/`, um por peça, gerados por `motion/build.py` a partir dos HTML estáticos e renderizados no HyperFrames. Coreografia, som e loudness estão descritos na seção 11 do `assets/brand/BRAND.md` ("Motion do feed"). Regeneração:

```bash
cd projects/cup-proteico-set26/motion
python3 build.py                       # src/01..08.html a partir de ../pecas
for n in 01 02 03 04 05 06 07 08; do cp src/$n.html index.html; npx hyperframes@0.8.50 lint; npx hyperframes@0.8.50 render --quality high --output renders/$n.mp4; bash finaliza.sh renders/$n.mp4 finais/$n.mp4; done
```

Antes de rodar: exportar as variáveis de proxy com `NODE_USE_ENV_PROXY=1` (ver `scripts/setup.sh`), copiar `assets/fonts` da raiz, `../img/*.png` e os SFX do media-use para `motion/assets/` (o `.gitignore` do projeto não versiona esses assets; a trilha `assets/audio/bed.mp3` é versionada porque foi gerada e não se regenera igual).

## Pendências para o cliente antes de publicar

1. **Fechada em 19/set, conferida no site.** "Cup Proteico" é o nome de marketing (menu "CUP PROTEICO 32G PROTEÍNA", página da Linha Proteica, seções da página de produto); "Konjac Massa® Cup High Protein Dry Noodles" é o nome de catálogo (composição de kits, URLs, título de SKU). Arte de feed usa o registro de marketing: as peças ficam com **Konjac Massa® CUP Proteico**. O design system vivo ainda escreve "Cup High Protein" e deveria alinhar com o menu do site.
2. Confirmar a embalagem vigente: as fotos oficiais do site dizem "pronto em 3 minutos"; nas referências antigas aparecia "4 minutos".
3. Corrigir no site a imagem da tabela nutricional do sabor frango: imprime "0,7 g" de fibras onde o %VD prova 6,7 g.
4. Decidir se "caneta emagrecedora" fica na peça 07.
5. Aprovar 64% do VD (rótulo) no lugar de 55% (estimativa) na peça 06.
6. O design system vivo (artifact, 19/set) diverge das peças em quatro pontos registrados na seção 11 do BRAND.md: posição do logo, limite de três badges por arte, fundo na cor do produto para a família Proteica, e o nome "Cup High Protein". Nenhum deles é erro de execução; são escolhas a fechar com quem mantém o sistema.
