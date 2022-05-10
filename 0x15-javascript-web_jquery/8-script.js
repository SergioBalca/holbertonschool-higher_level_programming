#!/usr/bin/node

const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, (data) => {
  $(data.results).each((index) => {
    $('ul#list_movies').append('<li>' + data.results[index].title + '</li>');
  });
}, 'json');
