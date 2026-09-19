#!/usr/bin/env python3
"""Gera as composições HyperFrames (src/XX.html) a partir dos estáticos em ../pecas.

Cada peça vira uma composição standalone 1080x1350 de 8 s, com a mesma marcação
e CSS do estático (fontes locais em assets/fonts, imagens em assets/img), uma
timeline GSAP pausada registrada em window.__timelines e as faixas de áudio
(trilha em assets/audio/bed.mp3 e SFX em assets/sfx).
"""
import json, os, re, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..', '..'))
DUR = 8.0
BED_VOL = 0.45
SFX_DUR = {'pop': 0.72, 'whoosh-short': 0.58, 'whoosh': 0.58, 'sparkle': 1.81, 'chime': 2.5, 'ping': 1.32}

feed = open(os.path.join(RAIZ, 'design-system', 'feed.css'), encoding='utf-8').read()
feed = feed.replace('url(../assets/fonts/', 'url(assets/fonts/')

# ---- coreografia por peça: JS (t em segundos) e cues de SFX (arquivo, t, volume) ----
PECAS = {
 '01': dict(
  js='''
KJ.intro(tl);
KJ.slide(tl,'.frango',0.95,-90,0.9);
KJ.rise(tl,'#produto',1.05,140,1.0);
KJ.pop(tl,S(0),1.75); KJ.pop(tl,S(1),2.05,true);
KJ.fade(tl,'.leg',2.35,0.5);
KJ.up(tl,'.faixa > *',2.7,26,0.55,0.12);
KJ.fade(tl,'.nota',3.2);
KJ.float(tl,'#produto',2.1,8); KJ.float(tl,'.frango',2.0,5);
''',
  sfx=[('whoosh-short',0.30,.25),('whoosh',1.05,.22),('pop',1.75,.28),('pop',2.05,.34),('sparkle',2.25,.12),('pop',2.70,.16),('pop',2.82,.16)]),
 '02': dict(
  js='''
KJ.intro(tl);
KJ.up(tl,'.col',1.0,120,0.9,0.15);
KJ.pop(tl,S(0),1.7); KJ.pop(tl,S(1),1.9); KJ.pop(tl,S(2),2.1); KJ.pop(tl,S(3),2.4,true);
KJ.fade(tl,'.nome',2.3,0.5);
KJ.pop(tl,S(4),2.85); KJ.pop(tl,S(5),3.0);
KJ.slide(tl,'.cta',3.2,-24,0.6);
KJ.fade(tl,'.nota',3.5);
KJ.float(tl,'#produto',2.0,8);
''',
  sfx=[('whoosh-short',0.30,.25),('whoosh',1.0,.2),('pop',1.7,.24),('pop',1.9,.24),('pop',2.1,.24),('pop',2.4,.34),('sparkle',2.60,.12),('pop',2.85,.18),('pop',3.0,.18)]),
 '03': dict(
  css_del=['transform:translateX(-50%);'],
  js='''
KJ.intro(tl,{kickerCentered:true});
KJ.rise(tl,'#produto',1.1,160,1.0,{xPercent:-50});
KJ.pop(tl,S(0),1.9,true); KJ.pop(tl,S(1),2.15); KJ.pop(tl,S(2),2.4);
KJ.up(tl,'.apoio > *',2.8,20,0.6,0.15);
KJ.float(tl,'#produto',2.1,8,{xPercent:-50});
''',
  sfx=[('whoosh-short',0.30,.25),('whoosh',1.1,.22),('pop',1.9,.34),('sparkle',2.10,.12),('pop',2.15,.24),('pop',2.4,.24)]),
 '04': dict(
  js='''
KJ.intro(tl);
tl.fromTo('.copo',{opacity:0,y:40,scale:.96,transformOrigin:'50% 0%'},{opacity:1,y:0,scale:1,duration:.8,ease:'power3.out'},0.9);
KJ.slide(tl,'.lista li',1.4,-28,0.55,0.12);
KJ.slide(tl,'#produto',1.2,120,0.9);
KJ.pop(tl,S(0),2.8,true);
KJ.fade(tl,'.leg',3.05,0.5);
KJ.float(tl,'#produto',2.2,8);
''',
  sfx=[('whoosh-short',0.30,.25),('whoosh',1.2,.2),('pop',2.8,.34),('sparkle',3.00,.12)]),
 '05': dict(
  js='''
KJ.intro(tl);
KJ.rise(tl,'#produto',1.0,140,1.0);
KJ.pop(tl,S(0),1.8,true);
KJ.slide(tl,'.passo',2.1,-30,0.6,0.3);
KJ.up(tl,'.faixa > *',3.1,26,0.55,0.12);
KJ.float(tl,'#produto',2.0,8);
''',
  sfx=[('whoosh-short',0.30,.25),('whoosh',1.0,.22),('pop',1.8,.34),('sparkle',2.00,.12),('pop',2.1,.14),('pop',2.4,.14),('pop',2.7,.14),('pop',3.1,.16),('pop',3.22,.16)]),
 '06': dict(
  js='''
KJ.intro(tl);
tl.fromTo('.num',{opacity:0,scale:.5,transformOrigin:'0% 50%'},{opacity:1,scale:1,duration:.8,ease:'back.out(1.6)'},1.15);
KJ.fade(tl,'.rot',1.7,0.5);
KJ.rise(tl,'#produto',1.3,140,1.0);
KJ.pop(tl,F(0),2.3); KJ.pop(tl,F(1),2.55); KJ.pop(tl,F(2),2.8);
KJ.up(tl,'.faixa .pill',3.0,20,0.5);
KJ.fade(tl,'.nota',3.3);
KJ.float(tl,'#produto',2.3,8);
''',
  sfx=[('whoosh-short',0.30,.25),('pop',1.15,.36),('sparkle',1.35,.14),('whoosh',1.3,.2),('pop',2.3,.22),('pop',2.55,.22),('pop',2.8,.22)]),
 '07': dict(
  css_del=['transform:translateX(-50%);'],
  js='''
KJ.intro(tl);
KJ.rise(tl,'#produto',0.9,140,1.0,{xPercent:-50});
KJ.slide(tl,document.querySelectorAll('.item.esq'),1.6,-30,0.6,0.28);
KJ.slide(tl,document.querySelectorAll('.item.dir'),1.74,30,0.6,0.28);
KJ.pop(tl,F(0),3.0); KJ.pop(tl,F(1),3.2);
KJ.up(tl,'.faixa .pill',3.35,20,0.5,0.12);
KJ.fade(tl,'.nota',3.6);
KJ.float(tl,'#produto',1.9,7,{xPercent:-50});
''',
  sfx=[('whoosh-short',0.30,.25),('whoosh',0.9,.22)]+[('pop',round(1.6+0.14*i,2),.11) for i in range(8)]+[('pop',3.0,.22),('pop',3.2,.22)]),
 '08': dict(
  css_del=['transform:translateX(-50%);','transform:translate(-50%,-50%);'],
  js='''
KJ.intro(tl);
KJ.slide(tl,'.painel.esq',0.9,-60,0.8); KJ.slide(tl,'.painel.dir',1.0,60,0.8);
KJ.slide(tl,'.painel.esq .lin, .painel.esq .ou',1.4,-20,0.5,0.12);
KJ.rise(tl,'#produto',1.5,120,0.9,{xPercent:-50});
tl.fromTo('.OU',{opacity:0,scale:0,xPercent:-50,yPercent:-50},{opacity:1,scale:1,xPercent:-50,yPercent:-50,duration:.6,ease:'back.out(2)'},2.0);
KJ.pop(tl,'.painel.dir .selo',2.5,true);
KJ.up(tl,'.um',2.7,16,0.5);
KJ.fade(tl,'.nota',3.1);
KJ.float(tl,'#produto',2.4,7,{xPercent:-50});
''',
  sfx=[('whoosh-short',0.30,.25),('whoosh',1.0,.2),('pop',2.0,.26),('pop',2.5,.34),('sparkle',2.70,.12)]),
}

