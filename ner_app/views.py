from django.shortcuts import render
from django.http import HttpResponse
from .utils import create_test_input_from_text

def home(request):
    return render(request, 'home.html')



def predict(request):
    if request.method == 'POST':
        text = request.POST['text']
        result = create_test_input_from_text(text)
        return render(request, 'predict.html', {'result': result, 'text': text})
    else:
        return HttpResponse("Invalid request")

    
    