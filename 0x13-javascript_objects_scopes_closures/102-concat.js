#!/usr/bin/node
const fs = require('fs');

if (process.argv.length === 5) {
  const fileA = process.argv[2];
  const fileB = process.argv[3];
  const fileC = process.argv[4];

  fs.readFile(fileA, (errA, dataA) => {
    if (errA) {
      console.error(errA);
      return;
    }
    fs.readFile(fileB, (errB, dataB) => {
      if (errB) {
        console.error(errB);
        return;
      }
      fs.writeFile(fileC, dataA, err => {
        if (err) {
          console.error(err);
          return;
        }
        fs.appendFile(fileC, dataB, err => {
          if (err) {
            console.error(err);
            return;
          }
          console.log(`Files ${fileA} and ${fileB} were merged into ${fileC}`);
        });
      });
    });
  });
} else {
  console.log('Usage: ./merge_files.js <fileA> <fileB> <fileC>');
}
