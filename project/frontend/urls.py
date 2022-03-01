from django.urls import path
from .views import indexView, loadingView, dashboardView  # the view responsible for the frontend
urlpatterns = [
    path('', indexView, name='index'),  # add the view to the url
    path('dashboard', dashboardView),
    path('loading',loadingView)
]
