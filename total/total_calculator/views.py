from django.shortcuts import render 
from django.http import HttpResponse
from  total_calculator.models import Numbers
from django.views.decorators.cache import cache_page


# Create your views here.

def empty_view(request):
    return HttpResponse("Empty View Please go to <a href=""http://127.0.0.1:8000/total""> total </a>")
	
#@cache_page(60 * 10)	 This statement can be used to implement and cache web page for 10 minutes.

# View calculating and populating the total for the range of numbers.
def index(request):
    length=len(Numbers.numbers_to_add)
    total =int((length*(length+1))/2)
    return HttpResponse("totals : {}".format(total)) 
	 