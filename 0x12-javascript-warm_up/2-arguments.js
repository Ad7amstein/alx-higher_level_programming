#!/usr/bin/node

const argv = process.argv;
const len = argv.length;
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argumet found');
} else {
  console.log('Arguments found');
}
