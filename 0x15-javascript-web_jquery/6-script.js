#!/usr/bin/node

const $ = window.$;

$('div#update_header').click(function () {
  $('header').replaceWith('<header>New Header!!!</header>');
});
