from .views import note_list_view, note_detail_view
from django.urls import path


urlpatterns = [
    path('', note_list_view, name='note_list'),
    path('<int:pk>', note_detail_view, name='note_detail'),
]
