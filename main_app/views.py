from django.shortcuts import render, redirect
from .models import Cat, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView

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
    # Only get the toys the cat does not have
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))

    # toys = Toy.objects.all()  # Fetch all toys
    feeding_form = FeedingForm() # Create an instance of the FeedingForm
    return render(request, 'cats/detail.html', {
        'cat': cat, 
        'feeding_form': feeding_form, 
            # send those toys  
        'toys': toys_cat_doesnt_have 
    })
            # send those toys  

# Define the CatCreate view class
class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/cats/'  # Redirect to the cat index page after creation

    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class CatUpdate(UpdateView):
    model = Cat
    #disallow the renaming of a cat by excluding the name field
    fields = ['breed', 'description', 'age']  

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'  # Redirect to the cat index page after deletion
    # The success_url is the URL to redirect to after a successful delete operation

# Define the add_feeding view function
def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)

# Define the ToyCreate view class
class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    success_url = '/toys/'  # Redirect to the toy index page after creation

# Define the ToyDetail view class
class ToyDetail(DetailView):
    model = Toy
    
# Define the ToyList view class
class ToyList(ListView):
    model = Toy
    
# Define the ToyUpdate view class
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# Define the ToyDelete view class
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'  # Redirect to the toy index page after deletion

# Define the associate_toy view function
def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)

# Define the remove_toy view function
def remove_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect('cat-detail', cat_id=cat_id)


class Home(LoginView):
    template_name = 'home.html'