from django.shortcuts import render, redirect
from login_app.forms import RegistrationForm, LoginForm
from login_app.models import User
import bcrypt

# Create your views here.
def index(request):
    regform = RegistrationForm()
    logform = LoginForm()
    context = {
        'regform': regform,
        'loginform': logform, 
    }
    return render(request, 'index.html', context)

def success(request):
    
    return render(request, 'logged_in.html')

#data processing
def register(request):
    request.session.flush()
    unique = True
    password_ok = True
    if request.method == 'POST':
        formData = RegistrationForm(request.POST)
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        if len(User.objects.filter(email=request.POST['email']))>0:
            request.session['duplicate_account'] = "there is already an accout using this email address"
            unique = False
        if not request.POST['password'] == request.POST['confirm_password']:
            request.session['password_match'] = "Passwords do not match"
            password_ok = False
        if formData.is_valid() and password_ok and unique:
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            user1 = User.objects.get(email=request.POST['email'])
            request.session['logged_in'] = "registered"
            request.session['user_id'] = user1.id
            request.session['user_name'] = user1.first_name
            return redirect ('/logged_in')
        # errors={}
        # error=formData.errors
        request.session['errors'] = formData.errors
    return redirect('/')

def check_login(request):
    request.session.flush()
    user1 = User.objects.filter(email=request.POST['email'])
    
    pw = request.POST['password']
    if not len(user1)==1:
        request.session['email'] = "Invalid email address"
    else:
        user1 = user1[0]
        if bcrypt.checkpw(pw.encode(), user1.password.encode()):
            request.session['logged_in'] = 'logged in'
            request.session['user_id'] = user1.id
            request.session['user_name'] = user1.first_name
            return redirect('/logged_in')
        else:
            request.session['pass_match'] = 'Incorrect password'
    return redirect('/')
        
        