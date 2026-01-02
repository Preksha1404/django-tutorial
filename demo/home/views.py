from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "index.html")

def success_page(request):
    return HttpResponse("""<h1>Success! Your operation was completed.</h1>
                        <p>Thank you for using our service.</p>
                        <a href="/">Return to Home Page</a>""")