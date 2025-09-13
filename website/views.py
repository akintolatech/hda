from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "message": "Dreams Transcend various Lifetimes"
    }
    return render(request, 'website/index.html', context)