from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/detail/',views.recipe_detail,name='recipe_detail'),
    path('recipe/new/',views.recipe_new,name='recipe_new'),
    path('like/',views.like_post,name="like_post"),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete', views.recipe_delete, name='recipe_delete'),

]