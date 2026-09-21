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
# Selos no padrao dos prints do cliente (v6): numero grande + rotulo curto, ou duas linhas de texto. Sem tamanho por selo.
S_KCAL = '<div class="n">9</div><div class="l">Kcal</div>'
S_CARBO = '<div class="n">0</div><div class="l">Carb</div>'
S_FIBRA = '<div class="t">Rico em<br>Fibras</div>'  # texto por decisao do cliente (20/set); "rico" exige 6 g/100 g e a linha tem 4 g, risco registrado no BRIEFING
S_GLUTEN = '<div class="t">Sem<br>Glúten</div>'
NOTA100 = '<div class="nota nota100">Valores por 100 g de Konjac Massa® Low Carb.</div>\n'
def faixa4(top=1066, left=48, gap=29, itens=(S_KCAL,S_CARBO,S_FIBRA,S_GLUTEN)):
    return f'<div class="faixa" style="top:{top}px;left:{left}px;gap:{gap}px">' + ''.join(selo(i) for i in itens) + '</div>\n'

def blob(x,y,w,h,cx=35,cy=35,a=.92):
    """Escurecimento local atras do texto: elipse suave, nao cobre a embalagem."""
    return f'.peca.foto .scrim{{inset:auto;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:radial-gradient(ellipse at {cx}% {cy}%,rgba(64,12,60,{a}) 0%,rgba(64,12,60,{a*.8:.2f}) 38%,rgba(64,12,60,0) 72%)}}'
BASE='.base{position:absolute;left:0;right:0;bottom:0;height:420px;background:linear-gradient(180deg,rgba(64,12,60,0) 0%,rgba(64,12,60,.78) 100%)}'
def foto(n, img, pos, titulo, lado='esq', titulo_css='', extra_css='', extra_html='', faixa=None, scrim=None, logo_css=''):
    x = '64px' if lado=='esq' else 'auto'
    css=f'''.titulo{{position:absolute;top:84px;font-size:92px;{'left:64px;width:470px' if lado=='esq' else 'right:64px;left:500px;top:236px'};{titulo_css}}}
.fundo{{object-position:{pos}}}
{scrim or ''}
{BASE}
.faixa{{position:absolute;display:flex;align-items:center}}
.nota100{{position:absolute;left:64px;top:1302px;max-width:900px}}
.logo{{{logo_css}}}
{extra_css}'''
    html=HEAD.format(css=css,cls=' foto')
    html+=f'<img class="fundo" src="../img/{img}" alt="">\n<div class="scrim"></div>\n<div class="base"></div>\n'+LOGO
    html+=f'<h1 class="display titulo">{titulo}</h1>\n'+extra_html+(faixa or faixa4())+NOTA100+FOOT
    open(os.path.join(AQUI,'pecas',f'{n}.html'),'w',encoding='utf-8').write(html)

# ---------- 01: linha, recortes oficiais em leque ----------
cortes=[('pappardelle',-14,190,70),('fettuccine',-7,95,26),('espaguete',0,0,0),('penne',7,-95,26),('linguine',14,-190,70)]
ordem=[0,4,1,3,2]  # z: extremos atrás, centro na frente
pouches=''
for idx in ordem:
    nome,rot,dx,dy=cortes[idx]
    pouches+=f'<img class="pouch" src="../img/mockup_{nome}.png" alt="" style="transform:translate({-dx}px,{dy}px) rotate({rot}deg)">\n'
css01='''.k{position:absolute;left:64px;top:72px}
.titulo{position:absolute;left:64px;top:84px;width:900px;font-size:100px}
.leque{position:absolute;left:0;right:0;top:400px;height:600px}
.pouch{position:absolute;left:50%;top:0;width:300px;margin-left:-150px;transform-origin:50% 110%;filter:drop-shadow(0 18px 18px rgba(43,33,48,.22))}
.apoio{position:absolute;left:64px;right:64px;top:986px;text-align:center;font-family:var(--corpo);font-weight:700;font-size:34px;color:var(--tinta)}
.faixa{position:absolute;display:flex;align-items:center}
.nota100{position:absolute;left:64px;top:1302px;max-width:900px}'''
h=HEAD.format(css=css01,cls='')+LOGO
h+='<h1 class="display titulo">Massa com <span class="acento">zero carboidratos</span> existe.</h1>\n'
h+='<div class="leque">\n'+pouches+'</div>\n'
h+='<div class="apoio">Escolha seu corte favorito.</div>\n'
h+=f'<div class="faixa" style="top:1066px;left:164px;gap:40px">{selo(S_KCAL)}{selo(S_FIBRA)}{selo(S_GLUTEN)}</div>\n'+NOTA100+FOOT
open(os.path.join(AQUI,'pecas','01.html'),'w',encoding='utf-8').write(h)

