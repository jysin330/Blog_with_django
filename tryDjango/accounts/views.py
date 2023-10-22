from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login_view (request):
    # if request.user.is_authenticate:
    #     return render(request,'accounts/already-logged-in.html',{})
    if request.method =="POST":
        username = request.POST.get('username')
        password =request.POST.get('password')
        # remove this
        print(username, password)
        
        user = authenticate(request, username= username, password= password)
        
        if user is None:
            context ={"error": "invalid username or password"}
            return render(request, 'accounts/login.html', context)
        
        print(user)
        login(request,user)
        return redirect('/')
    return render(request, 'accounts/login.html', {})


def logout_view (request):
    if request.method =="POST":
        logout(request)
        return redirect("/login")
    return render(request, 'accounts/logout.html', {})


def register_view (request):
    form = UserCreationForm(request.POST or None)
     
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login.html')
    
    context= {
        'form': form
    }
    
    return render(request, 'accounts/register.html', context)
