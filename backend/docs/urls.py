from django.urls import path

from .views import DocumentsView

urlpatterns = [path("all/", DocumentsView.as_view())]
