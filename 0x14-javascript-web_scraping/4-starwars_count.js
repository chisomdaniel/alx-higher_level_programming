#!/usr/bin/node

const request = require('request');

const args = process.argv;

const url = args[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
let count = 0;

request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }

  for (let i = 0; i < body.results.length; i++) {
    for (let j = 0; j < body.results[i].characters.length; j++) {
	if (body.results[i].characters[j].includes('18')) {
          count++;
	}
    }
  }

  console.log(count);
});
