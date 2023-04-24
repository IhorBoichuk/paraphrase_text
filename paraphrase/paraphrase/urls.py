
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from my_app.views import ParaphraseAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
    path('paraphrase/', ParaphraseAPIView.as_view()),
]
