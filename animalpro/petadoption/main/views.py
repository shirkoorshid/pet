from django.shortcuts import render
from .models import Pet

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
