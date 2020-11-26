from django.shortcuts import render
from .models import MyTest, ContactInfo

items = MyTest.objects.all()

home_context = {

    'heading': 'WELCOME TO TEAMS',

    'h_desc': 'This is out teams portfolio, here we are leading our projects. Make it short and sweet, but not too '
              'short so folks don\'t simply skip over it entirely. ',

    'data': items
}

about_context = {

    'heading': 'MEET OUR TEAM',
    'h_desc': 'We are all very different. We were born in different cities, at different times, we love different '
              'music, food, movies. But we have something that unites us all. It is our company. We are its heart. We '
              'are not just a team, we are a family. '
}


def home(request):
    return render(request, 'home.html', home_context)


def about(request):
    return render(request, 'about.html', about_context)


def contact(request):
    if request.method == "POST":
        cname = request.POST.get('name')
        cemail = request.POST.get('email')
        ccomment = request.POST.get('comment')

        data = ContactInfo()

        data.name = cname
        data.email = cemail
        data.comment = ccomment

        data.save()

    return render(request, 'contact.html')
