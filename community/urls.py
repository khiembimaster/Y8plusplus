from django.urls import path

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
]