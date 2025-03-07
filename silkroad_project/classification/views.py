from django.shortcuts import render

# Create your views here.
def index(request):
    name = ""
    if request.method == "POST":
        name = request.POST.get("name")
    return render(request, "classification/index.html", {
        "name": name
    })