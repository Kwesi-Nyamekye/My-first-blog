from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, "Blog/index.html")

def posts(request):
    return

def posts_details(request):
    return