from django.test import SimpleTestCase,TestCase
from .models import *

# Create your tests here.
#agregar diferentes pruebas al archivo test
class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)


#setUpTestData() se llama una vez al comienzo de la ejecución de prueba para la configuración a nivel 
# de clase. Usaría esto para crear objetos que no se modificarán ni cambiarán en ninguno de los métodos 
# de prueba.
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass
#setUp() se llama antes de cada función de prueba para configurar cualquier objeto que pueda 
# ser modificado por la prueba (cada función de prueba obtendrá una versión "nueva" 
# de estos objetos).
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

#creacion de la prueba para ver la creacion o la existencia de un super usario
class SuperUsuarioTestCase(TestCase):
    def setUp(self):
        UsuarioPers.objects.create_superuser(username='ivan', password='',email='ivan_andi@hotmail.com')
    def testUsuario(self):
        usr=UsuarioPers.objects.all()
#creacion de la prueba para ver la creacion o la existencia de un usario
class UsuarioTestCase(TestCase):
    def setUp(self):
        UsuarioPers.objects.create_superuser(username='meliodas', password='',email='andres.pentes2525@gmail.com')
    def testUsuario(self):
        usr=UsuarioPers.objects.all()

 