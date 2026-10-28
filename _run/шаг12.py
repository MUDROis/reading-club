import os
base=r"C:\Users\Lenovo\Documents\Dewiar\Задачи"
folder=os.path.join(base,"2026-10-28 2227 Детская читалка")
parts=os.path.join(folder,"parts")
p=os.path.join(parts,"a2_01.js")

part2 = """ s6:{text:`Tom looked at the note again. "There must be another clue," he said. He turned the paper over. On the other side, there was a small drawing. It showed a bridge. Under the bridge, there was a circle. "A bridge!" said Mia. "There is an old bridge over the river!" They ran to the bridge. It was an old wooden bridge. It crossed the river. Tom and Mia walked under the bridge. It was dark and wet there. They looked around. Mia saw something shiny in the corner. "Tom, look!" she said. She picked it up. It was a small key! It was old and made of brass. "A key!" said Tom. "But what does it open?"

They looked at the key. It was small. "Maybe it opens a box," said Mia. "But we already found the box." Tom thought. "Maybe there is another box somewhere," he said. They looked at the map again. The map showed the park, the river, and the tree. But there was also a small drawing in the corner of the map. It looked like a house. "What is this?" asked Mia. "Maybe it is the old house near the park," said Tom. "Let's go there!"`, choices:[{t:'Пойти к старому дому',n:'s8'},{t:'Вернуться к дереву и поискать ещё',n:'s9'}]},
 s7:{text:`Tom and Mia decided to go home and show the note to their mother. They ran home, wet and tired. "Mom! Look what we found!" shouted Mia. She showed the note to her mother. Mother read it. "The real treasure is not gold. It is the friends you make on the way," she read. She smiled. "This is a beautiful message," she said. "It means that the most important thing is not money or things. It is the people you love and the adventures you share." Tom and Mia thought about this. "So there is no gold?" asked Tom. "Maybe not," said mother. "But you found something better. You had an adventure together. And you learned something important." Tom and Mia smiled. They had a great adventure, even without gold. They put the map and the note in a safe place. It was a treasure they would always keep.`, ending:true},
 s8:{text:`Tom and Mia walked to the old house near the park. It was an old, empty house. Nobody lived there. The windows were broken. The door was locked. Tom tried the door. It would not open. "The key!" said Mia. "Maybe the key opens this door!" Tom took the small key and put it in the lock. It fit! He turned it. The lock clicked. The door opened slowly. Tom and Mia went inside. The house was dark and dusty. There were old furniture and cobwebs. "It is scary," said Mia quietly. "Don't worry," said Tom. "We are together."

They looked around. In the corner, there was an old desk. On the desk, there was a small box. It was locked. "The key must open this box!" said Mia. Tom put the key in the box's lock. It fit! He opened it. Inside, there was a letter and a small bag. Tom opened the letter. It said: "Dear finder, you have found my treasure. It is not gold. It is this: the stories of my life. I hope you enjoy them. — Old Mr. Brown." Tom opened the bag. Inside, there were many old photographs and letters. They were stories of a man's life. Tom and Mia looked at the photos. They showed a young man, a family, and a happy life. "This is the treasure," said Mia softly. "His memories." Tom nodded. "This is better than gold," he said. They took the box home and showed it to their mother. She was amazed. They learned that the best treasures are memories and stories.`, ending:true},
 s9:{text:`Tom and Mia went back to the big tree. They looked around for more clues. Mia saw a small stone near the tree. It was different from the other stones. It was smooth and round. She moved it. Under the stone, there was a small metal box! "Tom! Look!" she shouted. Tom ran to her. They opened the box. Inside, there was a letter and a small bag. Tom opened the letter. It said: "Dear finder, you have found my treasure. It is not gold. It is this: the stories of my life. I hope you enjoy them. — Old Mr. Brown." Tom opened the bag. Inside, there were many old photographs and letters. They were stories of a man's life. Tom and Mia looked at the photos. They showed a young man, a family, and a happy life. "This is the treasure," said Mia softly. "His memories." Tom nodded. "This is better than gold," he said. They took the box home and showed it to their mother. She was amazed. They learned that the best treasures are memories and stories.`, ending:true},
},
quiz:[
 {q:'Where do the children find the map?',o:['In the attic','In the park','In the river'],a:0},
 {q:'What does the map show?',o:['A park, a river, and a big tree','A city','A school'],a:0},
 {q:'What is in the first metal box?',o:['A note with a message','Gold coins','A toy'],a:0},
 {q:'What does the note say?',o:['The real treasure is friends, not gold','Find the gold under the tree','Go home now'],a:0},
 {q:'What is the real treasure?',o:['Memories and stories','Gold','Jewels'],a:0}
]}
"""
with open(p,"a",encoding="utf-8") as f:
    f.write(part2)
print("дописано, размер:", os.path.getsize(p))
