from django. urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('',views.homepage,name='homepage'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/<user_id>',views.edit_profile,name='edit_profile'),
    path('all-hoods/', views.hoods, name='hood'),
    path('new-hood/', views.create_new_hood, name='new-hood'),
    path('business/',views.add_business, name='business'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)