from django.shortcuts import render
from django.http import HttpResponse
from .models import RegistrationInformation


def index(request, *args, **kwargs):
    print(request.META['HTTP_HOST'])
    if (request.method == 'GET'):
        return render(request, 'index.html')
    elif (request.method == 'POST'):
        if len(request.POST['Name']) == 0:
            return HttpResponse("姓名不可为空")
        if len(request.POST['Grade']) == 0:
            return HttpResponse("年级不可为空")
        try:
            assert len(request.POST['StuNo']) == 11
            int(request.POST['StuNo'])
        except Exception:
            return HttpResponse("学号格式错误", status=406)

        try:
            assert len(request.POST['CellPhone']) == 11
            int(request.POST['CellPhone'])
        except Exception:
            return HttpResponse("电话号码错误", status=406)

        try:
            RegistrationInformation.objects.create(
                name=str(request.POST['Name']),
                grade=str(request.POST['Grade']),
                stu_no=str(request.POST['StuNo']),
                cellphone=str(request.POST['CellPhone'])
            )
        except Exception:
            return HttpResponse("你已经报名过了哦", status=406)
        return HttpResponse("提交成功", status=201)
