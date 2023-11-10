#!/usr/bin/node

const request = require('request');

const MOVIE_ID = 3; // Return of the Jedi

const API_ENDPOINT = 'https://swapi-api.alx-tools.com/api/films/';

async function getCharacters(movieId){
    const response = await request.get(`${API_ENDPOINT}${movieId}`);
    const movieData = JSON.parse(response.body);

    const characters = movieData.characters;

    for (const character of characters) {
      console.log(character.name);
    }
}
getCharacters(MOVIE_ID);
