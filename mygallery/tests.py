from django.test import TestCase
from .models import Image,Category
# Create your tests here.
  
class CategoryTestClass(TestCase):
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.food= Category(category='food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))

    def tearDown(self):
        '''
        Method to clear the test that has been done on category
        '''
        Category.objects.all().delete()

    def test_save_method(self):
        '''
        Method to save category
        
        '''
        self.food.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        '''
        Method to delete the category
        '''
        self.food.delete_category('food')
        category = Category.objects.all()
        self.assertTrue(len(category)==0)