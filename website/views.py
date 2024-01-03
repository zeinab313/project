from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect
# from website.models import Contact
# from website.forms import ContactForm,NameForm,NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

# def contact_view(request):
#     if request.method=='POST':
#         form= ContactForm(request.POST)
#         if form.is_valid():
#             contact = form.save(commit=False)
#             contact.name = 'anonymous'
#             contact.save()
#             messages.add_message(request,messages.SUCCESS,'save information seccessfully')
#         else:
#             messages.add_message(request,messages.ERROR,'save information not seccessfully')
#     form=ContactForm()
#     return render(request,'website/contact.html',{'form': form})

# def newsletter_view(request):
#     if request.method=='POST':
#         form= NewsletterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponsePermanentRedirect('/')
#     else:
#         return HttpResponsePermanentRedirect('/')