# ---------- 02, 03, 04: foto, embalagem sempre livre ----------
# 02: embalagem no alto a direita (foto descida ao maximo), titulo a esquerda; logo um pouco menor e mais alto para nao tocar a embalagem
foto('02','carbonara-5.jpg','50% 0%','Macarronada <span class="acento">sem sair da dieta.</span>', lado='esq',
     titulo_css='width:460px', scrim=blob(-160,-120,820,600,45,40), logo_css='width:180px;top:44px')
# 03: embalagem (desfocada) a esquerda, titulo a direita sob o logo
foto('03','pappardelle-5.jpg','50% 0%','Quem disse que <span class="acento">macarronada</span> não cabe no emagrecimento?', lado='dir',
     titulo_css='font-size:76px;left:520px', scrim=blob(380,120,760,560,62,42))
# 04: embalagem a esquerda, titulo e apoio a direita
foto('04','fettuccine-6.jpg','50% 0%','Quer macarronada <span class="acento">na dieta?</span>', lado='dir',
     titulo_css='font-size:88px;top:224px', scrim=blob(360,110,780,560,62,40),
     extra_css='.apoio{position:absolute;left:500px;right:64px;top:484px;font-size:31px;line-height:1.25}',
     extra_html='<div class="apoio">A massa da sua dieta é Konjac Massa® Low Carb.</div>\n')
print('pecas 01-04 geradas')

# ================= CARROSSÉIS =================
CSS_SLIDE_FOTO='''.titulo{position:absolute;left:64px;top:84px;width:860px;font-size:100px}
.faixa{position:absolute;display:flex;align-items:center}
.perfil{position:absolute;left:64px;right:64px;top:120px;display:flex;flex-direction:column;gap:56px}
.perfil .item{display:flex;gap:26px;align-items:flex-start}
.perfil .item i{flex:0 0 14px;width:14px;height:92px;border-radius:7px;background:var(--menta);margin-top:8px}
.perfil .item b{font-family:var(--display);font-weight:800;font-size:92px;line-height:.94;text-transform:uppercase;color:var(--branco);text-shadow:0 3px 16px rgba(0,0,0,.35)}
.passe{position:absolute;right:64px;bottom:64px}
.contador{position:absolute;left:64px;bottom:72px;font-family:var(--corpo);font-weight:700;font-size:22px;letter-spacing:2px;color:rgba(255,255,255,.85)}
.nota{position:absolute;left:64px;right:64px;bottom:64px}
.nota100{position:absolute;left:64px;right:auto;bottom:auto;top:1302px;max-width:900px}
'''
def slide_foto(nome, img, pos, corpo, extra_css='', scrim_full=False, scrim=None, base=False, logo=True):
    css=CSS_SLIDE_FOTO+('.peca.foto .scrim{background:linear-gradient(180deg,rgba(64,12,60,.9) 0%,rgba(64,12,60,.7) 45%,rgba(64,12,60,.45) 100%)}' if scrim_full else '')+(scrim or '')+(BASE if base else '')+extra_css
    html=HEAD.format(css=css,cls=' foto')+f'<img class="fundo" src="../img/{img}" alt="">\n<div class="scrim"></div>\n'+('<div class="base"></div>\n' if base else '')+(LOGO if logo else '')+corpo+FOOT
    open(os.path.join(AQUI,'pecas',f'{nome}.html'),'w',encoding='utf-8').write(html)
def perfis(*itens):
    return '<div class="perfil">'+''.join(f'<div class="item"><i></i><b>{t}</b></div>' for t in itens)+'</div>\n'
K=''  # kicker retirado a pedido do cliente (21/set): o logo ja identifica a marca
def cont(i,n): return f'<div class="contador">{i} / {n}</div>\n'

# ---------- 05: carrossel, 7 slides ----------
slide_foto('05-1','hum-6650.jpg','50% 78%', K+'<h1 class="display titulo">A linha Low Carb da Konjac Massa® é para <span class="acento">você que...</span></h1>\n<div class="pill passe">Passe para o lado</div>\n'+cont(1,7), extra_css='.titulo{font-size:104px}')
slide_foto('05-2','hum-6764.jpg','50% 30%', K+perfis('Está em processo de emagrecimento','Segue low carb ou cetogênica')+cont(2,7), scrim_full=True)
slide_foto('05-3','hum-6612.jpg','50% 35%', K+perfis('Quer controlar as calorias','Busca mais fibras e saciedade')+cont(3,7), scrim_full=True)
slide_foto('05-4','hum-6598.jpg','50% 50%', K+perfis('Tem diabetes*','Tem doença celíaca')+'<div class="nota">*Sob orientação de profissional de saúde.</div>\n'+cont(4,7), scrim_full=True, extra_css='.contador{bottom:112px}')
slide_foto('05-5','pappardelle-5.jpg','50% 55%', K+perfis('É vegano ou vegetariano')+cont(5,7), scrim_full=True)
slide_foto('05-6','MF40.jpg','50% 50%', K+perfis('É atleta','Precisa de praticidade')+cont(6,7), scrim_full=True)
slide_foto('05-7','carbonara-6.jpg','34% 62%', K+'<h1 class="display titulo">Não abre mão de comer uma <span class="acento">massa deliciosa.</span></h1>\n<div class="apoio" style="position:absolute;left:64px;top:470px;font-size:34px">Conheça a linha Low Carb.</div>\n'+faixa4()+NOTA100+cont(7,7), extra_css='.titulo{font-size:84px;width:470px}.contador{bottom:auto;top:1020px}', scrim=blob(-160,-120,820,700,45,40), base=True)

