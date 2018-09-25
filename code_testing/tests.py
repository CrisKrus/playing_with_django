from django.test import TestCase

from code_testing.models import GithubFile


# if file don't exists

class GithubFileTest(TestCase):
    def test_read_file_content_from_github(self):
        """
        content() returns the content of the file
        """
        readme = GithubFile(username='criskrus',
                            repository='juego-saber',
                            path='readme')
        # TODO this test is wrong
        self.assertNotEquals(readme.content(), 'irrelevant')

    def test_create_file_from_github(self):
        """
        File(user, repo, path) returns a file with the data
        """
        readme = GithubFile(username='criskrus',
                            repository='juego-saber',
                            path='readme')
        self.assertEqual(readme.type(), "file")

