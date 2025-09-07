from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("years/", views.years, name="years"),
    path("months/<int:year>/", views.months, name="months"),
    path("days/<int:year>/<int:month>/", views.days, name="days"),
    path("workout/<int:year>/<int:month>/<int:day>/", views.workout_detail, name="workout_detail"),
]
