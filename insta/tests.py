from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):

    #set up method
    def setUp(self):
        self.tarick = Image(image = "images/4k-wallpaper-abstract-abstract-expressionism-1266808.jpg", image_name = 'tarick',image_caption = 'color image')

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tarick,Image))

        # Testing Save Method
    def test_save_method(self):
        self.tarick.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
