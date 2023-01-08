from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

# class based views
class TaskListView(ListView):
	model=Task
	template_name="home.html"
	context_object_name='taks'
    
class TaskDetailView(DetailView):
	model=Task
	template_name="detail.html"
	context_object_name='i'

class TaskUpdateView(UpdateView):
	model=Task
	template_name="update.html"
	context_object_name='task'
	fields=('name','priority')
	def get_success_url(self):
		return reverse_lazy('TaskDetailView',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
	model=Task
	template_name="delete.html"
	context_object_name='task'
	success_url=reverse_lazy("TaskListView")





# function based views
def Index(request):
	return render(request,"login.html")


def register(request):
	if request.method=="POST":
		first_name=request.POST.get("first_name")
		# fname=request.POST['first-name']
		last_name=request.POST.get("last_name")
		username=request.POST.get("username")
		email=request.POST.get("email")
		password=request.POST.get("password")
		password2=request.POST.get("password2")
		if password==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"username already taken")
				return redirect(register)
			elif User.objects.filter(email=email).exists():
				messages.info(request,"email already taken")
				return redirect(register)
			else:
				user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
				user.save()
				print("user created")
				return redirect(login)
		else:
			messages.info(request,"password mismatched")
			print("invalid password")
			return redirect(register)
	return render(request,"register.html")

def login(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect(home)
		else:
			messages.info(request,"invalid credentials")
			return redirect(login)
	return render(request,"login.html")


def logout(request):
	auth.logout(request)
	return redirect(Index)




def home(request):
	taks=Task.objects.all()
	if request.method=="POST":
		name=request.POST.get("name")
		priority=request.POST.get("priority")
		date=request.POST.get("date")
		obj=Task(name=name,priority=priority,date=date)
		obj.save()
		return redirect(home)
	return render(request,"home.html",{'taks':taks})

def delete(request,taskid):
	tasks=Task.objects.get(id=taskid)
	tasks.delete()
	return redirect(home)

def edit(request,taskid):
	tasks=Task.objects.get(id=taskid)
	if request.method=="POST":
		name=request.POST.get("name")
		priority=request.POST.get("priority")
		date=request.POST.get("date")
		Task.objects.filter(id=taskid).update(name=name,priority=priority,date=date)
		return redirect(home)
	return render(request,"edit.html",{'tasks':tasks})