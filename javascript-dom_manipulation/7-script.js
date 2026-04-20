fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        console.log(data);
        const listMovies = document.getElementById('list_movies');
        data.results.forEach((movie) => {
            const newMovie = document.createElement('li');
            newMovie.innerHTML = movie.title;
            listMovies.appendChild(newMovie);
        })
    })
    .catch(function(error) {
        console.log(error);
    });
