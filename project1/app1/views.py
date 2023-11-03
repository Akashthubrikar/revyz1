from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer


class CandidateList(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateCreate(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer




