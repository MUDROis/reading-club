'use strict';
// Сборка app.html (корень проекта): заменяет блок const STORIES={...}
// на const STORIES={a1:[...],a2:[...],b1:[...]} из файлов parts/*.js
const fs = require('fs');
const path = require('path');

const dir = __dirname;
const appPath = path.join(dir, 'app.html');
const backupPath = path.join(dir, 'outputs', 'app.backup.html');
let html = fs.readFileSync(appPath, 'utf8');

const startMarker = 'const STORIES={';
const endMarker = 'const DICT={';
const startIdx = html.indexOf(startMarker);
const endIdx = html.indexOf(endMarker);
if (startIdx < 0 || endIdx < 0 || endIdx <= startIdx) {
  console.error('Маркеры не найдены: startIdx=' + startIdx + ' endIdx=' + endIdx);
  process.exit(1);
}

function loadPart(name) {
  const p = path.join(dir, 'parts', name);
  if (!fs.existsSync(p)) throw new Error('Нет файла: ' + p);
  let src = fs.readFileSync(p, 'utf8');
  src = src.replace(/^\uFEFF/, '');
  src = src.replace(/^\/\*[\s\S]*?\*\/\s*/, '');
  src = src.trim();
  if (!src.endsWith('}')) throw new Error('Файл не заканчивается на }: ' + name);
  return src;
}

const a1 = [], a2 = [], b1 = [];
for (let i = 1; i <= 7; i++) {
  a1.push(loadPart('a1_0' + i + '.js'));
  a2.push(loadPart('a2_0' + i + '.js'));
  b1.push(loadPart('b1_0' + i + '.js'));
}

const block =
  'const STORIES={\n' +
  '  a1:[\n' + a1.join(',\n') + '\n  ],\n' +
  '  a2:[\n' + a2.join(',\n') + '\n  ],\n' +
  '  b1:[\n' + b1.join(',\n') + '\n  ]\n' +
  '};\n\n';

fs.mkdirSync(path.dirname(backupPath), { recursive: true });
fs.writeFileSync(backupPath, html);
html = html.slice(0, startIdx) + block + html.slice(endIdx);
fs.writeFileSync(appPath, html);
console.log('Готово. Итог: ' + appPath);
console.log('Бэкап: ' + backupPath);
console.log('Новый размер app.html: ' + Buffer.byteLength(html) + ' байт');
