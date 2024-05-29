// JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
'use strict';
$(() => {
  const APIURL = 'https://swapi-api.hbtn.io/api';
  $.get(`${APIURL}/people/5/?format=json`, (charName, status) => {
    $('DIV#character').html(charName.name);
  });
})
