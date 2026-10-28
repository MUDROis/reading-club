import os
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
p=os.path.join(folder,"parts","a1_stories.js")
s=open(p,encoding="utf-8").read()
# извлечь объект первой истории между 'const A1_STORIES=[' и '];'
start=s.index("const A1_STORIES=[")+len("const A1_STORIES=[")
end=s.rindex("];")
obj=s[start:end].strip()
open(os.path.join(folder,"parts","a1_01.js"),"w",encoding="utf-8").write(obj)
print("a1_01.js сохранён, len",len(obj))
print("слов в истории:", len(obj.split()))
