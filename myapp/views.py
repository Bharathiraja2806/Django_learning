from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from myapp.models import Post, about_us, Categories
from django.core.paginator import Paginator
from .forms import Contactform, ForgotPasswordForm, register_form, LoginForm, ResetPasswordForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail

# heello = [
#     {"id": 1, "name": "John", "age": 30},
#     {"id": 2, "name": "Jane", "age": 25},
#     {"id": 3, "name": "Bob", "age": 40},
# ]

# Create your views here.
def index(request):
    all_data = Post.objects.all()

    pagionate_data = Paginator(all_data, 5) # Show 5 posts per page

    page_number = request.GET.get('page')

    page_object = pagionate_data.get_page(page_number)

    # logger = logging.getLogger('Testing')
    # logger.debug('summa oru debug message')
    return render(request, "index.html", {"page_object": page_object})

def post(request, id):
    # data = next((item for item in heello if item["id"] == int(id)), None)
    try:
        data = Post.objects.get(slug=id) #either we can give id =  , or pk = id, both are same, but pk (primary key) is more generic, as it can be used for any primary key, not just id
        related_post = Post.objects.filter(category = data.category).exclude(pk=data.id)
        # logger = logging.getLogger('Testing')
        # logger.debug(f"the post variable is {data}")

    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    return render(request, "post.html", {"post" : data, "related_post" : related_post})

def firstpage(request):
    return render(request, 'firstpage.html')

def secondpage(request):
    return render(request, 'secondpage.html')

def samplepage(request):
    return redirect(reverse('myapp:old_monk'))

def new_sample_page(request):
    return HttpResponse('this is a old monk redirect page')

def contact(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')   
        message = request.POST.get('message')
        if form.is_valid():

            logger = logging.getLogger('Testing')
            logger.debug('form data is %s', form.cleaned_data['name'])
            message = 'Your email saved successfully!'
            return render(request, 'contact.html', {'form': form, 'message': message})
        else:
            logger = logging.getLogger('Testing')
            logger.debug('form is not valid')
        return render(request, 'contact.html', {'form': form, 'name': name, 'email': email, 'message': message})
    return render(request, 'contact.html')

def about(request):

    about_content = about_us.objects.first()  # Fetch the first instance of about_us model
    if about_content is None or about_content.content is None:
        default_content = "This is the default about us content."
        return render(request, 'about.html', {'about_content': default_content})
    else:
        about_content = about_us.objects.first()  # Get the content field from the instance
    return render(request, 'about.html', {'about_content': about_content.content})

def register(request):
    form = register_form()
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registeration successful! You can now log in.")
            # message = 'Your email saved successfully!'
            # return render(request, 'register.html', {'form': form, 'message': message})
            return redirect('myapp:login')
  
    return render(request, 'register.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('myapp:dashboard')  # Redirect to a success page after login
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    blog_title = 'My Blog'

    all_data = Post.objects.filter(user=request.user)


    pagionate_data = Paginator(all_data, 5) # Show 5 posts per page

    page_number = request.GET.get('page')

    page_object = pagionate_data.get_page(page_number)

    return render(request, 'dashboard.html', {'blog_title': blog_title, 'page_object':page_object})

def logout(request):
    auth_logout(request)
    return redirect('myapp:index')  # Redirect to the index page after logout

def forgot_password(request):
    form = ForgotPasswordForm()
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            domain = current_site.domain
            subject = "password reset requested"
            message = render_to_string('password_reset_email.html', {'domain': domain, 'uid': uid, 'token': token})
            send_mail(subject, message, 'noreply@gmail.com', [email])
            messages.success(request, "Password reset email sent! Please check your inbox.")
            
    return render(request, 'forgot_password.html', {'form' : form})

def reset_password(request,  uidb64, token):

    form = ResetPasswordForm()

    if request.method == 'POST':

        form = ResetPasswordForm(request.POST)

        if form.is_valid():

            new_password = form.cleaned_data["new_password"]

            try:
                uid = urlsafe_base64_decode(uidb64)
                user = User.objects.get(pk=uid)
            except(ValueError, TypeError, User.DoesNotExist):
                user = None 

            if user is not None and default_token_generator.check_token(user, token):

                user.set_password(new_password)
                user.save()

                messages.success(request, "New password set successfully!")
                return redirect('myapp:login')
            
            else:
                messages.error(request, "Password reset link is invalid!")
            
    return render(request, 'password_reset.html', {'form': form})

def new_post(request):

    categories = Categories.objects.all()

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('myapp:dashboard')

    return render(request, 'new_post.html', {'categories': categories, 'form' : form}) 