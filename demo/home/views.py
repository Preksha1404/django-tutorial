from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]

    context = {
        "peoples": peoples,
        "page": "home",
    }

    return render(request, "index.html", context)

def about(request):
    context={"page":"about"}
    return render(request, "about.html", context)

def contact(request):
    context={"page":"contact"}
    return render(request, "contact.html", context)

def success_page(request):
    return HttpResponse("""<h1>Success! Your operation was completed.</h1>
                        <p>Thank you for using our service.</p>
                        <a href="/">Return to Home Page</a>""")