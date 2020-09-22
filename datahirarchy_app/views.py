from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index_view(request):
    if request.user.id:
        print()
        folder = models.Folder.objects.filter(author__id=request.user.id)
    else:
        folder = models.Folder.objects.all()
    return render(request, "index.html", {'folder': folder})
@login_required
def create_view(request):
    if request.method == 'POST':
        form = forms.FolderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data   
            login_author  = models.Author.objects.filter(user__id=request.user.id).first()     
            new_folder = models.Folder.objects.create(
                name = data['name'],
                parent = data['parent'] ,
                author =  login_author         
                )
            if new_folder:
                return HttpResponseRedirect(reverse('homepage')) 
                

    form = forms.FolderForm()
    return render(request,'create.html',{'form':form})

def login_view(request):
    if request.method == "POST":
    
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data.get('username'),password=data.get('password'))

            if user is not None:
                
                login(request,user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
                
                        
    form = forms.LoginForm()
    return render (request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('homepage')