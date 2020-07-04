from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util
import re
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    q = request.POST['q']
    entries = util.list_entries()
    match = []
    for title in entries:
        stitle = title.lower()
        if stitle.find(q) != -1:
            match.append(title)
    
    if not match:
        return render(request, "encyclopedia/apology.html", {
            "message":"Sorry. No results"
        })
    
    return render(request, "encyclopedia/results.html", {
        "entries": match
    })    
    
def create(request):
    return render(request, "encyclopedia/create.html")

def save(request):
    title = request.POST['title']
    content = request.POST['content']
    if util.get_entry(title):
        print("file exists")
        return render(request, "encyclopedia/create.html", {
            "message": "Entry already exists", "title": title, "content": content
    })

    util.save_entry(title, content)
    return HttpResponseRedirect(reverse("entry", args=(title,)))

def entry(request, title):
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/apology.html", {
            "message":"Sorry. Page not found"
        })

    converted_entry = util.convert(entry)
    return render(request, "encyclopedia/entry.html", {
        "entry": converted_entry, "title": title
    })

def edit(request, title):
    if request.method == "POST":
        content = request.POST['content']
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("entry", args=(title,)))
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title, "content": content
        })

def randomentry(request):
    entry = util.list_entries()
    i = random.randint(0, (len(entry)-1))
    randomentry = entry[i]
    return HttpResponseRedirect(reverse('entry', args=(randomentry,)))
