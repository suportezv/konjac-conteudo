#!/usr/bin/env python3
"""Gera as peças estáticas da linha Low Carb (set/2026) em pecas/NN.html a partir do design system."""
import os, re
AQUI=os.path.dirname(os.path.abspath(__file__))
RAIZ=os.path.abspath(os.path.join(AQUI,'..','..'))
SELO=open(os.path.join(RAIZ,'design-system','selo.svg'),encoding='utf-8').read().strip().replace('xmlns="http://www.w3.org/2000/svg"','aria-hidden="true"')
HEAD='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><link rel="stylesheet" href="../../../design-system/feed.css"><style>\n{css}</style></head><body><div class="peca{cls}">\n'
FOOT='</div></body></html>\n'
LOGO='<img class="logo" src="../img/logo.png" alt="">\n'

def selo(inner, cls='', style=''):
    st=f' style="{style}"' if style else ''
    return f'<div class="selo {cls}"{st}>{SELO}{inner}</div>'
S_KCAL = '<div class="n">9<small>kcal</small></div><div class="l">por 100 g</div>'
S_CARBO = '<div class="n" style="font-size:46px">Zero</div><div class="l" style="font-size:20px">carboidratos</div>'
S_FIBRA = '<div class="t">Fonte de<br>fibras</div>'
S_GLUTEN = '<div class="t">Sem<br>glúten</div>'
def faixa4(top=1078, left=48, gap=29, itens=(S_KCAL,S_CARBO,S_FIBRA,S_GLUTEN)):
    return f'<div class="faixa" style="top:{top}px;left:{left}px;gap:{gap}px">' + ''.join(selo(i) for i in itens) + '</div>\n'

def foto(n, img, pos, kicker, titulo, extra_css='', extra_html='', faixa=None):
    css=f'''.k{{position:absolute;left:64px;top:72px}}
.titulo{{position:absolute;left:64px;top:112px;width:800px;font-size:100px}}
.fundo{{object-position:{pos}}}
.faixa{{position:absolute;display:flex;align-items:center}}
{extra_css}'''
    html=HEAD.format(css=css,cls=' foto')
    html+=f'<img class="fundo" src="../img/{img}" alt="">\n<div class="scrim"></div>\n'+LOGO
    html+=f'<div class="kicker k">{kicker}</div>\n<h1 class="display titulo">{titulo}</h1>\n'+extra_html+(faixa or faixa4())+FOOT
    open(os.path.join(AQUI,'pecas',f'{n}.html'),'w',encoding='utf-8').write(html)

# ---------- 01: linha, recortes oficiais em leque ----------
cortes=[('pappardelle',-14,190,70),('fettuccine',-7,95,26),('espaguete',0,0,0),('penne',7,-95,26),('linguine',14,-190,70)]
ordem=[0,4,1,3,2]  # z: extremos atrás, centro na frente
pouches=''
for idx in ordem:
    nome,rot,dx,dy=cortes[idx]
    pouches+=f'<img class="pouch" src="../img/mockup_{nome}.png" alt="" style="transform:translate({-dx}px,{dy}px) rotate({rot}deg)">\n'
css01='''.k{position:absolute;left:64px;top:72px}
.titulo{position:absolute;left:64px;top:112px;width:900px;font-size:100px}
.leque{position:absolute;left:0;right:0;top:400px;height:600px}
.pouch{position:absolute;left:50%;top:0;width:300px;margin-left:-150px;transform-origin:50% 110%;filter:drop-shadow(0 18px 18px rgba(43,33,48,.22))}
.apoio{position:absolute;left:64px;right:64px;top:986px;text-align:center;font-family:var(--corpo);font-weight:700;font-size:34px;color:var(--tinta)}
.faixa{position:absolute;display:flex;align-items:center}'''
h=HEAD.format(css=css01,cls='')+LOGO
h+='<div class="kicker k">Linha Low Carb Konjac Massa®</div>\n'
h+='<h1 class="display titulo">Massa com <span class="acento">zero carboidratos</span> existe.</h1>\n'
h+='<div class="leque">\n'+pouches+'</div>\n'
h+='<div class="apoio">Escolha seu corte favorito.</div>\n'
h+=f'<div class="faixa" style="top:1078px;left:164px;gap:40px">{selo(S_KCAL)}{selo(S_FIBRA)}{selo(S_GLUTEN)}</div>\n'+FOOT
open(os.path.join(AQUI,'pecas','01.html'),'w',encoding='utf-8').write(h)

# ---------- 02, 03, 04: foto ----------
foto('02','carbonara-5.jpg','50% 62%','Konjac Massa® Low Carb','Macarronada <span class="acento">sem sair da dieta.</span>')
foto('03','pappardelle-3.jpg','50% 58%','Konjac Massa® Low Carb','Quem disse que <span class="acento">macarronada</span> não cabe no emagrecimento?',
     extra_css='.titulo{font-size:88px;width:840px}')
foto('04','fettuccine-6.jpg','50% 60%','Konjac Massa® Low Carb','Quer macarronada <span class="acento">na dieta?</span>',
     extra_css='.apoio{position:absolute;left:64px;top:372px;width:900px;font-size:34px;line-height:1.2}',
     extra_html='<div class="apoio">A massa da sua dieta é Konjac Massa® Low Carb.</div>\n')
print('pecas 01-04 geradas')
