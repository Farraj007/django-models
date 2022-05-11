from django.urls import path
from .views import SnackListView, SnackDetailView,SnackBaseView

urlpatterns = [
    path('', SnackListView.as_view(), name='Snack_List'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack_detail'),
    path('base', SnackBaseView.as_view(), name='Base View'),
]