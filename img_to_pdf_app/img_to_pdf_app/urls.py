"""
URL configuration for img_to_pdf_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from . import views
# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# # ---


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from pdf_converter import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_images, name='upload_images'),
    path('pdf_generation_in_progress/', views.pdf_generation_in_progress,
         name='pdf_generation_in_progress'),
    path('get_generated_pdf/', views.get_generated_pdf, name='get_generated_pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)