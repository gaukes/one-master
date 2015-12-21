function helloWorld() {
        document.getElementById('points').innerHTML = "1000";
        alert('Hello World!');
}

$(document).ready(function() {
        $.ajax({
                url: "http://localhost:5000/one/api/v1.0/points/1"
        }).then(function(data) {
                $('.user-name').append(data.users[0].name);
                $('.user-points').append(data.users[0].points);
        });
});
