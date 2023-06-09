from django.shortcuts import render,redirect,get_object_or_404
from . import views
from django.http import HttpResponse
from.models  import Crud
from.forms import CrudForm
from django.contrib import messages
# Create your views here.

def index(request):
    
    data=Crud.objects.all()
    if request.method=='POST':
        Slno=request.POST.get('Slno','')
        Itemname=request.POST.get('Itemname','')
        Description=request.POST.get('Description','')
        
        result=Crud(Slno=Slno,Itemname=Itemname,Description=Description)
        result.save()
        messages.info(request, "Data added successfully.")      

        
    return render(request,'index.html',{'data':data})


def delete(request,deleteid):
    data=Crud.objects.get(id=deleteid)
    if request.method=='POST':
        data.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    
    data = get_object_or_404(Crud, id=id)

    if request.method == "POST":
        if (
            request.POST.get("Itemname")
            and request.POST.get("Description")
            and request.POST.get("Slno")
        ):
            Crud.objects.filter(id=id).update(
                Itemname=request.POST.get("Itemname"),
                Description=request.POST.get("Description"),
                Slno=request.POST.get("Slno"),
            )
        return redirect("/")
    messages.success(request, "The item was successfully updated")
    return render(request, "edit.html", {"data": data})
    
    
    