#!/usr/bin/node

const len = Number(process.argv[2]);

if (isNaN(len)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < len; ++i) {
    for (let j = 0; j < len; ++j) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
