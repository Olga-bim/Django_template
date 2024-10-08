
from django.contrib import admin
from django.urls import path,include
from base import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index),
    path('register',views.register),
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('students', views.getStudents),
        # path('upload_image/',views.APIViews.as_view()),
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)