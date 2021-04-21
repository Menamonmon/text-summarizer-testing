from rest_framework import generics, mixins

from .serializers import DocumentSerializer
from .models import Document


class DocumentsView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, *kwargs)
