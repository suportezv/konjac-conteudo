#!/usr/bin/env python3
"""Lista (e opcionalmente baixa) o conteúdo de uma pasta do Drive compartilhada
"qualquer pessoa com o link", sem token e sem o conector.

Por que existe: o conector MCP do Drive só enxerga os filhos de uma pasta quando
a conta conectada tem permissão explícita neles. Pasta do cliente compartilhada
só por link aparece vazia ("{}") no conector, mas a página pública
https://drive.google.com/drive/folders/<id> renderiza a lista completa com
`data-id` e `aria-label` de cada arquivo. Este script lê essa página.

Uso:
    python3 scripts/drive_pasta_publica.py <folder_id>              # lista
    python3 scripts/drive_pasta_publica.py <folder_id> --baixar DIR # baixa imagens
        [--max 1600]  redimensiona para caber em N px (0 = original)
Download direto: https://drive.usercontent.google.com/download?id=<id>&export=download&confirm=t
Se a página vier com "robot.png"/"googlelogo", a pasta não é pública: pedir ao cliente.
"""
import argparse, html, json, os, re, subprocess, sys

def listar(fid):
    h = subprocess.run(['curl','-sL','--max-time','90',f'https://drive.google.com/drive/folders/{fid}'],capture_output=True,text=True).stdout
    if 'robot.png' in h and 'data-id=' not in h:
        return None
    itens, vistos = [], set()
    for m in re.finditer(r'data-id="([A-Za-z0-9_-]{20,})"', h):
        did = m.group(1)
        if did == fid or did in vistos: continue
        al = re.search(r'aria-label="((?:[^"\\]|\\.)*?) (Image|Video|Folder|PDF|Google Docs|Unknown)[^"]*"', h[m.end():m.end()+6000])
        if not al: continue
        vistos.add(did); itens.append({'id':did,'nome':html.unescape(al.group(1)),'tipo':al.group(2)})
    return itens

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('folder'); ap.add_argument('--baixar'); ap.add_argument('--max',type=int,default=1600)
    a = ap.parse_args()
    itens = listar(a.folder)
    if itens is None: sys.exit('pasta não é pública (página de login/erro)')
    for it in itens: print(f"{it['id']}  {it['tipo']:7s} {it['nome']}")
    if not a.baixar: return
    from PIL import Image
    os.makedirs(a.baixar, exist_ok=True)
    for it in itens:
        if it['tipo'] != 'Image': continue
        base = re.sub(r'[^A-Za-z0-9._-]+','_', re.sub(r'^(Cópia de )+','',it['nome'])).strip('_')
        dst = os.path.join(a.baixar, base); raw = dst + '.raw'
        subprocess.run(['curl','-sL','--max-time','300','-o',raw,f"https://drive.usercontent.google.com/download?id={it['id']}&export=download&confirm=t"])
        try:
            im = Image.open(raw); im.load()
            if a.max: im.thumbnail((a.max,a.max))
            (im.convert('RGBA') if dst.lower().endswith('.png') else im.convert('RGB')).save(dst, quality=88)
            print('ok', base, im.size)
        except Exception as e:
            print('FALHA', it['nome'], e)
        finally:
            if os.path.exists(raw): os.remove(raw)

if __name__ == '__main__': main()
