const request = require('request');

function getMovieCharacters(movieId) {
  // Star Wars API base URL
  const baseUrl = 'https://swapi.dev/api/films/';

  // Make a request to get information about the specified movie
  request.get({ url: `${baseUrl}${movieId}/`, json: true }, (error, response, movieData) => {
    if (error) {
      console.error(`Error fetching movie data: ${error.message}`);
      return;
    }

    // Extract characters list from the movie data
    const charactersUrls = movieData.characters;

    // Use a recursive function to process characters one by one
    function processCharacter(index) {
      if (index === charactersUrls.length) {
        // All characters processed, exit
        return;
      }

      // Make a request to get information about the character
      request.get({ url: charactersUrls[index], json: true }, (characterError, characterResponse, characterData) => {
        if (characterError) {
          console.error(`Error fetching character data: ${characterError.message}`);
        } else {
          // Print the character name
          console.log(characterData.name);
        }

        // Process the next character
        processCharacter(index + 1);
      });
    }

    // Start processing characters from index 0
    processCharacter(0);
  });
}

// Check if Movie ID is provided as a command line argument
if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
} else {
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}

