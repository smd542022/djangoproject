from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def account(request):
    return render(request,'account.html')


    
def dashboard(request):
    return render(request,'dashboard.html')




def signup(request):
    if request.method == 'POST':

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        Email = request.POST['email']
        password = request.POST['password']
        user =User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname, email=Email)
        print("user created")
        return redirect('/account')
    else:
            return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['Password']

        user = auth.authenticate(username=username, password=Password)
        if user is not None:
         auth.login(request, user)
         print("user is logged in")
         return redirect('/account/dashboard')
         
    else:
            return render(request, 'login.html')

