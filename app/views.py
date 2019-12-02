from django.shortcuts import render, HttpResponse, redirect
from .models import Record
from .forms import RecordForm, UserForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def frontpage(request):
    user = request.user
    record_form = RecordForm(user=user)
    user_form = UserForm()
    records = Record.objects.filter(user = user, event_type='active')
    return render(request, 'app/index.html', locals())

@login_required
def addRecord(request):
    if request.method == 'POST':
        user = request.user
        form = RecordForm(user,request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = user
            record.event_type = 'active'
            record.save()
    return redirect('/')

@login_required
def deleteRecord(request):
    if request.method == 'POST':
        id = request.POST['delete_val']
        Record.objects.filter(id=id).delete()
    return redirect('/')

@login_required
def editRecord(request):
    if request.method == 'POST':
        id = request.POST['edit_val']
        record = Record.objects.get(id=id)

        return render(request, 'app/edit_record.html', locals())
    return redirect('/')

@login_required
def updateRecord(request):
    if request.method == 'POST':
        user = request.user
        posted_data = request.POST
        id = posted_data['id_val']
        date = posted_data['date']
        title = posted_data['title']
        description = posted_data['description']
        Record.objects.filter(id=id).update(date=date,title=title,description=description)
    return redirect('/')

@login_required
def archiveRecord(request):
    if request.method == 'POST':
        id = request.POST['archive_val']
        Record.objects.filter(id=id).update(event_type='old')
    return redirect('/archive_events')

@login_required
def shareRecord(request):
    if request.method == 'POST':
        id = request.POST['share_val']
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            record = Record.objects.get(id=id)
            Record.objects.create(date=record.date,title=record.title,
                description=record.description, event_type=record.event_type, user=user)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', locals())

@login_required
def archiveEvents(request):
    user = request.user
    records = Record.objects.filter(user = user, event_type='old')
    return render(request, 'app/archive_events.html', locals())

@login_required
def searchRecord(request):
    if request.method == 'POST':
        title = request.POST['title']
        user = request.user
        records = Record.objects.filter(user = user, title=title)
        return render(request, 'app/search_events.html', locals())
    return redirect('/')