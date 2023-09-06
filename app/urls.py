from django.contrib import admin
from django.urls import path,include
from .views  import home,visiter,visiterviewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register('users',visiterviewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("visiter/",visiter,name="visiter"),
    path("visiterapi/",include(router.urls)),
    path("auth/",include("rest_framework.urls"))
]
