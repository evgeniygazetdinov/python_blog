from django.shortcuts import render
from crm.models import Orders

# Create your views here.
def main_form_view(request):
    return render(request, './index.html')


def thanks_page(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    if name and phone:
        Orders.objects.create(name=name, phone=phone)
    return render(request, './thanks.html', {'phone': phone, 'name': name})
