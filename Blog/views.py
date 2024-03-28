from django.shortcuts import render
from datetime import date

All_Posts = [
    {
        "slug" : "hike-in-the-mountains",
        "image" : "bm.jpg",
        "author" : "Nyamekye",
        "date" : date(2024, 3, 21),
        "title" : "Mountain Hiking ",
        "excerpt" : " is simply dummy text of the printing and typesetting industry",
        " content" : ''' 
            when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book. 

            It has survived not only five centuries, but also the leap into 
            electronic typesetting, remaining essentially unchanged. It was 
            popularised in the 1960s with the release
            of Letraset sheets containing Lorem Ipsum passages, and more recently 
            '''
    },
    {
        "slug" : "hike-in-the-mountains",
        "image" : "bm.jpg",
        "author" : "Nyamekye",
        "date" : date(2024, 3, 23),
        "title" : "Mountain Hiking ",
        "excerpt" : " is simply dummy text of the printing and typesetting industry",
        " content" : ''' 
            is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever 
            since the 1500s, when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book. '''
    },
    {
        "slug" : "hike-in-the-mountains",
        "image" : "bm.jpg",
        "author" : "Nyamekye",
        "date" : date(2021, 3, 27),
        "title" : "Mountain Hiking ",
        "excerpt" : " is simply dummy text of the printing and typesetting industry",
        " content" : ''' It has survived not only five centuries, but also the leap into 
            electronic typesetting, remaining essentially unchanged. It was 
            popularised in the 1960s with the release
            of Letraset sheets containing Lorem Ipsum passages, and more recently 
            '''
    }
]

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(All_Posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "Blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "Blog/all-posts.html")

def posts_details(request, slug):
    return render(request, "Blog/post-detail.html")