def gera(n):
    spec = PECAS[n]
    src = open(os.path.join(AQUI, '..', 'pecas', n + '.html'), encoding='utf-8').read()
    css = src[src.index('<style>') + 7:src.index('</style>')]
    for d in spec.get('css_del', []):
        assert d in css, (n, d)
        css = css.replace(d, '')
    corpo = src[src.index('<body>') + 6:src.index('</body>')]
    corpo = corpo.replace('../img/', 'assets/img/')
    # id no produto (qualquer imagem de cup) e clip raiz
    corpo, k = re.subn(r'<img([^>]*?) src="assets/img/cup_', r'<img id="produto"\1 src="assets/img/cup_', corpo, count=1)
    assert k == 1, n
    corpo = corpo.replace('<div class="peca', '<div id="peca" class="peca', 1)
    audios = ['<audio id="bgm" src="assets/audio/bed.mp3" data-start="0" data-duration="%g" data-track-index="1" data-automation=\'%s\'></audio>' % (
        DUR, json.dumps({"version": 1, "lanes": [{"target": "volume", "points": [
            {"t": 0, "v": 0}, {"t": 0.4, "v": BED_VOL}, {"t": DUR - 0.9, "v": BED_VOL}, {"t": DUR, "v": 0}]}]}))]
    for i, (arq, t, vol) in enumerate(spec['sfx']):
        audios.append('<audio id="sfx%d" src="assets/sfx/%s.mp3" data-start="%g" data-duration="%g" data-volume="%g" data-track-index="%d"></audio>' % (i + 1, arq, t, SFX_DUR[arq], vol, i + 2))
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=1080, height=1350">
<title>Konjac Massa CUP Proteico {n}</title>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script src="assets/anim.js"></script>
<style>
{feed}
#root{{width:100%;height:100%;position:relative;overflow:hidden}}
.peca{{position:absolute;left:0;top:0}}
.titulo .w{{display:inline-block}}
{css}
</style>
</head>
<body>
<div id="root" data-composition-id="cup{n}" data-start="0" data-duration="{DUR:g}" data-width="1080" data-height="1350">
{corpo}
{chr(10).join(audios)}
</div>
<script>
(function () {{
  var tl = gsap.timeline({{ paused: true }});
  var S = function (i) {{ return document.querySelectorAll('.peca > .selo')[i]; }};
  var F = function (i) {{ return document.querySelectorAll('.faixa .selo')[i]; }};
  window.KJ_END = {DUR:g};
{spec['js'].strip()}
  window.__timelines["cup{n}"] = tl;
  tl.seek(0);
}})();
</script>
</body>
</html>
'''
    os.makedirs(os.path.join(AQUI, 'src'), exist_ok=True)
    open(os.path.join(AQUI, 'src', n + '.html'), 'w', encoding='utf-8').write(html)
    return html

if __name__ == '__main__':
    alvos = sys.argv[1:] or sorted(PECAS)
    for n in alvos:
        gera(n)
        print('src/%s.html' % n)
