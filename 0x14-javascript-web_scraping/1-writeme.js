#!/usr/bin/node

const fs = require('fs');

const args = process.argv;
const text = args[3];

fs.writeFile(args[2], text, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
