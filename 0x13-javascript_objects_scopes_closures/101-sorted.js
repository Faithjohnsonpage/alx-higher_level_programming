#!/usr/bin/node
const dict = require('./101-data.js').dict;

let sorted_dict = {};
for (let key in dict) {
  let value = dict[key];
  if (!(value in sorted_dict)) {
    sorted_dict[value] = [key];
  } else {
    sorted_dict[value].push(key);
  }
}

console.log(sorted_dict);
