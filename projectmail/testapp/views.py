from django.shortcuts import render
from .models import Details,Employee
from datetime import date
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def sendmail(r):
    t = date.today()
    obj = Details.objects.filter(event_date__day=t.day, event_date__month=t.month)
    id_data=[]
    for i in obj:
        id_data.append(i.employee_id)
        event_data = i.event_type

        obj1 = Employee.objects.filter(emp_id__in=id_data)
        if obj1.exists():
            for i in obj1:
                mail = i.email_id
            my_subject = 'This mail from django APP'
            if event_data == 'Birthday':
                html_content = render_to_string('testapp/birthday.html')
            else:
                html_content = render_to_string('testapp/welcome.html')
            plain_message = strip_tags(html_content)
            message = EmailMultiAlternatives(
                subject=my_subject,
                body=plain_message,
                from_email='akshaygawande533@example.com',
                to=[mail],
            )
            message.attach_alternative(html_content, 'text/html')
            message.send()
        else:
            return HttpResponse('<h1>Today No Event</h1>')
    return render(r,'testapp/mail.html')



def home(r):
    return render(r,'testapp/home.html')


def register(r):
    if r.method=='POST':
        form = RegisterForm(r.POST)
        if form.is_valid():
            form.save()
            messages.info(r, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = RegisterForm()
    return render(r, 'testapp/register.html', {'form':form})

@login_required
def datalist(r):
    obj = Details.objects.all()
    obj1 = Employee.objects.all()
    return render(r, 'testapp/data.html', {'obj': obj, 'obj1': obj1})
