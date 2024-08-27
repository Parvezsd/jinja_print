from django.shortcuts import render # type: ignore

# Create your views here.
def jinja_print(request):
    d={'name':'Parvez','age':20}
    return render(request,'jinja_print.html',d)