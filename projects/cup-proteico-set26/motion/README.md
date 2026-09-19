# Motion das 8 peças do CUP Proteico

Projeto HyperFrames. `build.py` gera `src/01..08.html` a partir de `../pecas/*.html` (mesmo CSS do estático, fontes locais, imagens em `assets/img`, trilha em `assets/audio/bed.mp3`, SFX em `assets/sfx`) com a coreografia GSAP e os cues de som declarados por peça no próprio script. `finaliza.sh` leva o render a -14 LUFS com limiter. Passo a passo no `../BRIEFING.md`, seção "Motion"; padrão de coreografia e som na seção 11 do `assets/brand/BRAND.md`.

Trilha: ElevenLabs `sound-generation`, 22 s, `loop: true`, prompt "Soft warm upbeat background music bed for a healthy food brand social video: marimba, plucked acoustic guitar, light shaker and finger snaps, gentle bass, bright and friendly, minimal, no vocals, 100 bpm, seamless loop", `prompt_influence` 0,4. Medida: -13,8 LUFS, 99 bpm, variação de energia baixa (cv 0,18), emenda de loop limpa.
