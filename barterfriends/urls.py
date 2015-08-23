from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'barterfriends.views.home', name='home'),
    url(r'^about/', 'barterfriends.views.about', name='about'),
    url(r'^register/', 'barterfriends.views.register', name='register'),
    url(r'^barter/', include('barter.urls', namespace='barter')),
    url(r'^collaborate/', include('collaborate.urls', namespace='collaborate')),
    url(r'^do/', include('do.urls', namespace='do')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
]
