#!/usr/bin/node

const argv = process.argv;
if (argv.length <= 3) {
  console.log(0);
} else {
  let mx = argv[2];
  argv.forEach((val, index) => {
    if (val > mx) {
      mx = val;
    }
  });

  let curMx = -Infinity;
  argv.forEach((val, index) => {
    if (val > curMx && val < mx) {
      curMx = val;
    }
  });

  console.log(curMx);
}
