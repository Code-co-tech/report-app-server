from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from utils.pagination import PaginationList
from utils.renderers import UserRenderers
from utils.permissions import IsUser

from admin_account.project.views import AdminProjectsSerializer

from prescription.models import Prescriptions, PrescriptionContractor
from prescription.customer.serializers import CustomerPrescriptionsSerializers
from prescription.user_app.serializers import UserPrescriptionsSerializer, UserPrescriptionsUpddateSerializer


class UserPrescriptionsCountView(APIView):
    render_classes = [UserRenderers]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUser]

    @swagger_auto_schema(
        tags=['Prescription User'],
        responses={200: UserPrescriptionsSerializer(many=True)}
    )
    def get(self, request):
        new = PrescriptionContractor.objects.filter(user=request.user, status=1).count()
        fiex = PrescriptionContractor.objects.filter(user=request.user, status=2).count()
        Просрочено = PrescriptionContractor.objects.filter(user=request.user, status=3).count()
        return Response({'new': new, 'fiex':fiex, 'Просрочено':Просрочено}, status=status.HTTP_200_OK)


class UserPrescriptionsView(APIView):
    render_classes = [UserRenderers]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUser]
    pagination_class = PaginationList

    @swagger_auto_schema(
        tags=['Prescription User'],
        responses={200: UserPrescriptionsSerializer(many=True)}
    )
    def get(self, request):
        instance = PrescriptionContractor.objects.filter(user=request.user).order_by('-id')
        # Pagination logic
        paginator = self.pagination_class()
        paginated_instances = paginator.paginate_queryset(instance, request)
        # Serializing paginated data
        serializer = UserPrescriptionsSerializer(paginated_instances, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class UserPrescriptionView(APIView):
    render_classes = [UserRenderers]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUser]

    @swagger_auto_schema(
        tags=['Prescription User'],
        responses={200: AdminProjectsSerializer(many=False)},
    )
    def get(self, request, pk):
        instances = get_object_or_404(PrescriptionContractor, id=pk)
        serializer = AdminProjectsSerializer(instances, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['Prescription User'],
        request_body=UserPrescriptionsUpddateSerializer
    )
    def put(self, request, pk):
        instance = get_object_or_404(PrescriptionContractor, id=pk)
        # Make sure to check that data is not a list, but a dictionary
        serializer = UserPrescriptionsUpddateSerializer(instance=instance, data=request.data, context={'owner':request.user, 'request': request}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)