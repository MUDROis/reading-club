import os,re
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
parts=os.path.join(folder,"parts")
tot=0
for i in range(1,8):
    p=os.path.join(parts,f"a1_{i:02d}.js")
    s=open(p,encoding="utf-8").read()
    # слова только в текстах сегментов (между ` и `)
    texts=re.findall(r"`([^`]*)`",s)
    w=sum(len(t.split()) for t in texts)
    tot+=w
    print(f"a1_{i}: {w} слов")
print("A1 всего слов в текстах:",tot)
