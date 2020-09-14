from django.urls import path
from multimedia import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.multimedia_index, name='multimedia_index'),
    path("<int:pk>/", views.multimedia_detail, name="multimedia_detail"),

]
