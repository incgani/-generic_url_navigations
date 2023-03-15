from django.shortcuts import render

# Create your views here.
def dubai(request):
    return render(request,'dubai.html')

def maldives(request):
    return render(request,'maldives.html')
