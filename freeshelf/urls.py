from collection import views
from django.contrib import admin
from django.urls import path, include
from collection.backends import MyRegistrationView
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('books/<slug>/', views.book_detail, name='book_detail'),
]
