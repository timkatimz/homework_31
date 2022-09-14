from rest_framework.generics import ListAPIView, CreateAPIView,\
    UpdateAPIView, DestroyAPIView, RetrieveAPIView

from selection.models import Selection
from selection.serializers import SelectionSerializer, SelectionDetailSerializer, SelectionCreateSerializer, \
    SelectionUpdateSerializer, SelectionDestroySerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDestroySerializer
