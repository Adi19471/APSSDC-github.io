from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from skills.models import Data

# Create your views here.

# inserting to database 
def boys(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        address = request.POST['address']
        email = request.POST['email']
        message = request.POST['message']

        # print(name,roll)

        Data.objects.create(name=name,roll=roll,address=address,email=email,message=message)
        return HttpResponse('<h1>Succesfully</h1>')
        

    return render(request, 'skills/Alldata.html')

   
# retreving the data from database

def Store_page(request):
    data =Data.objects.all()

    return render(request, 'skills/Storepage_detailes.html',{'data':data})


def Update_page(request,num):
    info = Data.objects.get(id=num)

    if request.method =='POST':
        info.name = request.POST['name']
        info.roll = request.POST['roll']
        info.address = request.POST['address']
        info.email = request.POST['email']
        info.message = request.POST['message']
        info.save()
        return redirect('ss')

        return HttpResponse(("<h2>Now Update is Grant</h2>"))

    return render(request, 'skills/Update_page.html',{'info':info})


def Delet_page(request,num):
    del_rec = Data.objects.get(id=num)

    if request.method =='POST':
        del_rec.delete()
        # return HttpResponse(("<q>Sucessfully Delete what u selected</q>"))
        return redirect('ss')
    return render(request, 'delet_page.html',{'del_rec':del_rec}) 