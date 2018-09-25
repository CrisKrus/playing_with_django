from django.test import TestCase

from code_testing.models import File


class GithubFile(TestCase):
    def test_read_file_content_from_github(self):
        """
        get_content() returns the content of the file
        """

    def test_create_file_from_github(self):
        """
        File(user, repo, path) returns a file with the data
        """
        readme = File(username='criskrus',
                      repository='juego-saber',
                      path='readme')
        self.assertEqual(readme.type(), "file")
