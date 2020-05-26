from django.test import TestCase
from .models import  Location, Category , Pictures

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_location(self):
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)<1)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category='wallpaper')

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_categories(self):
        self.categories.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)<1)

class PicturesTestClass(TestCase):
    def setUp(self):
        self.picture = Pictures(image='default.jpg',image_name='Rocket',image_description='Rockets are awsome',image_category='space')

    def test_instance(self):
        self.assertTrue(isinstance(self.picture,Pictures))

    def test_save_picture(self):
        self.picture.save_picture()
        pictures = Pictures.objects.all()
        self.assertTrue(len(pictures)>0)

    def test_delete_picture(self):
        self.picture.delete_picture()
        pictures = Pictures.objects.all()
        self.assertTrue(len(pictures)<1)