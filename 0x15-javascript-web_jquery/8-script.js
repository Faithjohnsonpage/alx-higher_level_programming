$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    data.results.forEach( (element) => {
      $('#list_movies').append('<li>' + element['title'] + '</li>');
    });
  });
});
