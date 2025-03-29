from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("regression", views.regression, name="regression"),
    path("classification", views.classification, name="classification"),
    path("sentiment_analysis", views.sentiment_analysis, name="sentiment_analysis"),
    path("summarization", views.summarization, name="summarization"),
    path("translation", views.translation, name="translation"),
    path("text_generation", views.text_generation, name="text_generation"),
    path("fill_mask", views.fill_mask, name="fill_mask"),
    path("document_q_a", views.document_q_a, name="document_q_a"),
    path("object_detection", views.object_detection, name="object_detection"),
    path("image_to_text", views.image_to_text, name="image_to_text"),
    path("mask_generation", views.mask_generation, name="mask_generation"),
    path("automatic_speech_recognition", views.automatic_speech_recognition, name="automatic_speech_recognition")
]