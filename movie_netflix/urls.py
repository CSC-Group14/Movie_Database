from django.urls import path
from .views import (category_list, 
                    movie_list,payment_list,user_list,subscription_list,profile_list,review_list,channel_list,query)
urlpatterns = [
    path('categories/', category_list, name='category_list'),


    path('movies/', movie_list, name='movie_list'),
    path('users/', user_list, name='user_list'),
    path('subscriptions/', subscription_list, name='subscription_list'),
    path('channels/', channel_list, name='channel_list'),
    path('payment/', profile_list, name='profile_list'),
    path('profile/', payment_list, name='payment_list'),
    path('review/', review_list, name='review_list'),
    path('review/', query, name='query'),
    # path('watch/', watch_list, name='watch_list'),
  
]
