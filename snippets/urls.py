from django.conf.urls import include
from django.urls import path
from . import views

app_name = "snippets"
urlpatterns = [
    path(
        "info/",
        include(
            [
                path("snippet-list/", views.snip_listing, name="list"),
                path("<int:id>/", views.snip_detail, name="detail"),
                path("add-new/", views.add_new, name="addnew"),
            ]
        ),
    )
]
