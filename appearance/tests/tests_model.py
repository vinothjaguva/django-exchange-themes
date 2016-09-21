import os
from django.test import TestCase, RequestFactory
from appearance.models import Theme
from django.core.files.uploadedfile import SimpleUploadedFile

test_img = os.path.join(os.path.dirname(__file__), 'test.png')


class ThemeTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.t1 = Theme.objects.create(
            pk=1000,
            name="Test1",
            description="Test Description",
            default_theme=True,
            active_theme=True,
            title="Test Title",
            tagline="Test Tagline",
            running_hex="ffffff",
            running_text_hex="ffffff",
            running_link_hex="ffffff",
            pb_text="Test Powered By Text",
            pb_link="http://boundlessgeo.com/",
            docs_link="/static/docs/index.html",
            background_logo="theme/img/default-background.png",
            primary_logo="theme/img/default-logo.png",
            banner_logo="theme/img/default-banner-icon.png"
        )
        self.t1.save()
        self.t2 = Theme.objects.create(
            pk=1001,
            name="Test2",
            description="Test Description",
            default_theme=False,
            active_theme=True,
            title="Test Title",
            tagline="Test Tagline",
            running_hex="ffffff",
            running_text_hex="ffffff",
            running_link_hex="ffffff",
            pb_text="Test Powered By Text",
            pb_link="http://boundlessgeo.com/",
            docs_link="https://boundlessgeo.github.io/exchange-documentation/",
            background_logo=None,
            primary_logo=None,
            banner_logo=None
        )
        self.t2.save()

    def test(self):
        self.assertEqual(
            self.t1.background_logo_url,
            '/static/theme/img/default-background.png'
        )
        self.assertEqual(
            self.t1.primary_logo_url,
            '/static/theme/img/default-logo.png'
        )
        self.assertEqual(
            self.t1.banner_logo_url,
            '/static/theme/img/default-banner-icon.png'
        )
        self.assertEqual(self.t1.__unicode__(), self.t1.name)
        self.assertEqual(self.t2.background_logo_url, None)
        self.assertEqual(self.t2.primary_logo_url, None)
        self.assertEqual(self.t2.banner_logo_url, None)
        self.t2.background_logo = SimpleUploadedFile(
            name='test2a_delete_me.png',
            content=open(test_img, 'rb').read(),
            content_type='image/png',
        )
        self.t2.primary_logo = SimpleUploadedFile(
            name='test2b_delete_me.png',
            content=open(test_img, 'rb').read(),
            content_type='image/png',
        )
        self.t2.banner_logo = SimpleUploadedFile(
            name='test2c_delete_me.png',
            content=open(test_img, 'rb').read(),
            content_type='image/png',
        )
        self.t2.save()
        self.assertEqual(
            self.t2.background_logo_url,
            '/media/theme/img/test2a_delete_me.png'
        )
        self.assertEqual(
            self.t2.primary_logo_url,
            '/media/theme/img/test2b_delete_me.png'
        )
        self.assertEqual(
            self.t2.banner_logo_url,
            '/media/theme/img/test2c_delete_me.png'
        )
