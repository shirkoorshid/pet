from django.urls import path # type: ignore
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pet_list, name='pet_list'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('adoption-process/', views.adoption_process, name='adoption_process'),
    path('success-stories/', views.success_stories, name='success_stories'),
    path('about-us/', views.about_us, name='about_us'),
    path('resources/', views.resources, name='resources'),
    path('blog/', views.blog, name='blog'),
     path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    
    path('memorial/', views.memorial, name='memorial'),
    
   path('contact/', views.contact_view, name='contact')
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)