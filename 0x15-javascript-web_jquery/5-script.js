// JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item
'use strict';
$(document).ready(() => {
  $('#add_item').on('click', () => {
    const listItem = $('<li>').text('Item');
    $('ul.my_list').append(listItem);
  });
});
