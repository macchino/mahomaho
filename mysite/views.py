from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail

from .forms import ContactForm

def index(request):
    language_code = get_language()
    display_text = _('MAHO')
    context = {'display_text': display_text, 'language_code': language_code}

    return render(request, 'index.html', context)

""" お問い合わせフォーム画面"""
def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            myself = form.cleaned_data['myself']
            recipients = [settings.EMAIL_HOST_USER]

            if myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')
            return redirect('mysite:complete')

    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

""" 送信完了画面"""
def complete(request):
    return render(request, 'complete.html')
