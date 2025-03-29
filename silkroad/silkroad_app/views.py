from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
def index(request):
    return render(request, "silkroad_app/index.html")


def regression(request):
    return render(request, "silkroad_app/regression.html")


def classification(request):
    from .models import classifier
    address = ""
    classified = ""
    if request.method == "POST":
        address = request.POST.get("address")
        classified = classifier(address)
    return render(request, "silkroad_app/classification.html", {
        "classified": classified,
    })


def sentiment_analysis(request):
    from .models import sentiment_analyzer
    textarea = ""
    sentiment_analyzed = ""
    if request.method == "POST":
        textarea = request.POST.get("textarea")
        sentiment_analyzed = sentiment_analyzer(textarea)
    return render(request, "silkroad_app/sentiment_analysis.html", {
        "sentiment_analyzed": sentiment_analyzed,
    })


def summarization(request):
    from .models import summarizer
    textarea = ""
    summarized = ""
    if request.method == "POST":
        textarea = request.POST.get("textarea")
        summarized = summarizer(textarea)
    return render(request, "silkroad_app/summarization.html", {
        "summarized": summarized,
    })


def translation(request):
    from .models import translator
    textarea = ""
    translated = ""
    if request.method == "POST":
        textarea = request.POST.get("textarea")
        translated = translator(textarea)
    return render(request, "silkroad_app/translation.html", {
        "translated": translated,
    })


def text_generation(request):
    from .models import text_generator
    textarea = ""
    text_generated = ""
    if request.method == "POST":
        textarea = request.POST.get("textarea")
        text_generated = text_generator(textarea)
    return render(request, "silkroad_app/text_generation.html", {
        "text_generated": text_generated,
    })


def fill_mask(request):
    from .models import fill_masker
    textarea = ""
    fill_masked = ""
    if request.method == "POST":
        textarea = request.POST.get("textarea")
        fill_masked = fill_masker(textarea)
    return render(request, "silkroad_app/fill_mask.html", {
        "fill_masked": fill_masked,
    })


def document_q_a(request):
    from .models import document_q_answerer
    address = ""
    textarea = ""
    document_q_answered = ""
    if request.method == "POST":
        address = request.POST.get("address")
        textarea = request.POST.get("textarea")
        document_q_answered = document_q_answerer(image=address, question=textarea)
    return render(request, "silkroad_app/document_q_a.html", {
        "document_q_answered": document_q_answered,
    })


def object_detection(request):
    from .models import object_detector
    address = ""
    object_detected = ""
    if request.method == "POST":
        address = request.POST.get("address")
        object_detected = object_detector(address)
    return render(request, "silkroad_app/object_detection.html", {
        "object_detected": object_detected,
    })


def image_to_text(request):
    from .models import image_to_texter
    address = ""
    image_to_texted = ""
    if request.method == "POST":
        address = request.POST.get("address")
        image_to_texted = image_to_texter(address)
    return render(request, "silkroad_app/image_to_text.html", {
        "image_to_texted": image_to_texted,
    })


def mask_generation(request):
    from .models import mask_generator
    address = ""
    mask_generated = ""
    if request.method == "POST":
        address = request.POST.get("address")
        mask_generated = mask_generator(address)
    return render(request, "silkroad_app/mask_generation.html", {
        "mask_generated": mask_generated,
    })

def automatic_speech_recognition(request):
    from .models import automatic_speech_recognizer
    address = ""
    automatic_speech_recognized = ""
    if request.method == "POST":
        address = request.POST.get("address")
        automatic_speech_recognized = automatic_speech_recognizer(address)
    return render(request, "silkroad_app/automatic_speech_recognition.html", {
        "automatic_speech_recognized": automatic_speech_recognized,
    })