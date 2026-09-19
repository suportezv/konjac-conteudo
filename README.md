# Konjac Conteúdo Studio

Estúdio de edição e agendamento de conteúdo para as redes da **Konjac Massa®** (Instagram `@konjacmassa_mf`). Infraestrutura compartilhada da agência, com o mesmo cinto de ferramentas dos estúdios irmãos; o posicionamento é o desta marca.

- **`assets/brand/`**: a marca. `BRIEFING-OFICIAL.md` (briefing v2 do cliente, prevalece sobre tudo), `BRAND.md` (paleta, claims, narrativa, pilares, cor por corte), logotipo, embalagens e o brand book em artboards.
- **`design-system/`**: cópia dos tokens oficiais e o mapa de onde a paleta é consumida. O sistema completo é um artifact, linkado ali.
- **`FRAMEWORK.md`**: persona, regras, pilares, escolha do framework de motion, assinaturas de edição e fluxo por vídeo.
- **`CLAUDE.md`**: memória persistente do projeto (IDs, contas, allowlist, gotchas).
- **`projects/`**: um subdiretório por vídeo (briefing, transcrição, scripts de edição, caption).
- **`scripts/`**: setup e validação do ambiente, mais o cinto de ferramentas genérico (abaixo).
- **`remotion/`**: composições Remotion (React). A paleta vive só em `src/marca.ts`.
- **`patches/`**: histórico. O patch do video-use foi aposentado pelo upstream; o `validate.sh` testa o comportamento.

## Primeiro uso (cloud)

```bash
bash /home/user/konjac-conteudo/scripts/setup.sh   # caminho absoluto: o campo de setup do environment roda no diretório pai
bash scripts/validate.sh                            # tem que ficar verde
```

Env vars do environment: `ELEVENLABS_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY` e `HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell` (render local do HyperFrames sem baixar Chrome). Allowlist medida e contornos no `CLAUDE.md`.

Depois: coloque o bruto no Drive (pasta pública) ou anexe na conversa, escreva o briefing em `projects/<nome>/` e peça a edição.

## Cinto de ferramentas (`scripts/`)

| Script | O que faz |
|---|---|
| `decupar.py` | Decupa vídeo por âncoras de texto ("de tal frase até tal frase") casadas contra a transcrição com timestamp por palavra; junta trechos, gira, aplica LUT, normaliza áudio |
| `relatorio_decupagem.py` | Retranscreve as peças finais e relata o que ficou e o que caiu |
| `gera_lut_slog2.py` | LUT 3D de S-Log2/S-Gamut para Rec.709 com a `colour-science` |
| `zip_index_remoto.py` | Lista e extrai arquivos de um ZIP gigante no Drive por range request, sem baixar o ZIP |
| `gera_imagem.py` | Gera imagem pela OpenAI ou pelo Gemini, mesma interface, chaves só do ambiente |
| `sobe_para_drive.py` | Sobe arquivos para uma pasta do Drive com token de acesso |

Os scripts não têm referência de marca e leem chaves só de variável de ambiente. Hosts necessários e o estado atual da allowlist estão no `CLAUDE.md`.

| Serviço | Uso | Configuração |
|---|---|---|
| Google Drive | Brutos e material da cliente | Conector oficial + `drive.google.com` e `drive.usercontent.google.com` liberados |
| Metricool | Agendamento | Marca no painel: PENDENTE conectar (blog_id PENDENTE) |
| ElevenLabs | Transcrição, trilha, SFX, TTS | `ELEVENLABS_API_KEY` na env var; o setup grava no `.env` do video-use |
| OpenAI / Gemini | Imagem por script | `OPENAI_API_KEY` e `GEMINI_API_KEY`: PENDENTE cadastrar e liberar os hosts |
| Kairogen | B-roll por IA | Conta da agência; conferir plano e créditos antes de usar |

> Este repositório é **público** de propósito: o agendamento no Metricool depende de servir o render por `raw.githubusercontent.com`. Nunca commitar chaves aqui.
