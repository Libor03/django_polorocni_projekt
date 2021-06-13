from django.shortcuts import render

from django.views import generic
from .models import Type, Animal, Attachment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib.auth.models import User  # Blog author or commenter
from django.shortcuts import get_object_or_404


def index(request):
    """
    View function for home page of site.
    """
    num_animals = Animal.objects.all().count()

    # Do proměnné films se uloží 3 filmy uspořádané podle hodnocení (sestupně)
    animals = Animal.objects.order_by('name')[:3]

    """ Do proměnné context, která je typu slovník (dictionary) uložíme hodnoty obou proměnných """
    context = {
        'num_animals': num_animals,
        'animals': animals
    }
    # Render the HTML template index.html
    return render(
        request,
        'index.html',
        context=context
    )


class AnimalListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = Animal
    paginate_by = 5
    context_object_name = 'animals'


class AnimalDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = Animal
    context_object_name = 'animal'

