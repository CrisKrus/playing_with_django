from django.shortcuts import render

from .models import GithubFile


def index(request):
    file_content = GithubFile(username='criskrus',
                              repository='juego-saber',
                              path='readme').content()
    context = {'file_content': file_content}
    return render(request, 'code_testing/index.html', context)
