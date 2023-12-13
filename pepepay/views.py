from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)

        # You can log the user in immediately after registration if needed
        # login(request, user)

        # Redirect to a success page or home page
        return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('login')
            # return render(request, 'login.html', {'error': 'login succcessful'})
        else:
            # Return an error message or render the login page with errors
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')


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