from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

from . import util

class NewQueryForm(forms.Form):
    query = forms.CharField(label="query", widget=forms.TextInput({"placeholder": "Search Encyclopedia", "class": "search"}))

def index(request):
    if request.method:
        form: NewQueryForm(request.GET)

        if form.is_valid():
            return HttpResponseRedirect("display/{NewQueryForm.value}")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewQueryForm()
    })

def display(request, title):
    return render(request, "encyclopedia/display.html", {
        "entries": util.get_entry(title)
    })
