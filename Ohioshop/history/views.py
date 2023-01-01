from django.shortcuts import render

from .models import Sells

from .forms import UserData
# Create your views here.

def history_form_view(request):
	my_form = UserData()
	if request.method == "POST":
		my_form = UserData(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Sells.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)
	context = {
	    "form"  : my_form
	}
	return render(request, "history/history_form.html", context)