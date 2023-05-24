#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const args = process.argv;

request(args[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }

  fs.writeFile(args[3], body, 'utf8', (err) => {
    if (err) {
      console.error('error:', err);
    }
  });
});
