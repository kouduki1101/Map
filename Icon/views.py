from django.shortcuts import render


# Create your views here.
def signupview(request):
    if request.method == 'POST':
        print('POST method')
    else:
        print('GET method probably...')
    return render(request, 'signup.html', {})


def gridview(request):
    return render(request,'grid.html')