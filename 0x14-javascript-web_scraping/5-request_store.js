#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

let data = '';
request.get(url)
  .on('data', (chunk) => {
    data += chunk;
  })
  .on('end', () => {
    fs.writeFile(filePath, data, 'utf-8', (err) => {
	  if (err) {
	    console.log(err);
	  }
    });
  });
