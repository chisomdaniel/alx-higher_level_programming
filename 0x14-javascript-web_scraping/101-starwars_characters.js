#!/usr/bin/node

const request = require('request');

const args = process.argv;

const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];

request(url, { json: true }, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }

  for (const element of body.characters) {
    request(element, { json: true }, function (err, response, body) {
      if (err) {
        return;
      }
      console.log(body.name);
    });
  }
});
