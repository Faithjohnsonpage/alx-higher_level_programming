#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

let data = '';
let i = 1;
let count = 0;
const tasks = {};
request
  .get(url)
  .on('data', (chunk) => {
    data += chunk;
  })
  .on('end', () => {
    const jsonContent = JSON.parse(data);
    jsonContent.forEach((element) => {
      if (element.userId === i) {
        if (element.completed === true) {
          count++;
        }
      } else {
        tasks[i] = count;
        i++;
        if (element.completed === true) {
          count = 1;
        } else {
          count = 0;
        }
      }
    });
    tasks[i] = count;
    console.log(tasks);
  });