# ---------- 06: carrossel, 3 slides ----------
ICONE_KCAL='<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="44" fill="none" stroke="#fff" stroke-width="3"/><text x="50" y="66" text-anchor="middle" font-family="Barlow Condensed" font-weight="700" font-size="52" fill="#fff">9</text></svg>'
ICONE_FIBRA='<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="44" fill="none" stroke="#fff" stroke-width="3"/><path d="M30 70c0-24 16-40 42-40 0 26-14 40-38 40" fill="none" stroke="#fff" stroke-width="3.5" stroke-linejoin="round"/><path d="M32 70c8-14 18-24 30-32" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg>'
ICONE_GLUTEN='<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="44" fill="none" stroke="#fff" stroke-width="3"/><path d="M50 30v42M50 42c-6-2-10-8-10-14 6 0 10 5 10 14zm0 0c6-2 10-8 10-14-6 0-10 5-10 14zm0 12c-6-2-10-8-10-14 6 0 10 5 10 14zm0 0c6-2 10-8 10-14-6 0-10 5-10 14z" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M28 72L72 28" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/></svg>'
def icone(svg,rotulo): return f'<div class="ic">{svg}<span>{rotulo}</span></div>'
css061='''.fundo{width:115%;height:115%;left:-15%;top:0;object-position:100% 0}
.pouch{position:absolute;left:606px;top:-56px;width:436px;filter:drop-shadow(-14px 22px 22px rgba(30,10,30,.45)) sepia(.18) saturate(1.05) brightness(.97)}
.titulo{position:absolute;left:64px;top:76px;width:560px;font-size:64px;line-height:.98}
.titulo b{font-weight:800;font-size:96px;line-height:.92;display:block}
.titulo i{font-style:normal;color:var(--menta)}
.regra{position:absolute;left:64px;top:404px;width:56px;height:5px;background:var(--menta);border-radius:3px}
.caixa{position:absolute;left:36px;top:432px;padding:20px 30px 22px 28px;border-radius:0 26px 26px 0;background:rgba(58,10,54,.9);font-family:var(--corpo);text-transform:uppercase;letter-spacing:.02em}
.caixa .l1{font-weight:500;font-size:30px;line-height:1.25;color:var(--branco)}
.caixa .l2{font-weight:800;font-size:31px;line-height:1.25;color:var(--menta)}
.icones{position:absolute;left:64px;right:64px;top:1130px;display:flex;align-items:center;justify-content:space-between}
.ic{display:flex;flex-direction:column;align-items:center;gap:10px;flex:1}
.ic svg{width:96px;height:96px}
.ic span{font-family:var(--corpo);font-weight:700;font-size:22px;letter-spacing:.06em;text-transform:uppercase;color:var(--branco);text-shadow:0 2px 8px rgba(0,0,0,.4)}
.sep{width:2px;height:130px;background:rgba(255,255,255,.55)}
.base{height:520px}'''
# 06.1: composicao aprovada pelo cliente na versao do GPT (texto a esquerda com hierarquia interna, caixa de destaque, embalagem em pe a direita, tigela embaixo, icones de linha no rodape).
# Foto espelhada para trazer a tigela para a esquerda; a embalagem espelhada fica coberta pelo mockup oficial (rotulo correto, nunca gerado por IA).
corpo061=('<img class="pouch" src="../img/mockup_linguine.png" alt="">\n'
 '<h1 class="display titulo">Essa macarronada <b>tem <i>zero</i></b><i>carboidratos</i> na <b>massa.</b></h1>\n<div class="regra"></div>\n'
 '<div class="caixa"><div class="l1">Não é truque.</div><div class="l2">É Konjac Massa® Low Carb.</div></div>\n'
 '<div class="icones">'+icone(ICONE_KCAL,'9 kcal')+'<div class="sep"></div>'+icone(ICONE_FIBRA,'Rico em fibras')+'<div class="sep"></div>'+icone(ICONE_GLUTEN,'Sem glúten')+'</div>\n')
