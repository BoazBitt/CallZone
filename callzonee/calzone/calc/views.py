from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
import re

# Create your views here.

def index(request):
    if request.method == 'POST':
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, request.POST.get('email')):
            send_mail('mail from Callzone',
                      'Thank you for subscribing to our site',
                      'CallzoneSCE@gmail.com',
                      [request.POST.get('email')],
                      fail_silently=False)
            return render(request, 'index.html', {'m': 'We sent you an Email'})
        else:
            return render(request, 'index.html', {'m': 'Error, enter correct email format'})
    return render(request, 'index.html',{'m': 'We sent you an Email'})
