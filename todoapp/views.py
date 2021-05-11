from django.shortcuts import render,redirect

from .models import todos
def todo(request):
    todo1=todos.objects.all()
    if request.method=='POST':
        title=request.POST['title']
        new=todos(title=title)
        new.save()
        return redirect("/")
    else:
        return render(request,"todo.html",{'todos':todo1})
def delete(request,id):
    todo1=todos.objects.get(id=id)
    todo1.delete()
    return redirect("/")
    return render(request,"todo.html",{'todos':todo1})