import unittest


class AppTests(unittest.TestCase):

    def test_file(self):
        with self.app() as client, self.app_context():
            file = {'upload_file': open('image.jpeg', 'rb')}
            response = client.post(
                "/",
                data=file.values(),
                headers={"Content-Type": "multipart/form-data"},
            )
            self.assertEqual(200, response.status_code)
            # self.assertEqual()


if __name__ == '__main__':
    unittest.main()
