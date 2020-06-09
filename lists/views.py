from django.shortcuts import render,redirect
from django.http import  HttpResponse
from .models import TodoItem,TodoUser
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm,UserUpdateForm,ProfileForm
from django.contrib.auth.decorators import login_required
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
    user = TodoUser.objects.get(id=id)
    mytodoitems = TodoItem.objects.filter(user=user)
    return render(request, 'list.html', {'todo_items': mytodoitems})

#show all todo items for an user
@login_required
def show_all_todo_item(request):
    if request.method == 'POST':
        TodoItem.objects.create(text=request.POST['item_text'])
    return render(request, 'list.html', {'todo_items': TodoItem.objects.all()})

@login_required
def home_page(request):
    return render(request,'home.html')

def start_page(request):
    return render(request, 'start.html')

def register_users_with_picture(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            print(user_form.cleaned_data.get('username'), "getting username")
            user = user_form.save()
            profile = profile_form.save(commit=False) # profile is not saved in db
            profile.user = user
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()

    context = {'user_form': user_form,
               'profile_form':profile_form}
    return render(request, 'registration/register.html',context)

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
    return render(request, 'registration/register.html',context)

def profile(request):
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST,instance=request.user)
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
    return render(request, 'profile.html',context )