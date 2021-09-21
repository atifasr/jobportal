from django.http.response import JsonResponse
from job_management.models import *
from django.shortcuts import render
from api.serializers import JobactivitySerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_applic(request):
    if request.method == 'GET':
        applied_candi = JobPostActivity.objects.filter(
            job_post__creater=request.user)
        serializer_data = JobactivitySerializer(applied_candi, many=True)
        return JsonResponse(serializer_data.data, safe=False)
