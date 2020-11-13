from django.urls import path
from .views import home, FormularioContacto, about, products, listar_productos

urlpatterns = [
    path('home/', views.home name="home"),
    path('about/', views.about name="about"),
    path('products/<str:id>/', views.products name="products"),
    path('FormularioContacto/',views.FormularioContacto name="FormularioContacto"),
    path('listar_autos/', listar_productos name="listar_productos")
    
]