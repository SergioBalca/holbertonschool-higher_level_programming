#!/usr/bin/node

const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.get(url, (data) => {
  $('div#hello').append(data.hello);
});
