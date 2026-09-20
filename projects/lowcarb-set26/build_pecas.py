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

# ================= CARROSSÉIS =================
CSS_SLIDE_FOTO='''.k{position:absolute;left:64px;top:72px}
.titulo{position:absolute;left:64px;top:112px;width:860px;font-size:100px}
.faixa{position:absolute;display:flex;align-items:center}
.perfil{position:absolute;left:64px;right:64px;top:160px;display:flex;flex-direction:column;gap:56px}
.perfil .item{display:flex;gap:26px;align-items:flex-start}
.perfil .item i{flex:0 0 14px;width:14px;height:92px;border-radius:7px;background:var(--menta);margin-top:8px}
.perfil .item b{font-family:var(--display);font-weight:800;font-size:92px;line-height:.94;text-transform:uppercase;color:var(--branco);text-shadow:0 3px 16px rgba(0,0,0,.35)}
.passe{position:absolute;right:64px;bottom:64px}
.contador{position:absolute;left:64px;bottom:72px;font-family:var(--corpo);font-weight:700;font-size:22px;letter-spacing:2px;color:rgba(255,255,255,.85)}
.nota{position:absolute;left:64px;right:64px;bottom:64px}
'''
def slide_foto(nome, img, pos, corpo, extra_css='', scrim_full=False):
    css=CSS_SLIDE_FOTO+('.scrim{background:linear-gradient(180deg,rgba(64,12,60,.9) 0%,rgba(64,12,60,.7) 45%,rgba(64,12,60,.45) 100%)}' if scrim_full else '')+extra_css
    html=HEAD.format(css=css,cls=' foto')+f'<img class="fundo" src="../img/{img}" alt="">\n<div class="scrim"></div>\n'+LOGO+corpo+FOOT
    open(os.path.join(AQUI,'pecas',f'{nome}.html'),'w',encoding='utf-8').write(html)
def perfis(*itens):
    return '<div class="perfil">'+''.join(f'<div class="item"><i></i><b>{t}</b></div>' for t in itens)+'</div>\n'
K='<div class="kicker k">Konjac Massa® Low Carb</div>\n'
def cont(i,n): return f'<div class="contador">{i} / {n}</div>\n'

# ---------- 05: carrossel, 7 slides ----------
slide_foto('05-1','hum-6650.jpg','50% 78%', K+'<h1 class="display titulo">A linha Low Carb da Konjac Massa® é para <span class="acento">você que...</span></h1>\n<div class="pill passe">Passe para o lado</div>\n'+cont(1,7), extra_css='.titulo{font-size:104px}')
slide_foto('05-2','hum-6764.jpg','50% 30%', K+perfis('Está em processo de emagrecimento','Segue low carb ou cetogênica')+cont(2,7), scrim_full=True)
slide_foto('05-3','hum-6612.jpg','50% 35%', K+perfis('Quer controlar as calorias','Busca mais fibras e saciedade')+cont(3,7), scrim_full=True)
slide_foto('05-4','hum-6598.jpg','50% 50%', K+perfis('Tem diabetes*','Tem doença celíaca')+'<div class="nota">*Sob orientação de profissional de saúde.</div>\n'+cont(4,7), scrim_full=True, extra_css='.contador{bottom:112px}')
slide_foto('05-5','pappardelle-5.jpg','50% 55%', K+perfis('É vegano ou vegetariano')+cont(5,7), scrim_full=True)
slide_foto('05-6','MF40.jpg','50% 50%', K+perfis('É atleta','Precisa de praticidade')+cont(6,7), scrim_full=True)
slide_foto('05-7','carbonara-6.jpg','50% 62%', K+'<h1 class="display titulo">Não abre mão de comer uma <span class="acento">massa deliciosa.</span></h1>\n<div class="apoio" style="position:absolute;left:64px;top:490px;font-size:36px">Conheça a linha Low Carb.</div>\n'+faixa4()+cont(7,7), extra_css='.titulo{font-size:96px}.contador{bottom:auto;top:1032px}')

