from django.shortcuts import render
from .models import Education
from project.forms import HomeForm
# Create your views here.
def index(request):

    form = HomeForm()
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            form=form.save(commit=True)
            return thanks(request)
        else:
            form=HomeForm()
    return render(request,'project/index.html',{'form':form})




def thanks(request):
    return render(request,'project/thanks.html')
