import os
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
s=open(os.path.join(folder,"parts","a2_06.js"),encoding="utf-8").read()
print("Длина:",len(s))
print("Начало:",s[:200])
print("Конец:",s[-200:])
import re
print("Сегменты:",re.findall(r"(\w+):\{text:",s))
