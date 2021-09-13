from django.urls import path

from . import views

app_name = 'tr_app'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('geomap/', views.map, name='map'),

]
