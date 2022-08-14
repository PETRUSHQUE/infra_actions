from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    """Xd."""
    return HttpResponse('А это вторая страница')
