import os,shutil
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
src=os.path.join(folder,"parts","A2.4 The Lost Puppy","a2_04.js")
dst=os.path.join(folder,"parts","a2_04.js")
shutil.copy(src,dst)
print("скопировано",os.path.getsize(dst),"байт")
