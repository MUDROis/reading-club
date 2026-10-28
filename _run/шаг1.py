import os,re
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
p=os.path.join(folder,"outputs","app.html")
s=open(p,encoding="utf-8").read()
# границы
i_stories=s.find("const STORIES={")
i_dict=s.find("const DICT={")
print("const STORIES={ at",i_stories)
print("const DICT={ at",i_dict)
# что между ними (первые 400 и последние 400 символов)
mid=s[i_stories:i_dict]
print("len mid:",len(mid))
print("--- начало mid ---")
print(mid[:400])
print("--- конец mid ---")
print(mid[-400:])
# сколько раз встречается 'segs'
print("segs count:",mid.count("segs"))
