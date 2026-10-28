import os,re
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
parts=os.path.join(folder,"parts")

for i in range(1,8):
    fn=f"a1_{i:02d}"
    s=open(os.path.join(parts,fn+".js"),encoding="utf-8").read()
    # слова в текстах
    texts=re.findall(r"`([^`]*)`",s)
    w=sum(len(t.split()) for t in texts)
    # сегменты
    segids=set(re.findall(r"(\w+):\{text:`",s))
    start=re.search(r"start:'(\w+)'",s).group(1)
    # все цели n:'...'
    targets=re.findall(r"n:'(\w+)'",s)
    # цели вне segids
    dangling=[t for t in targets if t not in segids]
    # ending-сегменты
    ends=re.findall(r"(\w+):\{text:`[^`]*`,\s*ending:true",s)
    # достижимость от start
    reachable=set([start])
    changed=True
    while changed:
        changed=False
        for sid in list(reachable):
            m=re.search(re.escape(sid)+r":\{text:`[^`]*`(.*?)(?=\n\s*\w+:\{text:|\n\s*\},)",s,re.S)
            if m:
                for t in re.findall(r"n:'(\w+)'",m.group(1)):
                    if t not in reachable:
                        reachable.add(t); changed=True
    unreachable=segids-reachable
    print(f"{fn}: {w} слов | start={start} | сегментов={len(segids)} | битых={dangling} | недостижимых={sorted(unreachable)} | концовок={len(ends)}")
