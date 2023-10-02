from django.shortcuts import render


# Create your views here.
def hello(request):
    if request.method == 'GET':
        print(request)
    return render(request, 'index.html', {'a':1,'b':3})