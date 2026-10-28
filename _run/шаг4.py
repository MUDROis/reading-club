import os
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
parts=os.path.join(folder,"parts")

# для каждой истории: (файл, новый сегмент id, текст, какой выбор перенаправить: (seg_id, idx_choice, новое_назначение))
adds = {
 "a1_01": ("s9", "Tom shows his father the new bed for Kitty. His father smiles and says: \"You are very kind, Tom. Kitty is lucky to have you.\" Tom is happy. He pets Kitty. Then father says: \"Come, let's read a story before bed.\" Tom and his father sit on the sofa. They read a story about a brave dog. Kitty sits on Tom's lap and listens. She purrs. After the story, Tom is sleepy. He yawns. Father says: \"Time for bed, Tom.\" Tom nods. He takes Kitty to his room. Kitty goes to her new bed. Tom lies down. \"Good night, Dad. Good night, Kitty,\" says Tom. Kitty says \"Meow\". Tom closes his eyes and sleeps.", ("s7",0,"s9")),
 "a1_02": ("s9", "After the games, grandmother says: \"Let me tell you a story about when your mother was little.\" Everyone listens. Grandmother tells a funny story about how mother lost her shoe in the garden. Everyone laughs. Emma says: \"Tell us more, Grandma!\" Grandmother smiles and tells another story. Then mother brings tea. They all drink tea together. Emma looks around. Her whole family is here. She feels warm and happy. She thinks: \"I am so lucky.\" After tea, it is late. Emma kisses everyone good night and goes to bed. She sleeps with a smile.", ("s8",0,"s9")),
 "a1_03": ("s9", "The next morning, Leo and Anna wake up. Rex is already at their door. He wags his tail. \"Good morning, Rex!\" says Leo. Rex barks happily. After breakfast, Leo and Anna take Rex for a walk. Rex runs and jumps. He is so happy. They go to the park. Rex plays with other dogs. He makes new friends. Leo and Anna watch and laugh. On the way home, Leo says: \"Rex, you are the best dog in the world.\" Rex licks Leo's hand. When they come home, they give Rex a big bowl of food. Rex eats and then sleeps. He is a happy dog.", ("s5",0,"s9")),
 "a1_04": ("s9", "In the evening, Leo's father comes home. He sees the balloons. \"Wow, Leo! You have many balloons!\" he says. Leo tells him about the red balloon and the wind. Father says: \"That is sad. But look, you have new balloons now.\" Leo smiles. \"Yes, and Mia gave me one too,\" he says. Father says: \"You have good friends, Leo.\" Leo nods. Then father takes one balloon and ties it to Leo's wrist. \"Now it can not fly away,\" he says. Leo laughs. He plays with the balloons. He is happy. He learned that even when you lose something, good things can come.", ("s8",0,"s9")),
 "a1_05": ("s9", "The next day, Emma draws a picture. She draws the picnic, the ducks, and the big tree. She shows it to her mother. \"It is beautiful, Emma!\" says mother. \"Can we put it on the fridge?\" Emma nods. They put the picture on the fridge. Max looks at it. \"I want to draw too!\" he says. He draws a big duck. Everyone laughs. Emma is happy. She thinks about the picnic. It was a wonderful day. She hopes they will go on another picnic soon. Mother says: \"We can go again next Sunday if the weather is nice.\" Emma and Max are very happy. They can not wait.", ("s8",0,"s9")),
 "a1_06": ("s9", "When they come home from the zoo, Leo and Anna tell their mother about everything. \"We saw a lion!\" says Leo. \"And a giraffe!\" says Anna. \"And a talking parrot!\" they both say. Mother smiles. \"That sounds wonderful,\" she says. Leo shows the pictures he drew of the animals. He drew a lion and an elephant. Anna drew a giraffe and a penguin. Mother puts the pictures on the wall. \"Now we can see the animals every day,\" she says. Leo and Anna are happy. They go to bed and dream about the zoo. It was a perfect day.", ("s8",0,"s9")),
 "a1_07": ("s9", "The next weekend, Emma visits Snowball. The woman is happy to see her. \"Snowball, Emma is here!\" she calls. Snowball runs to Emma. She purrs and rubs against Emma's legs. Emma pets her. \"Hello, Snowball!\" she says. They play together. Snowball chases a little ball. Emma laughs. The woman gives Emma cookies and milk. They have a nice time. Before Emma leaves, she says: \"I will come again, Snowball.\" Snowball says \"Meow\". Emma walks home happy. She has a new friend. She learned that helping others can bring you new friends and joy. She smiles all the way home.", ("s7",0,"s9")),
}

for fn,(newid,text,(src,idx,dst)) in adds.items():
    p=os.path.join(parts,fn+".js")
    s=open(p,encoding="utf-8").read()
    # вставить новый сегмент перед закрывающей '}' объекта segs: найдём '},\nquiz' — конец segs
    # надёжнее: вставить после последнего сегмента. Ищем '}\n},\nquiz' или '}\n},\nquiz'
    marker="},\nquiz"
    pos=s.rfind(marker)
    if pos==-1:
        print(fn,"marker not found"); continue
    # вставить новый сегмент перед marker
    newseg=f" {newid}:{{text:`{text}`, ending:true}},"
    s=s[:pos]+newseg+s[pos:]
    # перенаправить выбор: в сегменте src заменить idx-й n:'dst' на n:'{newid}'
    # найдём объект сегмента src
    import re
    # найдём 'src:{text:`...`' затем choices:[...]
    m=re.search(re.escape(src)+r":\{text:`", s)
    if not m:
        print(fn,"src seg not found"); continue
    # от позиции src до '},' конца сегмента
    segstart=m.start()
    # найдём 'choices:[' после segstart
    ci=s.find("choices:[",segstart)
    # найдём idx-й "n:'...'" внутри этого choices
    # соберём все n:'...' до конца этого сегмента (до '}' перед следующей запятой)
    end=s.find("},\n",ci)
    if end==-1: end=s.find("}",ci)
    chunk=s[ci:end]
    # найдём все n:'...'
    ns=list(re.finditer(r"n:'([^']*)'",chunk))
    if idx>=len(ns):
        print(fn,"choice idx out of range",len(ns)); continue
    m2=ns[idx]
    absstart=ci+m2.start(1); absend=ci+m2.end(1)
    s=s[:absstart]+newid+s[absend:]
    open(p,"w",encoding="utf-8").write(s)
    print(fn,"OK, вставлен",newid)
