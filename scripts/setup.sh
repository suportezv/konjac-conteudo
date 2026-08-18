#!/usr/bin/env bash
# Setup do estúdio de conteúdo (Linux/cloud). Agnóstico de marca: o symlink usa o
# nome da pasta do repo. No Mac, siga SETUP.md manualmente.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS_DIR="${TOOLS_DIR:-/workspace}"
VIDEO_USE="$TOOLS_DIR/browser-use/video-use"
HYPERFRAMES="$TOOLS_DIR/heygen-com/hyperframes"

echo "== 1/5 ffmpeg =="
if ! command -v ffmpeg >/dev/null; then
  # Cloud: proxy bloqueia apt (403); fallback para build estático BtbN via HTTPS.
  if ! (apt-get update -qq && apt-get install -y -qq ffmpeg fonts-liberation); then
    echo "apt bloqueado; baixando build estático BtbN"
    curl -sL -o "$TOOLS_DIR/ffmpeg.tar.xz" \
      "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linux64-gpl.tar.xz"
    tar xf "$TOOLS_DIR/ffmpeg.tar.xz" -C "$TOOLS_DIR" && rm "$TOOLS_DIR/ffmpeg.tar.xz"
    ln -sf "$TOOLS_DIR"/ffmpeg-master-latest-linux64-gpl/bin/ffmpeg /usr/local/bin/ffmpeg
    ln -sf "$TOOLS_DIR"/ffmpeg-master-latest-linux64-gpl/bin/ffprobe /usr/local/bin/ffprobe
  fi
fi
ffmpeg -version | head -1

echo "== 2/5 video-use =="
if [ ! -d "$VIDEO_USE/.git" ]; then
  GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/browser-use/video-use "$VIDEO_USE"
fi
if git -C "$VIDEO_USE" apply --check "$REPO_ROOT/patches/video-use-is-portrait-source.patch" 2>/dev/null; then
  git -C "$VIDEO_USE" apply "$REPO_ROOT/patches/video-use-is-portrait-source.patch"
  echo "patch is_portrait_source aplicado"
elif grep -q 'if f\]' "$VIDEO_USE/helpers/render.py" 2>/dev/null; then
  echo "patch is_portrait_source: já aplicado"
elif (cd "$VIDEO_USE" && patch -p1 --forward < "$REPO_ROOT/patches/video-use-is-portrait-source.patch"); then
  # git apply falha quando o upstream desloca linhas; patch -p1 tolera offset.
  echo "patch is_portrait_source aplicado (via patch -p1, com offset)"
else
  echo "patch is_portrait_source: não aplicável (verifique manualmente)"
fi
(cd "$VIDEO_USE" && uv sync) || (cd "$VIDEO_USE" && pip install -e .)
mkdir -p ~/.claude/skills
ln -sfn "$VIDEO_USE" ~/.claude/skills/video-use

echo "== 3/5 hyperframes + media-use =="
if [ ! -d "$HYPERFRAMES/.git" ]; then
  GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/heygen-com/hyperframes "$HYPERFRAMES"
fi
# No cloud o proxy pode barrar o manifest do GitHub e o comando falhar; os
# symlinks abaixo cobrem o registro, então falha aqui não aborta o setup.
npx --yes hyperframes skills update || echo "hyperframes skills update falhou (proxy/offline); registrando por symlink"
mkdir -p ~/.claude/skills
if [ -d "$HYPERFRAMES/skills" ] && ! ls ~/.claude/skills | grep -q hyperframes; then
  for d in "$HYPERFRAMES"/skills/*/; do
    ln -sfn "$d" ~/.claude/skills/"$(basename "$d")"
  done
  echo "skills do hyperframes registradas por symlink"
fi

echo "== 4/5 Python (PIL para overlays, numpy para batidas) =="
python3 -c 'import PIL' 2>/dev/null || pip3 install pillow
python3 -c 'import numpy' 2>/dev/null || pip3 install numpy

echo "== 5/5 estúdio =="
STUDIO_NAME="$(basename "$REPO_ROOT")"
ln -sfn "$REPO_ROOT" ~/"$STUDIO_NAME"
echo "~/$STUDIO_NAME -> $REPO_ROOT"

if [ ! -f "$VIDEO_USE/.env" ]; then
  echo "PENDENTE: gravar ELEVENLABS_API_KEY em $VIDEO_USE/.env (peça ao usuário; chave sk_ de 51 chars)"
fi
echo "Setup concluído. Rode: bash $REPO_ROOT/scripts/validate.sh"
