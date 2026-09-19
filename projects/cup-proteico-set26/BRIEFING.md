# CUP Proteico · 8 posts estáticos de feed (set/2026)

Framework de motion: nenhum, peças estáticas. Render: HTML + `design-system/feed.css` → PNG 1080x1350 com `scripts/render_peca.mjs` (Chrome headless; `npm i puppeteer-core` uma vez).

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
| 04 | Tudo isso dentro de um copo. | claro | carne | proposta sem ver a referência do Doc |
| 05 | Só precisa de água quente. | claro | frango | proposta; o briefing só tinha imagens |
| 06 | Entrega 64% do valor diário de proteína. | roxo | frango | 64% no lugar de 55%, nota do rótulo |
| 07 | Para quem é o CUP Proteico? | claro | cogumelo | 8 perfis saindo do copo; caneta com asterisco |
| 08 | Quanto você precisa comer para chegar a 32 g? | claro | vegetais (69 g) | números derivados da peça 02 do briefing |

## Pendências para o cliente antes de publicar

1. **Fechada em 19/set, conferida no site.** "Cup Proteico" é o nome de marketing (menu "CUP PROTEICO 32G PROTEÍNA", página da Linha Proteica, seções da página de produto); "Konjac Massa® Cup High Protein Dry Noodles" é o nome de catálogo (composição de kits, URLs, título de SKU). Arte de feed usa o registro de marketing: as peças ficam com **Konjac Massa® CUP Proteico**. O design system vivo ainda escreve "Cup High Protein" e deveria alinhar com o menu do site.
2. Confirmar a embalagem vigente: as fotos oficiais do site dizem "pronto em 3 minutos"; nas referências antigas aparecia "4 minutos".
3. Corrigir no site a imagem da tabela nutricional do sabor frango: imprime "0,7 g" de fibras onde o %VD prova 6,7 g.
4. Decidir se "caneta emagrecedora" fica na peça 07.
5. Aprovar 64% do VD (rótulo) no lugar de 55% (estimativa) na peça 06.
6. O design system vivo (artifact, 19/set) diverge das peças em quatro pontos registrados na seção 11 do BRAND.md: posição do logo, limite de três badges por arte, fundo na cor do produto para a família Proteica, e o nome "Cup High Protein". Nenhum deles é erro de execução; são escolhas a fechar com quem mantém o sistema.
