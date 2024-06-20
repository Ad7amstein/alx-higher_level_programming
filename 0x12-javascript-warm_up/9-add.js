#!/usr/bin/node

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

console.log(add(num1, num2));

function add (a, b) {
  return a + b;
}
