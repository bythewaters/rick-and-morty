from django.urls import path

from characters.views import get_random_character

urlpatterns = [
    path("random-character/", get_random_character, name="random_character"),
]

app_name = "characters"
