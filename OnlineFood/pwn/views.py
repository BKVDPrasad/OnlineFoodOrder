from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel,StateModel
from django.contrib import messages

def showIndex(request):
    return render(request,"pwn/login.html")


def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get("pwn_password"))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})
    else:
        request.session["admin_status"] = False
        return render(request, "pwn/login.html", {"error": "Admin Logout Success"})



def welcome(request):
    return render(request,"pwn/home.html")


def openState(request):
    sm = StateModel.objects.all()
    return render(request,"pwn/openstate.html",{'data':sm})


def openCity(request):
    return render(request,"pwn/opencity.html")


def openCusine(request):
    return render(request,"pwn/opencuisine.html")


def openVendor(request):
    return render(request,"pwn/openvendor.html")


def openReporsts(request):
    return render(request,"pwn/openreports.html")


def savestate(request):
    StateModel(name=request.POST.get('t1'),photo=request.FILES['t2']).save()
    messages.success(request,'state is saved')
    return openState(request)


def updatestate(request):
    sid = request.GET.get('id')
    print(sid)
    sm = StateModel.objects.get(id=sid)

    return render(request,'pwn/openstate.html',{'udata':sm})


def updatestateid(request):
    StateModel.objects.filter(id=request.GET.get('sid')).update(name=request.POST.get('t1'),photo=request.FILES.get('t2'))
    return redirect('state')


def sdelete(request):
    StateModel.objects.filter(id=request.GET.get('sid')).delete()
    messages.success(request,'state deleted')
    return redirect('state')