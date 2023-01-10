from django.shortcuts import render

# Create your views here.
def Func1(request):
    return render(request,'User1.html')

def Func2(request):
    return render(request,'User2.html')