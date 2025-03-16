from django.shortcuts import render
from .models import predict, proba, accuracy, cross_val, X_train, y_train, X_test, y_test

# Create your views here.
def index(request):
    zero = one = two = three = four = five = six = seven = eight = nine = None
    ten = eleven = twelve = thirteen = fourteen = fifteen = sixteen = seventeen = None
    zero_pred = zero_proba = zero_acc = zero_cv = None

    if request.method == "POST":
        zero = request.POST.get("0")
        if zero is not None:
            zero = predict(X_test[0])

            """
            zero_proba = proba(X_test[0])
            zero_acc = accuracy(X_test, y_test)
            zero_cv = cross_val(X_train, y_train)"
            """
            
        one = request.POST.get("1")
        if one is not None:
            one = predict(X_test[1])
        two = request.POST.get("2")
        if two is not None:
            two = predict(X_test[2])
        three = request.POST.get("3")
        if three is not None:
            three = predict(X_test[3])
        four = request.POST.get("4")
        if four is not None:
            four = predict(X_test[4])
        five = request.POST.get("5")
        if five is not None:
            five = predict(X_test[5])
        six = request.POST.get("6")
        if six is not None:
            six = predict(X_test[6])
        seven = request.POST.get("7")
        if seven is not None:
            seven = predict(X_test[7])
        eight = request.POST.get("8")
        if eight is not None:
            eight = predict(X_test[8])
        nine = request.POST.get("9")
        if nine is not None:
            nine = predict(X_test[9])
        ten = request.POST.get("10")
        if ten is not None:
            ten = predict(X_test[10])
        eleven = request.POST.get("11")
        if eleven is not None:
            eleven = predict(X_test[11])
        twelve = request.POST.get("12")
        if twelve is not None:
            twelve = predict(X_test[12])
        thirteen = request.POST.get("13")
        if thirteen is not None:
            thirteen = predict(X_test[13])
        fourteen = request.POST.get("14")
        if fourteen is not None:
            fourteen = predict(X_test[14])
        fifteen = request.POST.get("15")
        if fifteen is not None:
            fifteen = predict(X_test[15])
        sixteen = request.POST.get("16")
        if sixteen is not None:
            sixteen = predict(X_test[16])
        seventeen = request.POST.get("17")
        if seventeen is not None:
            seventeen = predict(X_test[17])


    return render(request, "classification/index.html", {
        "zero_pred": zero,

        """
        "zero_proba": zero_proba,
        "zero_acc": zero_acc,
        "zero_cv": zero_cv,"
        """

        "one": one,
        "two": two,
        "three": three,
        "four": four,
        "five": five,
        "six": six,
        "seven": seven,
        "eight": eight,
        "nine": nine,
        "ten": ten,
        "eleven": eleven,
        "twelve": twelve,
        "thirteen": thirteen,
        "fourteen": fourteen,
        "fifteen": fifteen,
        "sixteen": sixteen,
        "seventeen": seventeen,
    })