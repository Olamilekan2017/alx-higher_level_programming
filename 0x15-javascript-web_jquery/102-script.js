// JavaScript script that fetches and prints how to say “Hello” depending on the language
'use strict';
$(document).ready(() => {
	$('INPUT#btn_translate').click(() => {
		const APIURL = 'https://fourtonfish.com';
		const languageCode = $('INPUT#language_code').val();
		$.get(`${APIURL}/hellosalut/?lang=${languageCode}`, (langdata, status) => {
			$('DIV#hello').html(langdata.hello);
		});
	});
});)
