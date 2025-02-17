from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def homepage_view(request):
    return render(request, 'common/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('homepage')  # Change 'home' to the name of your homepage URL pattern.
        else:
            # Return an 'invalid login' error message.
            return render(request, 'common/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'common/login.html')
    
def user_logout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('homepage')  # Change 'home' to the name of your homepage URL pattern.