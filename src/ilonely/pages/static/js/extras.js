function getLocation() {
    function getLocation() {
        var output = document.getElementById("message");

        if (!navigator.geolocation) {
            // alert user that their browser does not support geolocation
            output.innerHTML = "Not supported";
            return;
        }

        function success(position) {
            document.getElementById('latitude').value = position.coords.latitude;
            document.getElementById('longitude').value = position.coords.longitude;
            output.innerHTML = "Success!";
            // document.getElementById.submit("geolocation");
        }

        function error() {
            // alert user of geolocation error
            // do not update user's location
            output.innerHTML = "geolocation api error";
        }
        output.innerHTML = "Looking for your location...";
        navigator.geolocation.getCurrentPosition(success, error);
    }
}

function sortPeople(radius) {
    profileList = document.getElementById("profiles");
    profileListItems = profileList.getElementsByTagName('li');

    for (i = 0; i < profileListItems.length; i++) {
        dist = document.getElementsByClassName("distances")[i];
        if (parseFloat(dist.innerHTML) < radius) {
            profileListItems[i].style.display = "";
        } else {
            profileListItems[i].style.display = "none";
        }
    }
}

// map.setView([{{ user.profile.latitude }}, {{ user.profile.longitude }}], 14);