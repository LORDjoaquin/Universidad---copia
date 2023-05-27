from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path('registrarLibros/',views.registrarLibros),
    path('edicionLibros/<codigo>', views.edicionLibros),
    path('editarLibros/',views.editarLibros),
    path('eliminarLibros/<codigo>',views.eliminarLibros),
    path('contacto/',views.contacto),
    
]