slide_foto('06-1','bolognesa-189-2-esp.jpg','100% 0', corpo061, extra_css=css061, scrim='.peca.foto .scrim{background:linear-gradient(180deg,rgba(64,12,60,.88) 0%,rgba(64,12,60,.55) 30%,rgba(64,12,60,0) 52%)}', base=True, logo=False)
S_18='<div class="n">18</div><div class="l">Kcal</div>'
S_8='<div class="n">8g</div><div class="l">Fibra</div>'  # singular como no print da marca ("6,7g fibra"); "Fibras" encosta no filete
slide_foto('06-2','bolognesa-189-1.jpg','50% 40%', K+'<h1 class="display titulo"><span class="acento">200<span style="text-transform:none">g</span></span> de massa</h1>\n<div class="apoio" style="position:absolute;left:64px;top:230px;width:860px;font-size:34px;line-height:1.2">Uma porção generosa de Konjac Massa® Low Carb tem:</div>\n'+faixa4(itens=(S_18,S_CARBO,S_8,S_GLUTEN))+cont(2,3), extra_css='.titulo{font-size:128px}.contador{bottom:auto;top:1020px}', scrim_full=False, scrim='.peca.foto .scrim{background:linear-gradient(180deg,rgba(64,12,60,.9) 0%,rgba(64,12,60,.6) 30%,rgba(64,12,60,0) 50%)}', base=True)
css063='''.k{position:absolute;left:64px;top:72px}
.titulo{position:absolute;left:64px;top:84px;width:900px;font-size:100px;color:var(--branco)}
.apoio{position:absolute;left:64px;top:400px;width:820px;font-family:var(--corpo);font-weight:600;font-size:38px;line-height:1.25;color:var(--branco)}
.leque{position:absolute;left:0;right:0;top:700px;height:520px}
.pouch{position:absolute;left:50%;top:0;width:280px;margin-left:-140px;transform-origin:50% 110%;filter:drop-shadow(0 18px 18px rgba(0,0,0,.35))}
.cta{position:absolute;left:64px;top:1214px}
.contador{position:absolute;right:64px;bottom:72px;font-family:var(--corpo);font-weight:700;font-size:22px;letter-spacing:2px;color:rgba(255,255,255,.85)}'''
h=HEAD.format(css=css063,cls=' roxa')+LOGO
h+='<h1 class="display titulo">Não abra mão de comer uma <span class="acento">massa deliciosa.</span></h1>\n'
h+='<div class="apoio">Escolha uma massa que combina com a sua estratégia.</div>\n<div class="leque">\n'
for nome,rot,dx,dy in [('pappardelle',-12,150,40),('linguine',12,-150,40),('espaguete',0,0,0)]:
    h+=f'<img class="pouch" src="../img/mockup_{nome}.png" alt="" style="transform:translate({-dx}px,{dy}px) rotate({rot}deg)">\n'
h+='</div>\n<div class="pill cta">Conheça a linha Low Carb no site</div>\n<div class="contador">3 / 3</div>\n'+FOOT
open(os.path.join(AQUI,'pecas','06-3.html'),'w',encoding='utf-8').write(h)

# ---------- 07: 2 slides ----------
slide_foto('07-1','MF21.jpg','50% 60%', K+'<h1 class="display titulo">Low carb não precisa ser omelete e salada todo dia.</h1>\n<div class="apoio" style="position:absolute;left:64px;top:520px;width:860px;font-family:var(--display);font-weight:800;font-size:76px;line-height:.96;text-transform:uppercase;color:var(--menta)">Pode ser uma deliciosa lasanha.</div>\n<div class="pill passe">Passe para o lado</div>\n'+cont(1,2), extra_css='.titulo{font-size:92px;width:900px}', scrim='.peca.foto .scrim{background:linear-gradient(180deg,rgba(64,12,60,.9) 0%,rgba(64,12,60,.65) 40%,rgba(64,12,60,0) 62%)}')
slide_foto('07-2','MF45.jpg','50% 45%', K+'<h1 class="display titulo">Mais variedade no cardápio. <span class="acento">Sem sair da sua estratégia.</span></h1>\n'+faixa4(itens=(S_KCAL,S_CARBO,S_FIBRA,S_GLUTEN))+NOTA100+cont(2,2), extra_css='.titulo{font-size:92px;width:900px}.contador{bottom:auto;top:1020px}', scrim_full=False, scrim='.peca.foto .scrim{background:linear-gradient(180deg,rgba(64,12,60,.85) 0%,rgba(64,12,60,.5) 28%,rgba(64,12,60,0) 46%)}', base=True)
print('carrosseis gerados')
