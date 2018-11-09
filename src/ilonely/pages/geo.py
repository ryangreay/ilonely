from math import sin, cos, sqrt
from haversine import haversine
from django.contrib.auth.models import User
from django.conf import settings
from pages.models import Profile
from urllib.parse import urljoin
import requests

# returns the user's location info in a dictionary
def getLocation():
    response = requests.get('http://api.ipstack.com/check?access_key=' + 'adb841f493ebe55b01d9d14d8992f765')
    geodata = response.json()
    return geodata

# returns a list of people nearby in a something mi radius
def getNearby(user, radius):
    myProfile = user.profile
    profiles = Profile.objects.exclude(user = user).all()
    nearbyPeople = []

    meLoc = (myProfile.latitude, myProfile.longitude)

    if profiles is not None:
        for profile in profiles:
            userLoc = (profile.latitude, profile.longitude)
            if all(userLoc):
                if haversine(meLoc, userLoc, miles=True) < radius:
                    nearbyPeople.append(profile)

    return nearbyPeople