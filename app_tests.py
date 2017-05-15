import app
import inspect
import os
import sys
import tempfile
import unittest

from StringIO import StringIO

CURRENT_LOCATION = os.path.dirname(os.path.realpath(sys.argv[0]))
TEST_IMAGE_LOCATION = CURRENT_LOCATION + '/app/static/'


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_get_landing_page(self):
        response = self.app.get(path='/', follow_redirects=True)
        assert b'Image Mirror App' in response.data

    def test_post_to_index(self):
        response = self.app.post(path='/', follow_redirects=True)
        assert response.status_code == 405

    def test_post_to_uploader_without_data(self):
        response = self.app.post(path='/uploader', follow_redirects=True)

        flash_message = b"There has been an error in your image submission."

        assert response.status_code == 200
        assert flash_message in response.data
        assert 'Path=/' in response.headers.get('Set-Cookie')

    def test_post_to_uploader_with_image(self):
        image_filename = '12algorithmseverydatascientistshouldknow.jpg'
        image_location = TEST_IMAGE_LOCATION + image_filename

        with open(image_location, 'rb') as img:
            imgStringIO = StringIO(img.read())
            app_data = {'file': (imgStringIO, 'my_img.jpg')}
            response = self.app.post(path='/uploader',
                                     data=app_data,
                                     follow_redirects=True)

        with open(image_location, 'rb') as img:
            imgStringIO = StringIO(img.read())
            imgStringIO.seek(0)

            assert response.data == imgStringIO.read()
            assert response.status_code == 200

    def test_post_to_uploader_with_wrong_image(self):
        image_filename = '12algorithmseverydatascientistshouldknow.jpg'
        image_location = TEST_IMAGE_LOCATION + image_filename

        other_image_filename = 'profile.jpg'
        other_image_location = TEST_IMAGE_LOCATION + other_image_filename

        with open(image_location, 'rb') as img:
            imgStringIO = StringIO(img.read())
            app_data = {'file': (imgStringIO, 'my_img.jpg')}
            response = self.app.post(path='/uploader',
                                     data=app_data,
                                     follow_redirects=True)

        with open(other_image_location, 'rb') as img:
            imgStringIO = StringIO(img.read())
            imgStringIO.seek(0)

            assert response.data != imgStringIO.read()
            assert response.status_code == 200

    def test_post_to_uploader_with_no_image(self):
        image_filename = '12algorithmseverydatascientistshouldknow.jpg'
        image_location = TEST_IMAGE_LOCATION + image_filename

        with open(image_location, 'rb') as img:
            imgStringIO = StringIO(img.read())
            app_data = {'file': (imgStringIO, '')}
            response = self.app.post(path='/uploader',
                                     data=app_data,
                                     follow_redirects=True)

            flash_message = "Please select an image to upload"
            assert flash_message in response.data

            assert response.status_code == 200
            assert 'Path=/' in response.headers.get('Set-Cookie')

    def test_404_redirect(self):
        path = "this/is/clearly/a/made/up/url"
        response = self.app.get(path=path, follow_redirects=True)

        flash_message = b'that page does not exist'
        assert flash_message in response.data

        assert response.status_code == 200
        assert 'Path=/' in response.headers.get('Set-Cookie')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
