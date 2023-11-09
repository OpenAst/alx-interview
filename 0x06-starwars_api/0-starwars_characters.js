#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl 'https://swapi-api.alx-tools.com/api/films/${movieId}/';

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode == 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.error('Error fetching character data:', charError);
        }
      });
    });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
