from django.urls import path
from contents import views

urlpatterns = [
  path('contents/', views.index)
]