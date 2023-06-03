$(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (index, value) {
      const mainText = $('<li></li>').text(value.title);
      $('ul#list_movies').append(mainText);
    });
  });
});
