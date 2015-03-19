from django.shortcuts import render
from .models import RegistrationInformation


def index(request, *args, **kwargs):
    if (request.method == 'GET'):
        return render(request, 'index.html')
    elif (request.method == 'POST'):
        RegistrationInformation.objects.create(
            name=str(request.POST['Name']),
            grade=str(request.POST['Grade']),
            stu_no=str(request.POST['StuNo']),
            cellphone=str(request.POST['CellPhone'])
        )
