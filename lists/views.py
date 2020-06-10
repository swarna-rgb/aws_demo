
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import TodoItem,User
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import TodoItem,TodoUser
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileForm
    #CustomEmailValidationForm
#add todo item to the existing user
def add_items_for_an_existing_user(request,user_id):
    existing_user = TodoUser.objects.get(id=user_id)
    TodoItem.objects.create(text=request.POST['item_text'], user=existing_user)
    return redirect(f'/todo/{existing_user.id}/')
#create new todo item
def create_todo_item(request):
    new_user = TodoUser.objects.create()
    TodoItem.objects.create(text=request.POST['item_text'],user=new_user)
    return redirect(f'/todo/{new_user.id}/')

def show_items_for_a_user(request,id):
    user = User.objects.get(id=id)

    user = TodoUser.objects.get(id=id)
    mytodoitems = TodoItem.objects.filter(user=user)
    return render(request, 'list.html', {'todo_items': mytodoitems})

#show all todo items for an user
def show_all_todo_item(request):
    if request.method == 'POST':
        TodoItem.objects.create(text=request.POST['item_text'])
    return render(request, 'list.html', {'todo_items': TodoItem.objects.all()})

def home_page(request):
    return render(request,'home.html')

def start_page(request):
    return render(request, 'start.html')


def register_users_with_profilepic(request):
    if request.method == 'POST':
        ur_form = UserRegisterForm(request.POST)
        p_form = ProfileForm(request.POST,request.FILES)
        if ur_form.is_valid() and p_form.is_valid():
            print(ur_form.cleaned_data.get('username'), "getting username")
            user = ur_form.save()
            print('creating profile for ', user.username, user.id)
            profile = p_form.save(commit=False)
            profile.user = user
            print(request.FILES)
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()
            return redirect('login')
    else:
        ur_form = UserRegisterForm()
        p_form = ProfileForm()
    context = {'ur_form': ur_form, 'p_form': p_form}
    return render(request, 'authsystem/register.html', context)

def register_users(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data.get('username'), "getting username")
            form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'authsystem/register.html',context)

def profile(request):
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if uu_form.is_valid() and pu_form.is_valid():
            uu_form.save()
            pu_form.save()
            return redirect('profile')
    else:
        uu_form = UserUpdateForm(instance=request.user)
        pu_form = ProfileForm(instance=request.user.profile)
    context = {'uu_form': uu_form,
               'pu_form': pu_form}
    return render(request, 'profile.html', context)


def custom_reset_view(request):
        print('custom_reset_view')
        if request.method =='POST':
            print('POST')
            pr_from = PasswordResetForm(request.POST)
            if pr_from.is_valid():
                print(pr_from.cleaned_data)
                uemail = pr_from.cleaned_data.get('email')
                if not AuthUser.objects.filter(email=uemail).exists():
                    #user with valid email and active
                    messages.error(request,
                    f'Your email { uemail } is invalid, '
                                            f'Please enter your registered email id ')

            else:
                messages.error(request, pr_from.errors)
        else:
            pr_from = PasswordResetForm()

        context = {'form':pr_from}
        return render(request, 'authsystem/password_reset.html', context)
