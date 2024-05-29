// JavaScript script that updates the text of the <header> element to New Header!!!
'use strict';
$(document).ready(() => {
  $('#update_header').on('click', () => {
    $('header').text('New Header!!!');
  });
});
