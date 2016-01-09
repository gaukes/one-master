$(document).ready(function() {
        $.ajax({
                url: "http://localhost:5000/one/api/v1.0/points/1"
        }).then(function(data) {
                // $('.user-name').empty().append(data.users[0].name);
                $('.user-currency').empty().append(data.users[0].currency + " INR");
        });
});

function refresh_points() {
	// TODO: clear the XHRs files being created
	$.ajax({
                url: "http://localhost:5000/one/api/v1.0/points/1"
        }).then(function(data) {
                // $('.user-name').empty().append(data.users[0].name);
                $('.user-currency').empty().append(data.users[0].currency + " INR");
    });
	setTimeout(refresh_points, 500);
};

refresh_points();