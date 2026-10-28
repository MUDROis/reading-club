import os
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
for root,dirs,files in os.walk(folder):
 for f in files:
  if 'a2_06' in f or '06' in f:
   print(os.path.join(root,f))