# ---------- 06: carrossel, 3 slides ----------
slide_foto('06-1','bolognesa-189-2.jpg','50% 55%', K+'<h1 class="display titulo">Essa macarronada tem <span class="acento">zero carboidratos</span> na massa.</h1>\n<div class="apoio" style="position:absolute;left:64px;top:486px;width:800px;font-size:36px;line-height:1.2">Não é truque. É Konjac Massa® Low Carb.</div>\n<div class="pill passe">Passe para o lado</div>\n'+cont(1,3), extra_css='.titulo{font-size:96px}')
S_18='<div class="n" style="font-size:46px">18<small>kcal</small></div><div class="l">por 200 g</div>'
S_8='<div class="n">8<small>g</small></div><div class="l">de fibras</div>'
slide_foto('06-2','bolognesa-189-4.jpg','50% 58%', K+'<h1 class="display titulo"><span class="acento">200<span style="text-transform:none">g</span></span> de massa</h1>\n<div class="apoio" style="position:absolute;left:64px;top:262px;width:860px;font-size:34px;line-height:1.2">Uma porção generosa de Konjac Massa® Low Carb tem:</div>\n'+faixa4(itens=(S_18,S_CARBO,S_8,S_GLUTEN))+cont(2,3), extra_css='.titulo{font-size:128px}.contador{bottom:auto;top:1032px}')
css063='''.k{position:absolute;left:64px;top:72px}
.titulo{position:absolute;left:64px;top:112px;width:900px;font-size:100px;color:var(--branco)}
.apoio{position:absolute;left:64px;top:560px;width:820px;font-family:var(--corpo);font-weight:600;font-size:38px;line-height:1.25;color:var(--branco)}
.leque{position:absolute;left:0;right:0;top:700px;height:520px}
.pouch{position:absolute;left:50%;top:0;width:280px;margin-left:-140px;transform-origin:50% 110%;filter:drop-shadow(0 18px 18px rgba(0,0,0,.35))}
.cta{position:absolute;left:64px;top:1214px}
.contador{position:absolute;right:64px;bottom:72px;font-family:var(--corpo);font-weight:700;font-size:22px;letter-spacing:2px;color:rgba(255,255,255,.85)}'''
h=HEAD.format(css=css063,cls=' roxa')+LOGO+'<div class="kicker k">Konjac Massa® Low Carb</div>\n'
h+='<h1 class="display titulo">Não abra mão de comer uma <span class="acento">massa deliciosa.</span></h1>\n'
h+='<div class="apoio">Escolha uma massa que combina com a sua estratégia.</div>\n<div class="leque">\n'
for nome,rot,dx,dy in [('pappardelle',-12,150,40),('linguine',12,-150,40),('espaguete',0,0,0)]:
    h+=f'<img class="pouch" src="../img/mockup_{nome}.png" alt="" style="transform:translate({-dx}px,{dy}px) rotate({rot}deg)">\n'
h+='</div>\n<div class="pill cta">Conheça a linha Low Carb no site</div>\n<div class="contador">3 / 3</div>\n'+FOOT
open(os.path.join(AQUI,'pecas','06-3.html'),'w',encoding='utf-8').write(h)

# ---------- 07: 2 slides ----------
slide_foto('07-1','MF21.jpg','50% 60%', K+'<h1 class="display titulo">Low carb não precisa ser omelete e salada todo dia.</h1>\n<div class="apoio" style="position:absolute;left:64px;top:520px;width:860px;font-family:var(--display);font-weight:800;font-size:76px;line-height:.96;text-transform:uppercase;color:var(--menta)">Pode ser uma deliciosa lasanha.</div>\n<div class="pill passe">Passe para o lado</div>\n'+cont(1,2), extra_css='.titulo{font-size:92px;width:900px}')
slide_foto('07-2','MF45.jpg','50% 45%', K+'<h1 class="display titulo">Mais variedade no cardápio. <span class="acento">Sem sair da sua estratégia.</span></h1>\n'+faixa4(itens=(S_CARBO,S_KCAL,S_FIBRA,S_GLUTEN))+cont(2,2), extra_css='.titulo{font-size:92px;width:900px}.contador{bottom:auto;top:1032px}')
print('carrosseis gerados')
