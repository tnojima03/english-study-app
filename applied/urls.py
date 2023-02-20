from django.contrib import admin
from django.urls import path, include
from .views import ListeningList, ListeningDetail, ListeningCreate, ListeningDelete, ListeningUpdate

app_name = 'word_app'

urlpatterns = [
    path('list/', ListeningList.as_view(), name='list_applied'),
    path('detail/<int:pk>', ListeningDetail.as_view(), name='detail'),
    path('create/', ListeningCreate.as_view(), name='create'),
    path('delete/<int:pk>', ListeningDelete.as_view(), name='delete'),
    path('update/<int:pk>', ListeningUpdate.as_view(), name='update'),

]