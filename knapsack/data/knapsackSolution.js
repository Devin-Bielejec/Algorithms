import { readFileSync } from 'fs';
var textByLine = readFileSync('data/small1.txt').toString().split("\n");

console.log(textByLine);