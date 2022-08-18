from django.shortcuts import render, redirect
from .forms import userRegisterFrom
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = userRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = userRegisterFrom()

    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')
