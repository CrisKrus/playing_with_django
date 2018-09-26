from django.shortcuts import render

from .models import GithubFile


def index(request):
    file_content = GithubFile(username='Alienah',
                              repository='saberYganar',
                              path='spec/AppSpec.js').content()
    context = {'file_content': file_content}
    return render(request, 'code_testing/index.html', context)
