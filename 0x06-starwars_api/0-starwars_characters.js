#/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
  const baseUrl = 'https://swapi.dev/api/films/';
  
  request.get('${baseUrl}${movieId}/', { json: true }, (error, response, movieData) => {
    if (error) {
      console.error('Erro fetching movie data: ${error.message}');
      return;
    }

    const characterUrls = movieData.characters;

    charactersUrls.forEach(characterUrl => {
      request.get(characterUrl, { json: true }, (characterError, characterResponse, characterData) => {
	if (characterError) {
	  console.error('Error fetching character data: ${characterError.message}');
	  return;
	}
	console.log(characterData.name);
      });
    });
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
} else {
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}
