from django.urls import path

from characters.views import get_random_character, CharacterListView

urlpatterns = [
    path("random-character/", get_random_character, name="random_character"),
    path("characters/", CharacterListView.as_view(), name="characters"),
]

app_name = "characters"
