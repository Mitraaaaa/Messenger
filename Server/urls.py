from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
 
urlpatterns = [
    # TODO assign path
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # signup-section
    path('sign_up/' , views.sign_up , name='sign_up'),
    path('create_user/', views.create_user),

]