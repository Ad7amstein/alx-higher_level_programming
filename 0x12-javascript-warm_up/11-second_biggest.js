#!/usr/bin/node

const argv = process.argv;
if (argv.length <= 3) {
  console.log(0);
} else {
  let mx = Number(argv[2]);
  argv.forEach((val, index) => {
    const num1 = Number(val);
    if (num1 > mx) {
      mx = num1;
    }
  });

  let curMx = -Infinity;
  argv.forEach((val, index) => {
    const num2 = Number(val);
    if (num2 > curMx && num2 < mx) {
      curMx = num2;
    }
  });

  console.log(curMx);
}
