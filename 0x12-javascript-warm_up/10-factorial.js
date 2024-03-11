#!/usr/bin/node

function factorial (value) {
  if (value === 0 || isNaN(value)) {
    return 1;
  }
  return value * factorial(value - 1);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
