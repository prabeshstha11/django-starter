from django.urls import path
from .views import receipe_list, create_list, update_list, delete_item

urlpatterns = [
    # read
    path("receipe/", receipe_list, name="receipe_list"),
    
    # create
    path("receipe/create/", create_list, name="create_list"),
    
    # update
    path("receipe/<id>/", update_list, name="update_list"),
    
    # delete
    path("receipe/delete/<id>", delete_item, name="delete_list")
]
