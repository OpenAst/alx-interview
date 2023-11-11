#!/usr/bin/node

; 'use strict';

const request = require('request');

function getCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request.get({ url: characterUrl, json: true }, (error, response, characterData) => {
      if (error) {
        reject(`Error fetching character data: ${error.message}`);
      } else {
        resolve(characterData.name);
      }
    });
  });
}

async function getMovieCharacters(movieId) {
  // Star Wars API base URL
  const baseUrl = 'https://swapi.dev/api/films/';

  // Make a request to get information about the specified movie
  request.get({ url: `${baseUrl}${movieId}/`, json: true }, async (error, response, movieData) => {
    if (error) {
      console.error(`Error fetching movie data: ${error.message}`);
      return;
    }

    // Extract characters list from the movie data
    const charactersUrls = movieData.characters;

    try {
      // Use Promise.all to wait for all character requests to complete
      const characterNames = await Promise.all(charactersUrls.map(getCharacterName));

      // Print character names
      characterNames.forEach(name => {
        console.log(name);
      });
    } catch (error) {
      console.error(`Error: ${error}`);
    }
  });
}

// Check if Movie ID is provided as a command line argument
if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
} else {
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}

