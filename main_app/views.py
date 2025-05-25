from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import HttpResponse to send text-based responses
# from django.http import HttpResponse

# Create your views here.

# Define the home view function
def home(request):
    return render(request, 'home.html') # Render the home.html template

def about(request):
    return render(request, 'about.html') # Render the about.html template

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# Create a list of Cat instances

# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

# Define the cat_index view function
def cat_index(request):
    cats = Cat.objects.all() # Get all Cat objects from the database
    return render(request, 'cats/index.html', {'cats': cats}) # Render the index.html template with the list of cats

# Define the cat_detail view function
def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id) # Get the Cat object with the specified ID
    return render(request, 'cats/detail.html', {'cat': cat}) # Render the detail.html template with the selected cat

# Define the CatCreate view class
class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # success_url = '/cats/'  # Redirect to the cat index page after creation