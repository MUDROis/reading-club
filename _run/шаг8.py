import os,re
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
parts=os.path.join(folder,"parts")

adds = {
 "a1_02": "After the games, grandmother says: \"Let me tell you a story about when your mother was little.\" Everyone listens. Grandmother tells a funny story about how mother lost her shoe in the garden. Everyone laughs. Emma says: \"Tell us more, Grandma!\" Grandmother smiles and tells another story. Then mother brings tea. They all drink tea together. Emma looks around. Her whole family is here. She feels warm and happy. She thinks: \"I am so lucky.\" After tea, it is late. Emma kisses everyone good night and goes to bed. She sleeps with a smile.",
 "a1_04": "In the evening, Leo's father comes home. He sees the balloons. \"Wow, Leo! You have many balloons!\" he says. Leo tells him about the red balloon and the wind. Father says: \"That is sad. But look, you have new balloons now.\" Leo smiles. \"Yes, and Mia gave me one too,\" he says. Father says: \"You have good friends, Leo.\" Leo nods. Then father takes one balloon and ties it to Leo's wrist. \"Now it can not fly away,\" he says. Leo laughs. He plays with the balloons. He is happy. He learned that even when you lose something, good things can come.",
 "a1_05": "The next day, Emma draws a picture. She draws the picnic, the ducks, and the big tree. She shows it to her mother. \"It is beautiful, Emma!\" says mother. \"Can we put it on the fridge?\" Emma nods. They put the picture on the fridge. Max looks at it. \"I want to draw too!\" he says. He draws a big duck. Everyone laughs. Emma is happy. She thinks about the picnic. It was a wonderful day. She hopes they will go on another picnic soon. Mother says: \"We can go again next Sunday if the weather is nice.\" Emma and Max are very happy. They can not wait.",
 "a1_06": "When they come home from the zoo, Leo and Anna tell their mother about everything. \"We saw a lion!\" says Leo. \"And a giraffe!\" says Anna. \"And a talking parrot!\" they both say. Mother smiles. \"That sounds wonderful,\" she says. Leo shows the pictures he drew of the animals. He drew a lion and an elephant. Anna drew a giraffe and a penguin. Mother puts the pictures on the wall. \"Now we can see the animals every day,\" she says. Leo and Anna are happy. They go to bed and dream about the zoo. It was a perfect day.",
}

for fn,text in adds.items():
    p=os.path.join(parts,fn+".js")
    s=open(p,encoding="utf-8").read()
    if "s9:" in s:
        print(fn,"уже есть s9"); continue
    marker="},\nquiz"
    pos=s.rfind(marker)
    if pos==-1:
        print(fn,"marker not found"); continue
    newseg=" s9:{text:`"+text+"`, ending:true},"
    s=s[:pos]+newseg+s[pos:]
    open(p,"w",encoding="utf-8").write(s)
    print(fn,"s9 вставлен")
