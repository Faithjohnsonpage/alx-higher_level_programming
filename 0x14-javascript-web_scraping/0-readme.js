#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
