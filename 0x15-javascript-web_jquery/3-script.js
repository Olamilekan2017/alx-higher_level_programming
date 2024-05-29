// JavaScript script that adds the class red to the <header> element
'use strict';
$(() => {
  $('DIV#red_header').click(() => {
    if (!$('header').hasClass('red')) {
      $('header').addClass('red');
    }
  });
});
