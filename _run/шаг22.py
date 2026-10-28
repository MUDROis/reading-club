import os,re
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
for fn in ["parts/a2_05.js"]:
 p=os.path.join(folder,fn)
 s=open(p,encoding="utf-8").read()
 texts=re.findall(r"`([^`]*)`",s)
 w=sum(len(t.split()) for t in texts)
 segids=set(re.findall(r"(\w+):\{text:`",s))
 targets=re.findall(r"n:'(\w+)'",s)
 dangling=[t for t in targets if t not in segids]
 print(fn,"слов:",w,"| сегментов:",len(segids),"| битых:",dangling,"| скобки:",s.count("{")-s.count("}"))
