from django.shortcuts import render

def profile(request):
    username = request.POST['username']
    password = request.POST['password']
    user=authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect(reverse('profile'))
    else:
        return redirect('index.html')
