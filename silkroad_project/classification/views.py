from django.shortcuts import render

# Create your views here.
def index(request):
    one = None
    two = None
    three = None
    if request.method == "POST":
        one = request.POST.get("1")
        two = request.POST.get("2")
        three = request.POST.get("3")
    return render(request, "classification/index.html", {
        "one": one,
        "two": two,
        "three": three
    })