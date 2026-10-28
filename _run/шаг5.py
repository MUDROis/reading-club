import os,re
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
parts=os.path.join(folder,"parts")

for fn in ["a1_02","a1_04","a1_05","a1_06"]:
    p=os.path.join(parts,fn+".js")
    s=open(p,encoding="utf-8").read()
    # найдём id сегмента с ending:true
    ends=[m.group(1) for m in re.finditer(r"(\w+):\{text:`[^`]*`,\s*ending:true",s)]
    if not ends:
        print(fn,"no ending found"); continue
    endid=ends[-1]
    # найдём выбор, указывающий на endid, и перенаправим на s9
    # ищем "n:'{endid}'"
    pat="n:'"+endid+"'"
    m=re.search(re.escape(pat),s)
    if not m:
        print(fn,"no choice to",endid); continue
    s=s[:m.start()]+"n:'s9'"+s[m.end():]
    open(p,"w",encoding="utf-8").write(s)
    print(fn,"перенаправлен",endid,"-> s9")
