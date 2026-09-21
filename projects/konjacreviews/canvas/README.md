# Konjac Reviews · fonte do Claude Design

Página de prova social da Konjac Massa MF no formato nativo do Claude Design (Design Components): 6 artboards `.dc.html`, layout em `canvas.json` e as 115 capas dos vídeos referenciadas por nome relativo.

| Arquivo | Artboard | Tamanho |
|---|---|---|
| `Main.dc.html` | Hero com a prova social em número | 1200 x 760 |
| `Card.dc.html` | Anatomia do card de review | 940 x 700 |
| `Mobile.dc.html` | Versão mobile | 390 x 1750 |
| `Galeria.dc.html` | Galeria completa com os 115 depoimentos | 1200 x 9400 |
| `Perguntas.dc.html` | Perguntas frequentes e CTA final | 940 x 1180 |
| `EstruturaGEO.dc.html` | Camada de dado estruturado para IA | 1000 x 830 |

Imagens: `p1.webp` a `p115.webp`, capas 9:16 extraídas de cada vídeo. O número do arquivo corresponde ao campo `n` em `../reviews.json`, que liga cada capa ao id do vídeo no Drive, ao review em texto e à transcrição.

- Para importar no Claude Design: use esta pasta como fonte do projeto. Os `.dc.html` são os artboards e o `canvas.json` posiciona e define o launch.
- Conteúdo item a item: `../BRIEFING-CONTEUDO.md`. Estratégia e regras de GEO: `../FRAMEWORK-PAGINA.md`. Dados estruturados: `../reviews.json`.
- Identidade visual: `../../../assets/brand/BRAND.md` (roxo Konjac `#812779`, menta `#a8dcda`, verde `#004c28`, Inter no corpo e condensada bold caps nos títulos).

Os vídeos aparecem como capa estática porque o canvas não carrega mídia externa. Em produção cada card recebe `<video controls preload="none" poster="...">`, conforme a seção 6 do framework.
