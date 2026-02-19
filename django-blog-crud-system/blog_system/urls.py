from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "BlogSys Administration"
admin.site.site_title = "BlogSys Admin Portal"
admin.site.index_title = "Welcome to BlogSys Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
