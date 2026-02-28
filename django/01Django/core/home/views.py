from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def page(request):
    
    peoples = [
        {"first": "Mark", "last": "Otto", "age": 28},
        {"first": "Jacob", "last": "Thornton", "age": 32},
        {"first": "Larry", "last": "the Bird", "age": 45},
        {"first": "Himanshu", "last": "Kumar", "age": 22},
        {"first": "John", "last": "Doe", "age": 30},
    ]
    
    for people in peoples:
        print(people["first"], people["last"], people["age"])    
    
    return render(request, "home/index.html", context={"peoples": peoples})
    # return HttpResponse("This is a simple page view.")