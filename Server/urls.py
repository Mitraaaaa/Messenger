from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # signup-section
    path('sign_up/' , views.sign_up , name='sign_up'),
    path('create_user/', views.create_user),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)