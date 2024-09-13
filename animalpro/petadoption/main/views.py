from django.shortcuts import render, redirect
from .models import Pet
from .models import BlogPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm 
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import ContactForm
from .forms import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def home(request):
    recommended_pets = Pet.objects.all()[:3]  # Example query for recommended pets
    return render(request, 'main/home.html', {'recommended_pets': recommended_pets})

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'templates/admin/pet_list.html', {'pets': pets})

def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'main/pet_detail.html', {'pet': pet})

def adoption_process(request):
    return render(request, 'main/adoption_process.html')

def success_stories(request):
    return render(request, 'main/success_stories.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def resources(request):
    pets = Pet.objects.all()  # Fetch all Pet objects from the database
    context = {'pets': pets}
    return render(request=request, template_name='pet_list.html',context=context)

def blog(request):
    if request.method == 'POST':
        # store it in the DB
      render(request, 'main/blog.html')

def adoption_process(request):
    return render(request, 'adoption_process.html')

def success_stories(request):
    return render(request, 'success_stories.html')

def about_us(request):
    return render(request, 'about_us.html')

def blog(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            from django.utils.timezone import localtime
            now = localtime().date()
            post = BlogPost(title='',
                            content=form.cleaned_data["content"],
                            created_at=now,
                            author=request.user)
            post.save()
    else:
        form = CommentForm()
    return render(request, 'blog.html', {"form": form, "comments": BlogPost.objects.all()})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # או כל דף אחר שתרצה להפנות אליו
        else:
            messages.error(request, 'שם המשתמש או הסיסמה שגויים')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            # התחברות אוטומטית לאחר הרשמה
            login(request, user)
            return redirect('login.html')
    else:
        form = RegisterForm()

    return render(request, 'main/register.html', {'form': form})

def memorial(request):
    pets = [
        {'name': 'סטיופה', 'species': 'חתול'},
        {'name': 'שארק', 'species': 'כלב רועה גרמני'},
        {'name': 'אנדי', 'species': 'כלב'}
    ]
    return render(request, 'memorial.html', {'pets': pets})

def contact(request):
    success = False
    
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        print(f'name = {name}, email = {email}, message={message}')
        
        # Set success to True to show the success message
        success = True
    context = {'success': success}    
    return render(request, 'contact.html', context)
"""
def pet_list(request):
    pets = Pet.objects.all()  # Fetch all Pet objects from the database
    return render(request=request, template_name='C:\\Users\\User\\Desktop\\animalpro\\petadoption\\main\\templates\\pet_list.html', context={'pets': pets})



"""

@login_required
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('blog')  # להפנות לדף הבלוג לאחר הוספת התגובה
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponse('לא מורשה', status=403)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponse('לא מורשה', status=403)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog')
    return render(request, 'confirm_delete_comment.html', {'comment': comment})

