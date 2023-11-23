from django.shortcuts import render

# Create your views here.
def munnabhayya(request):
    return render(request,'munnabhayya.html')

def guddubhayya(request):
    return render(request,'guddubhayya.html')