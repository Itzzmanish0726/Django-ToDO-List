from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
#here if somebody is at home show index.html 
def home(request):
    context={'success':False}
    if request.method=="POST":
        #Handle the form
        title=request.POST['title']
        desc=request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context={'success':True}
        #if somebody comes with the request.method==post then return the below template
        #but if somebody is saving then below one

    return render(request, 'index.html',context)

def tasks(request):
    allTasks=Task.objects.all() #fetch all the task from task model
   # print(allTasks)
    #for item in allTasks:
    #    print(item.taskDesc)
    context={'tasks': allTasks}
    return render(request, 'tasks.html', context)   