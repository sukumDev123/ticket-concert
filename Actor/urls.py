from django.contrib import admin
from django.urls import path
from .views import *
app_name = "Actor"
urlpatterns = [
    path("get_all_actors/", get_all_actors, name="get_all_actors"),
    path("get_by_id_actor/", get_by_id_actor, name="get_by_id_actor"),
    path("delete_by_id_actor/", delete_by_id_actor, name="delete_by_id_actor"),
    path("edit_by_id_actor/", edit_by_id_actor, name="edit_by_id_actor"),
    path("add_actor/", add_actor, name="add_actor"),
]


# - Actor
# 	- /Actor/get_all_actors/
# 	- /Actor/get_by_id_actor/?id_actor
# 	- /Actor/delete_by_id_actor/?id_actor
# 	- /Actor/edit_by_id_actor/?id_actor
# 	- /Actor/add_actor/
