# Assets desta pasta (não versionados: `.gitignore` barra mídia em projects/)

- `cup_<sabor>.png`: recorte oficial da galeria do site, `https://konjacmassamf.com.br/cdn/shop/files/swatch_<sabor>.png`, alpha aparado. Texto de embalagem legível.
- `kitcup_<sabor>.png`: `destaque_<sabor>_transparent.png` do site. **Não usar**: texto da embalagem corrompido por upscale de IA.
- `kit_<sabor>.jpg`: flat-lay oficial `<sabor>-kit.png` (fundo branco).
- `barrinha.png`, `shake.png`: props que o próprio site usa na comparação. `tabela_frango.png`: tabela nutricional oficial.
- `logo.png`: `assets/brand/logotipo-konjac-massa-mf.png`.
- `ovo.png`, `pasta_amendoim.png`, `frango_coluna.png`, `frango_peito.png`: gerados com gpt-image-1, fundo transparente, qualidade medium, prompts em português descrevendo foto de produto realista sem texto (ovo marrom inteiro; duas colheradas de pasta de amendoim empilhadas; cubos de peito de frango grelhado em coluna; peito de frango grelhado fatiado em três).

Para recompor: baixar os swatches do site e regenerar os quatro alimentos com os prompts acima.
