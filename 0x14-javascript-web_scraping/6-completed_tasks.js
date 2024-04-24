#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

let data = '';
const tasks = {};
request
  .get(url)
  .on('data', (chunk) => {
    data += chunk;
  })
  .on('end', () => {
    const jsonContent = JSON.parse(data);
    let count = 0;
    let i = 1;
    jsonContent.forEach((element) => {
      if (element.userId === i) {
        if (element.completed === true) {
          count++;
        }
      } else {
        tasks[i] = count;
        i++;
        count = (element.completed === true) ? 1 : 0;
      }
    });
    tasks[i] = count;
    console.log(tasks);
  });
