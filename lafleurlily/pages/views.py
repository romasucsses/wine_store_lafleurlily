from django.shortcuts import render


def home_page(request):
    if request == 'GET':
        return render(request, 'pages/index.html')

    if request == 'POST':
        pass

