from django.urls import path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (ReviewCreate, ReviewList, ReviewDetail, WatchListAV, WatchListDetailAV,
                                     StreamPlatformAV, StreamPlatformDetailAV)

urlpatterns = [
    path('list', WatchListAV.as_view(), name='watchlist-list'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='watchlist-detail'), 
    path('stream', StreamPlatformAV.as_view(), name='stream-platform'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review', ReviewList.as_view(), name='review-list'), 
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
]
