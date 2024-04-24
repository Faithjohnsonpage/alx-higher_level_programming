#!/usr/bin/node

const request = require('request');

const endpoint = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + endpoint;

let data = '';
request
  .get(url)
  .on('data', (chunk) => {
    data += chunk;
  })
  .on('end', () => {
    const jsonContent = JSON.parse(data);
    console.log(jsonContent.title);
  });
