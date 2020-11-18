from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import MapModel
from django.shortcuts import render, get_object_or_404


class maplist(ListView):
    template_name = 'list.html'
    model = MapModel


class maplist_detail(DetailView):
    template_name = 'detail.html'
    model = MapModel


def online_diagnosis(request):
    return render(request, 'online_diagnosis.html')


def blood_donation(request):
    return render(request, 'blood_donation.html')


def book_online(request):
    return render(request, 'book_online.html')


def children_cafeteria(request):
    return render(request, "children_cafeteria.html")


def female_doctor(request):
    return render(request, "female_doctor.html")


def nursing_home(request):
    return render(request, "nursing_home.html")


def resting_place(request):
    return render(request, "resting_place.html")


def library(request):
    return render(request, "library.html")


def sports_center(request):
    return render(request, "sports_center.html")


def post_detail(request, pk):
    post = get_object_or_404(MapModel, id=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_list(request):
    posts = MapModel.objects.filter
    return render(request, 'post_list.html', {'posts': posts})


def list(request):
    posts = MapModel.objects.filter
    return render(request, "list.html", {'posts': posts})


def assistance_dog(request):
    return render(request, "assistance_dog.html")


def citizen_group(request):
    return render(request,"citizen_group.html")


def univercity(request):
    return render(request,"univercity.html")

def municipality(request):
    return render(request,"municipality.html")


def company(request):
    return render(request,"company.html")