from .views import MetaDataList, MetaDataDetail, UserList
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path


app_name = 'App'
urlpatterns = [
    path('Metadatalist', MetaDataList.as_view(), name="Metadatalist"),
    path('Metadataedit/<int:pk>/', MetaDataDetail.as_view(), name="metadatadetails"),
    path('Metadatalist1', UserList.as_view(), name='userlist')
     ]
urlpatterns = format_suffix_patterns(urlpatterns)