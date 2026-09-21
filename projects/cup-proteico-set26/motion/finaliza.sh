#!/usr/bin/env bash
# Finaliza o render: ganho linear até -14 LUFS integrado + limiter de pico em -1 dBFS, vídeo copiado sem reencode.
# Uso: bash finaliza.sh renders/01.mp4 finais/01.mp4
set -euo pipefail
in="$1"; out="$2"; mkdir -p "$(dirname "$out")"
I=$(ffmpeg -v info -i "$in" -af ebur128 -f null - 2>&1 | grep -A6 Summary | grep " I:" | awk '{print $2}')
g=$(python3 -c "print(round(-14.0 - ($I) + 0.3, 2))")  # +0.3 dB compensa o que o limiter come
ffmpeg -v error -y -i "$in" -c:v copy -af "volume=${g}dB,alimiter=limit=0.85:attack=3:release=60:level=false" -ar 48000 -c:a aac -b:a 192k -movflags +faststart "$out"
res=$(ffmpeg -v info -i "$out" -af ebur128=peak=true -f null - 2>&1 | grep -A9 Summary | grep " I:\|Peak:" | tr -s ' ' | tr '\n' ' ')
echo "$(basename "$out"): entrada I=$I LUFS, ganho ${g} dB -> $res"
