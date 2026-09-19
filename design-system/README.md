# Design system da Konjac Massa®

O sistema vive em **dois lugares**, e nenhum deles é este diretório:

1. **`assets/brand/`** neste repo: a fonte canônica escrita pelo estúdio. `BRIEFING-OFICIAL.md` (briefing v2 do cliente, prevalece sobre tudo), `BRAND.md` (paleta, claims, narrativa, pilares, cor por corte), o logotipo em PNG e vetor, os renders das embalagens e o brand book em artboards (`canvas/`).
2. **Artifact "Konjac Massa Design System"**: https://claude.ai/artifact/PYtJR5b7YsjzHRBZUAAq9Z, construído a partir de `assets/brand/`. Tem os tokens, os componentes, os specimen cards e os UI kits (loja e social). Artifact irmão, só texto: **Brand Book Konjac Massa MF** (`5RKA3CYnRWLX3K3RxmFqyN`).

Este diretório guarda apenas uma **cópia dos tokens** (`tokens.json`, lida do artifact em 19/set/2026), para que um script ou um render não dependa de rede nem de sessão para saber a paleta.

## Onde a paleta é consumida

| Lugar | O que usa |
|---|---|
| `remotion/src/marca.ts` | tokens do Remotion; as chaves vêm do template da agência, os valores são os oficiais |
| Lettering do ffmpeg | roxo `#812779` por padrão, ou a cor do corte da linha BOX |
| Artifact do design system | fonte dos componentes e dos UI kits |

Se a paleta mudar, atualizar os três. O roxo oficial é `#812779`; o site usa variantes mais violetas, documentadas no `BRAND.md`.

## Regra que não está nos tokens

O logotipo é lettering vetorizado. **Nunca recriar**, sempre usar o arquivo em `assets/brand/`.
