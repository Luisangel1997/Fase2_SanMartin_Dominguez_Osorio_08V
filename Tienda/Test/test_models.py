from django.test import TestCase
from Productos.models import Productos
from Usuarios.models import Usuarios
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class ProductosModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        imageBasquet = SimpleUploadedFile(name='balon_Nike-110520190504.jpg', content=b'', content_type='img/imgProducto/jpeg')
        imageFutbol = SimpleUploadedFile(name='Balon_Futbol_Adidas-110520195322.jpg', content=b'', content_type='img/imgProducto/jpeg')
        imageRaqueta = SimpleUploadedFile(name='Raqueta_Tenis_Especial_JR-110520192805.jpg', content=b'', content_type='img/imgProducto/jpeg')
        Productos.objects.create(Nombre='Marcelo', descripcion='Productos para hacer deportes', imageBasquet=imageBasquet, imageFutbol=imageFutbol,imagen3=imageRaqueta)

    def test_descripcion_label(self):
        productos=Productos.objects.get(id=1)
        field_label = Productos._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label,'descripcion')

    def test_nombreProductos_label(self):
        productos=Productos.objects.get(id=1)
        field_label = Productos._meta.get_field('nombreProductos').verbose_name
        self.assertEquals(field_label,'nombreProductos')

    def test_nombreProductos_max_length(self):
        productos=Productos.objects.get(id=1)
        max_length = Productos._meta.get_field('nombreProductos').max_length
        self.assertEquals(max_length,30)

    def test_descripcion_max_length(self):
        productos=Productos.objects.get(id=1)
        max_length = Productos._meta.get_field('nombreProductos').max_length
        self.assertEquals(max_length,200)

    def test_object_name_is_last_name_comma_first_name(self):
        productos=Productos.objects.get(id=1)
        expected_object_name = '%s, %s' % (productos.Nombre, productos.descripcion)
        self.assertEquals(expected_object_name,str(productos))

class UsuariosModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Usuarios.objects.create(Nombre='Naruto', Direccion='4 poniente', Email='angel@guzman.com', Telefono="+5698387208" )

    def test_Nombre_label(self):
        usuarios=Usuarios.objects.get(id=1)
        field_label = usuarios._meta.get_field('Nombre').verbose_name
        self.assertEquals(field_label,'Nombre')

    def test_Direccion_label(self):
        usuarios=Usuarios.objects.get(id=1)
        field_label = usuarios._meta.get_field('Direccion').verbose_name
        self.assertEquals(field_label,'Direccion')

    def test_Nombre_max_length(self):
        usuarios=Usuarios.objects.get(id=1)
        max_length = usuarios._meta.get_field('Nombre').max_length
        self.assertEquals(max_length,30)

    def test_Direccion_max_length(self):
        usuarios=Usuarios.objects.get(id=1)
        max_length = usuarios._meta.get_field('Direccion').max_length
        self.assertEquals(max_length,30)

    def test_object_name_is_last_name_comma_first_name(self):
        usuarios=Usuarios.objects.get(id=1)
        expected_object_name = '%s, %s, %s' % (usuarios.Nombre, usuarios.Direccion)
        self.assertEquals(expected_object_name,str(usuarios))