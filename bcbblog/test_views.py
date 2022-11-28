from dgango.test import TestCase

class TestViews(TestCase)

    def test_get_PostList(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/base.html')

    def test_get_PostDetail(self):
    