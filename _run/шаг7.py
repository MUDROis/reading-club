import os
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
parts=os.path.join(folder,"parts")
for fn in ["a1_02","a1_04","a1_05","a1_06"]:
    s=open(os.path.join(parts,fn+".js"),encoding="utf-8").read()
    print(fn, "s9 есть:", "s9:" in s, "| длина:", len(s))
