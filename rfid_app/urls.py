from django.urls import path
from . import views

app_name = 'rfid_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_tag, name='add_tag'),
    path('search/', views.search, name='search'),
    path('tags/<str:uid>/', views.tag_detail, name='tag_detail'),
    path('tags/<str:uid>/delete/', views.delete_tag, name='delete_tag'),
]
