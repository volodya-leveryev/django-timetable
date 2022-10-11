from django.urls import path

from timetable import views

urlpatterns = [
    path("", views.index_page),
]
