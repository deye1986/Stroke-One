from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Person

#def searchView(request): # MUST USE ONLY ONE
#    allPeople = Person.objects.all()
#    context = {'count' : allPeople.count()}
#    return render(request, 'search.html', context)

def searchView(request): # MUST USE ONLY ONE
    # Limit the number of records and optimize by fetching specific fields as a dictionary
    tenPersonList = Person.objects.values('name', 'description')[:10]  # Fetch only 'name' and 'description' fields
    return render(request, 'search.html', {'person_list': tenPersonList})


def searchResultsView(request):
    query = request.GET.get('search', '')
    print(f'{query = }')

    allPeople = Person.objects.all()
    if query:
        people = allPeople.filter(name__icontains=query)
    else:
        people = []

    context = {'people' : people, 'count' : allPeople.count()}
    return render(request, 'searchResults.html', context)