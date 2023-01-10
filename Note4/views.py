from django.shortcuts import render

# Create your views here.
def parent(request):
    return render(request,'Parent.html')

def child(request):
    return render(request,'Child.html')