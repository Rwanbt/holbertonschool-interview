#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const getCharacters = async () => {
  try {
    const filmData = await requestPromise(url);
    const charactersList = filmData.characters;

    for (const characterUrl of charactersList) {
      const characterData = await requestPromise(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
};

getCharacters();
