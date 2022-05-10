#!/usr/bin/node

const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.get(url, function (data) {
  $('div#character').append(data.name);
}, 'json');
