from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginpage, name="loginhome"),
    path('login/', views.login, name="login"),
    path('register/', views.signup, name = "register"),
    path('logout/', views.logout, name="logout")

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)