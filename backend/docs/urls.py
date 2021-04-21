from django.urls import path

from .views import DocumentView, CreateDocumentView, ListDocumentsView

urlpatterns = [
    path("create/", CreateDocumentView.as_view()),
    path("all/", ListDocumentsView.as_view()),
    path("<int:pk>/", DocumentView.as_view()),
]
