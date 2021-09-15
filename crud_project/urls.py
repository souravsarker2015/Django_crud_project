
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_data),
    path('delete/<int:id>/', views.delete,name='delete'),
    path('<int:id>/', views.update,name='updatedata'),
]
