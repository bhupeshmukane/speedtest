from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.speed_test, name='speed_test'),  # pointing to speed_test view
]
