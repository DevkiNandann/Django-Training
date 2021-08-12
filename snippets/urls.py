from django.conf.urls import include
from django.urls import path
from . import views

app_name = "snippets"
urlpatterns = [
    path(
        "info/",
        include(
            [
                path("snippet-list/", views.SnippetList.as_view(), name="list"),
                path("<int:id>/", views.SnippetDetail.as_view(), name="detail"),
            ]
        ),
    )
]
