#!/usr/bin/node
const dict = require('./101-data.js').dict;

const sortedDict = {};
for (const key in dict) {
  const value = dict[key];
  if (!(value in sortedDict)) {
    sortedDict[value] = [key];
  } else {
    sortedDict[value].push(key);
  }
}

console.log(sortedDict);
