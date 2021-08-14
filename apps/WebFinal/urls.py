from django.urls import path
from .views import may


urlpatterns = {
    path('', may, name='may'),
}
