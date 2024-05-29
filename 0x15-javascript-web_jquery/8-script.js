// JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
'use strict';
$(document).ready(() => {
  const API_URL = 'https://swapi-api.hbtn.io/api';
  $.get(`${API_URL}/films/?format=json`, (data, status) => {
    data.results.forEach(film => {
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    });
  });
});
