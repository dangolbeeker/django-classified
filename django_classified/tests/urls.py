from django.conf.urls import include, url

urlpatterns = [
    url(r'', include('django_classified.urls', namespace='django_classified')),
    url('accounts/', include('django.contrib.auth.urls')),
]
