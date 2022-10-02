from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm, UserRegisterForm,UserUpdateForm # ResumeUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created do login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form =UserUpdateForm(request.POST,instance=request.user) #we passing instance=request.user so that update karate time already data show ho jaye
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        # r_form=ResumeUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid(): # and r_form.is_valid():
            u_form.save()
            p_form.save()
            # r_form.save()

            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')

    else:
        u_form =UserUpdateForm(instance=request.user) #if user update na bhi kare still we need show the data
        p_form=ProfileUpdateForm(instance=request.user.profile)
        # r_form=ResumeUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form,
        'p_form':p_form,
        # 'r_form':r_form
    }
    return render(request,'users/profile.html',context)
