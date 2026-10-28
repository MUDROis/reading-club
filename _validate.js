const fs=require('fs');
function load(path){
  const raw=fs.readFileSync(path,'utf8').replace(/^\uFEFF/,'').replace(/^\/\*[\s\S]*?\*\/\s*/,'');
  return eval('['+raw+'][0]');
}
function analyze(src,name){
  try{
    const s=load(src);
    const segs=s.segs||{};
    const keys=Object.keys(segs);
    let words=0;
    for(const k of keys) words+=(segs[k].text.match(/[A-Za-z']+/g)||[]).length;
    const ends=keys.filter(k=>segs[k].ending);
    // битые ссылки
    const broken=[];
    for(const k of keys){
      const ch=(segs[k].choices||[]);
      for(const c of ch) if(!segs[c.n]) broken.push(k+'->'+c.n);
    }
    // достижимость
    const seen=new Set([s.start]); const q=[s.start];
    while(q.length){ const k=q.shift(); for(const c of (segs[k].choices||[])) if(!seen.has(c.n)){seen.add(c.n);q.push(c.n);} }
    const unreach=keys.filter(k=>!seen.has(k));
    console.log(`${name} | title="${s.title}" | segs=${keys.length} | words=${words} | end=${ends.length} | start=${s.start} | broken=${broken.length?broken.join(','):'нет'} | unreach=${unreach.length?unreach.join(','):'нет'} | quiz=${Array.isArray(s.quiz)?s.quiz.length:0}`);
    return {words,seg:keys.length,end:ends.length};
  }catch(e){ console.log(name+' | ОШИБКА: '+e.message); return null; }
}
console.log('--- A1 ---');
for(let i=1;i<=7;i++) analyze(`parts/a1_0${i}.js`,`a1_0${i}`);
console.log('--- A2 ---');
for(let i=1;i<=7;i++){
  const p=i===3?'C:/Users/Lenovo/Documents/Dewiar/Задачи/2026-10-28 2338 A2.3 The Secret Treehouse/outputs/a2_03.js':`parts/a2_0${i}.js`;
  if(fs.existsSync(p)) analyze(p,`a2_0${i}`);
  else console.log(`a2_0${i} | НЕТ ФАЙЛА`);
}
console.log('--- B1 (из app.html) ---');
const html=fs.readFileSync('outputs/app.html','utf8');
const bStart=html.indexOf('const B1_NEW_STORIES=[');
const bEnd=html.indexOf('];\nSTORIES.a1.push');
if(bStart>=0&&bEnd>0){
  const arr=eval('('+html.slice(bStart+html.indexOf('['),bEnd+2)+')');
  arr.forEach((s,i)=>{
    const segs=s.segs||{}; const keys=Object.keys(segs);
    let words=0; for(const k of keys) words+=(segs[k].text.match(/[A-Za-z']+/g)||[]).length;
    const ends=keys.filter(k=>segs[k].ending);
    const broken=[]; for(const k of keys) for(const c of (segs[k].choices||[])) if(!segs[c.n]) broken.push(k+'->'+c.n);
    console.log(`b1 embedded[${i}] | "${s.title}" | segs=${keys.length} | words=${words} | end=${ends.length} | broken=${broken.length?broken.join(','):'нет'} | quiz=${Array.isArray(s.quiz)?s.quiz.length:0}`);
  });
}
