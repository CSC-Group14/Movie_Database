from django.urls import path
from .views import (category_list, category_create, category_detail, category_update, category_delete,
                    movie_list, movie_create, movie_detail, movie_update, movie_delete,payment_list,review_list,watch_list,subscription_list,user_list,profile_list)

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('categories/add/', category_create, name='category_create'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('categories/<int:pk>/edit/', category_update, name='category_update'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),

    path('movies/', movie_list, name='movie_list'),
    path('movies/add/', movie_create, name='movie_create'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/<int:pk>/edit/', movie_update, name='movie_update'),
    path('movies/<int:pk>/delete/', movie_delete, name='movie_delete'),
    
    path('payment/', profile_list, name='profile_list'),
    path('profile/', payment_list, name='payment_list'),
    path('review/', review_list, name='review_list'),
    path('watch/', watch_list, name='watch_list'),
    path('subscription/', subscription_list, name='subscription_list'),
    path('user/', user_list, name='user_list'),

    # Add URLs for Payment, Profile, Review, Subscription, User, and WatchList views
]
