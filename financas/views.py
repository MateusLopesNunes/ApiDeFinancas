from rest_framework import viewsets, generics
from .models import User, Finance
from rest_framework import permissions
from .serializer import UserSerializer, FinanceSerializer, ListFinanceToUserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['salary']
    ordering_fields = ['salary']

class ListFinanceToUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = Finance.objects.filter(user_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListFinanceToUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['receipt_date']

