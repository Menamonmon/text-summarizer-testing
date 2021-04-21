from rest_framework import generics, mixins

from .serializers import DocumentSerializer
from .models import Document


class CreateDocumentView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = DocumentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DocumentView(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, pk, *args, **kwargs)

    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    def delete(self, request, pk, *args, **kwargs):
        return self.destroy(request, pk, *args, **kwargs)


class ListDocumentsView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
