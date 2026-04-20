document.addEventListener('DOMContentLoaded', function() {
fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        console.log(data);
        document.getElementById('hello').innerHTML = data.hello;
    })
    .catch(function(error) {
        console.log(error);
    })
});
