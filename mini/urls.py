from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('prediction/', include("prediction.urls")),
    path('admin/', admin.site.urls),
]
