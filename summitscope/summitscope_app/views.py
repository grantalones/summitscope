from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Mountain



class MountainListView(APIView):
    def get(self, request):
        # Implement logic to fetch mountain data based on location and heading
        mountains = [
        {'name': 'Mount Everest', 'elevation': 8848, 'lat':27.9881, 'lon': 86.9250}, 
        {'name': 'K2', 'elevation': 8611, 'lat':35.8800, 'lon':76.5151}
        ]
        return Response(mountains)



def get_mountains(request):
    # Fetch mountain data from your database or any other source
    mountains = Mountain.objects.all().values('name', 'elevation')
    
    # Convert queryset to list of dictionaries
    mountains_list = list(mountains)

    return JsonResponse(mountains_list, safe=False)
