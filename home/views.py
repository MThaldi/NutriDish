from django.shortcuts import render

def nutri_homes(request):
    return render(request, 'home/nutri_home.html', {})

def menu(request):
    return render(request,'home/menu.html',{})

def n_contactus(request):
    return render(request,'home/contactus.html',{})

