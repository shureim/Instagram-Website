from django.test import TestCase
from .models import Image, profile

# Create your tests here.
class ImageTestClass(TestCase):

    #set up method
    def setUp(self):
        self.tarick = Image(Image_name = 'tarick',image_caption = 'tarick',likes = 1, comment = 'tarick')

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tarick,Image))

        # Testing Save Method
    def test_save_method(self):
        self.tarick.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
