from django.db import models
from transformers import pipeline

# Create your models here.
regressor = None
classifier = pipeline("image-classification")
sentiment_analyzer = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")
translator = pipeline("translation_en_to_fr")
text_generator = pipeline("text-generation")
fill_masker = pipeline("fill-mask")
document_q_answerer = pipeline("document-question-answering")
object_detector = pipeline("object-detection")
image_to_texter = pipeline("image-to-text")
mask_generator = pipeline("mask-generation")
automatic_speech_recognizer = pipeline("automatic-speech-recognition")
