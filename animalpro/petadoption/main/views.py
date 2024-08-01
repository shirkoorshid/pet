from django.shortcuts import render, redirect
from .models import Pet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm 
from django.contrib.auth import login, authenticate


from django.http import HttpResponse
from .forms import ContactForm







def home(request):
    recommended_pets = Pet.objects.all()[:3]  # Example query for recommended pets
    return render(request, 'main/home.html', {'recommended_pets': recommended_pets})

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'main/pet_list.html', {'pets': pets})

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
    return render(request, 'main/resources.html')

def blog(request):
    return render(request, 'main/blog.html')

def adoption_process(request):
    return render(request, 'adoption_process.html')

def success_stories(request):
    return render(request, 'success_stories.html')

def about_us(request):
    return render(request, 'about_us.html')

def blog(request):
    return render(request, 'blog.html')


def resources(request):
    
    return render(request, 'resources.html')

def resources(request):
    
    return render(request, 'pet_list.html')

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
            return redirect('home')
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

# views.py
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # טיפול בנתונים, לדוגמה, שמירה בבסיס נתונים או שליחת אימייל
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return HttpResponse('תודה על יצירת הקשר! ההודעה שלך נשלחה בהצלחה.')



