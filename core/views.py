from django.shortcuts import render

# Create your views here.
def homepage(request):
    """view for homepage"""
    
    context = {}
    return render(request, 'homepage.html', context)
