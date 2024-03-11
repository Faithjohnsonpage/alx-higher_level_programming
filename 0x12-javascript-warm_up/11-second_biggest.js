#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  let max = parseInt(process.argv[2]);
  let secondMax = -Infinity;

  for (let i = 3; i < process.argv.length; i++) {
    const num = parseInt(process.argv[i]);

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax) {
      secondMax = num;
    }
  }

  console.log(secondMax === -Infinity ? '0' : secondMax);
}
