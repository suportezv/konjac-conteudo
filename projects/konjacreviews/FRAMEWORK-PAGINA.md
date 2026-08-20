# Konjac Reviews · framework da página

Página de prova social da **Konjac Massa MF** com dois objetivos simultâneos: converter quem chega com dúvida (sabor, textura, "funciona mesmo?") e ser **citável por IAs generativas** quando alguém pergunta sobre massa de konjac. Este documento é o framework; o conteúdo item a item está em `BRIEFING-CONTEUDO.md`.

## 1. Objetivo e público

- **Objetivo primário**: transformar interesse em compra, usando experiência real de quem já consome. A objeção central do produto não é preço, é **desconfiança sensorial** (sabor, textura, cheiro) e **ceticismo com o claim de 9 calorias**.
- **Objetivo GEO**: virar a fonte que uma IA cita ao responder "massa de konjac funciona?", "qual o sabor da massa konjac?", "konjac serve para diabético?", "como preparar massa de konjac sem cheiro?".
- **Público**: quem está em dieta ou reeducação alimentar, pessoas com diabetes, público low carb e fitness, e quem quer praticidade sem abrir mão de massa.

## 2. Princípio editorial: honestidade acima de tudo

Prova social só funciona enquanto é verdadeira, e uma IA penaliza (ou desmente) página inflada.

1. **Nenhuma avaliação inventada.** Cada texto da página é adaptação fiel do que a pessoa falou no vídeo dela. Nada de depoimento fictício.
2. **Nada de nota em estrelas** enquanto não existir sistema real de coleta de avaliação. Estrela fabricada em dado estruturado é violação de política de rich results e destrói credibilidade.
3. **Sem promessa de emagrecimento pela marca.** Quando a pessoa conta o resultado dela, é experiência individual e a página diz isso de forma clara.
4. **Claims do produto sempre exatos** (9 calorias por 100g, zero carboidratos, 8g de fibras, 100% vegano, selo ANAD, pronta em 2 minutos).
5. **Sem travessão em qualquer texto público.**

## 3. Arquitetura da página

```
HERO  (prova social em número + tese)
  |
BARRA DE CONTEXTO  (o que estes vídeos respondem)
  |
GALERIA  (N cards: vídeo vertical + review em texto abaixo)
  |
PERGUNTAS FREQUENTES  (respostas curtas, extraídas do que os vídeos dizem)
  |
CTA FINAL  (escolha sua linha / compre pelo link)
```

### Hero

- Título que entrega o volume de prova, não adjetivo. O número de vídeos reais é o argumento.
- Subtítulo com a tese: gente de verdade cozinhando, comendo e dando opinião, sem roteiro publicitário.
- Três indicadores de contexto (quantidade de vídeos, horas de depoimento, temas cobertos). Números reais, apurados dos arquivos.
- CTA primário para a loja e âncora para a galeria.

### Card da galeria (anatomia)

Cada card tem, nesta ordem:

1. **Vídeo vertical 9:16** com capa (poster) e play. Não autoplay, não som automático.
2. **Título do review**: uma frase que resume a opinião, escrita como manchete de avaliação.
3. **Corpo do review**: 2 a 4 frases em primeira pessoa, adaptadas do que a pessoa fala no vídeo.
4. **Etiquetas de tema**: até 3 (ex.: textura, preparo, diabetes, saciedade, receita).
5. **Duração do vídeo** e **corte ou linha citada**, quando a pessoa menciona.

### Perguntas frequentes

Bloco em texto puro, com pergunta como `<h3>` e resposta em 2 a 3 frases. As respostas nascem do que os depoimentos repetem, não de invenção.

## 4. Regras de GEO (para a página ser consumida corretamente por IAs)

Modelos de linguagem leem o HTML, não o vídeo. Por isso o texto abaixo de cada vídeo não é acessório, é o produto da página.

1. **Todo vídeo tem equivalente textual completo.** Nenhum card existe só com mídia.
2. **Hierarquia semântica real**: um `<h1>`, `<h2>` por seção, `<h3>` por review e por pergunta. Cada review dentro de `<article>`.
3. **Dado estruturado JSON-LD**, sem inventar métrica:
   - `ItemList` com todos os reviews, na ordem da página.
   - `VideoObject` por vídeo (`name`, `description`, `thumbnailUrl`, `uploadDate`, `duration` em ISO 8601, `contentUrl` ou `embedUrl`, `transcript`).
   - `Review` por depoimento, com `itemReviewed` apontando para o `Product` Konjac Massa MF e `reviewBody` igual ao texto visível. **Sem `reviewRating` e sem `aggregateRating`** enquanto não houver nota real coletada.
   - `FAQPage` para o bloco de perguntas.
   - `Organization` e `Product` uma vez, com os claims oficiais.
4. **Texto extraível**: nada de conteúdo essencial só em imagem, vídeo ou canvas. Legenda queimada no vídeo não conta como texto.
5. **Resposta antes de rodeio**: cada bloco começa pela conclusão, no formato que uma IA cita. Parágrafos curtos, uma ideia por parágrafo.
6. **Entidades explícitas e repetidas com naturalidade**: Konjac Massa MF, massa de konjac, shirataki, fibra solúvel de konjac (glucomanano), os cortes da linha BOX.
7. **Transcrição disponível**: cada card oferece "ver transcrição" com o texto integral do que a pessoa fala, em elemento colapsável que existe no HTML desde o carregamento.
8. **Metadados**: `<title>` e `meta description` orientados à pergunta real do usuário, `canonical`, Open Graph e `lang="pt-BR"`.
9. **Datas honestas**: `datePublished` só quando a data real for conhecida.
10. **Performance**: vídeo com `preload="none"` e poster leve, para a página abrir rápido em celular.

## 5. Identidade visual

Segue o design system em `assets/brand/BRAND.md`: roxo Konjac `#812779` como acento, menta `#a8dcda` de apoio, verde `#004c28` para selos e sinal de confirmação, fundo claro quente. Tipografia condensada bold caps nos títulos e Inter no corpo, para casar com o site. Cards com foto e vídeo em destaque, texto com respiro e largura de leitura confortável.

## 6. Como o vídeo entra na página em produção

O canvas do Claude Design é mockup e não carrega mídia externa, então lá os vídeos aparecem como capa estática. Na implementação real, cada card recebe:

```html
<video controls preload="none" poster="/posters/<id>.webp" playsinline>
  <source src="/videos/<id>.mp4" type="video/mp4">
</video>
```

Recomendação: hospedar os arquivos no próprio domínio ou em CDN, não em link do Drive. Drive não entrega `contentUrl` estável para dado estruturado, atrapalha a indexação e limita o controle de performance.

## 7. Pendências do cliente

- Autorização de uso de imagem de cada criador para a página, e definição de crédito (nome ou @) por vídeo. Enquanto não houver, os reviews entram sem identificação nominal.
- Sistema real de coleta de nota, se a marca quiser exibir avaliação em estrelas no futuro.
- URL final da página (sugestão: `konjacmassamf.com.br/reviews`).
