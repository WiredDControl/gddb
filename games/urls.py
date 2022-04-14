from django.urls import path
from . import views

urlpatterns = [
    #path('', views.games_list, name='games_list'),
    path('', views.releases_list.as_view(), name='releases_list'),
    path('games', views.games_list.as_view(), name='games_list'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('glp', views.glp_list, name='glp_list'),
    path('glp/<int:pk>/', views.glp_detail, name='glp_detail'),
    path('glp/new/', views.glp_new, name='glp_new'),
    path('glp/<int:pk>/edit/', views.glp_edit, name='glp_edit'),
    path('release/<int:pk>/', views.release_detail, name='release_detail'),
    path('image/', views.image_upload_view)
]