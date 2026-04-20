fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        const character = document.getElementById('character');
        character.innerHTML = data.name;
    })
    .catch(function(error) {
        console.log(error);
    });
