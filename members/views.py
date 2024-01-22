from django.http import HttpResponse
from django.template import loader
from .models import Member

from django.shortcuts import render, redirect
from .forms import FileUploadModelForm

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers':mymembers
    }
    return HttpResponse(template.render(context,request))

def details(request,slug):
    mymember = Member.objects.get(slug = slug)
    template = loader.get_template('details.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits':['Apple','Banana','Cherry'],
    }
    return HttpResponse(template.render(context, request))
def upload_file(request):
    if request.method =='POST':
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('success_view')
    else:
        form = FileUploadModelForm()
    template = loader.get_template('fileupload.html')
    context = {
        'form':form
    }
    return HttpResponse(template.render(context,request))
# Create your views here.
