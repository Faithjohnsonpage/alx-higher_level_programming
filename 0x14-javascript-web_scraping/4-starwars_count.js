#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const id = '18';

let data = '';
let count = 0;
request
  .get(url)
  .on('data', (chunk) => {
    data += chunk;
  })
  .on('end', () => {
    const jsonContent = JSON.parse(data);
    const results = jsonContent.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes(id)) {
          count++;
        }
      }
    }
    console.log(count);
  });
