from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('add_record', views.addRecord),
    path('delete_record', views.deleteRecord),
    path('edit_record', views.editRecord),
    path('update_record', views.updateRecord),
    path('archive_record', views.archiveRecord),
    path('search_record', views.searchRecord),
    path('share_record', views.shareRecord),
    path('signup/', views.signup),
    path('archive_events', views.archiveEvents),
]
