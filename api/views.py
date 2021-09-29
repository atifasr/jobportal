import json
from django.http.response import JsonResponse
from job_management.models import *
from django.shortcuts import render
from api.serializers import JobactivitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status


@api_view(['GET'])
def get_applic(request):
    if request.method == 'GET':
        applied_candi = JobPostActivity.objects.filter(
            job_post__creater=request.user)
        serializer_data = JobactivitySerializer(applied_candi, many=True)
        return JsonResponse(serializer_data.data, safe=False)




@api_view(['GET'])
def dashboard_data(request):
    if request.method == 'GET':
        applicants = JobPostActivity.objects.filter(job_post__job_posters = request.user)
        job_posts = JobPost.objects.filter(job_posters = request.user)
        print(job_posts)
        resp = {}
        resp['status'] = 'working'
        return Response(resp,status=status.HTTP_200_OK)