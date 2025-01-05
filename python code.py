"""TweetData URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/2.2/topics/http/urls/

Examples:
Function views
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', views.home, name='home')

Class-based views
1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')

Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from admins import views as admins
from TweetData import views as TweetData
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('index/', admins.index, name='index'),
    path('adminlogin/', admins.adminlogin, name='adminlogin'),
    path('adminloginentered/', admins.adminloginentered, name='adminloginentered'),
    path('storecsvdata/', admins.storecsvdata, name='storecsvdata'),
    path('svm/', admins.svm, name='svm'),
    path('NaiveBayes/', admins.NaiveBayes, name='NaiveBayes'),
    path('logout/', admins.logout, name='logout'),
    path('searchahashtags/', TweetData.searchahashtags, name='searchahashtags'),
    path('searchresults/', TweetData.searchresults, name='searchresults'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)