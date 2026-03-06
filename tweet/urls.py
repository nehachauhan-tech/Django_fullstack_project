
from django.urls import path
from tweet import views

# URL patterns for the tweet app - all CRUD operations
urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),           # List tweets
    path('new/', views.tweet_create, name='tweet_create'),   # Create tweet
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),      # Edit tweet
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'), # Delete tweet
    path('register/', views.register, name='register'),      # User registration
]
