from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
import os

@api_view(['GET', 'POST'])
def api_root(request, format=None):
    base_urls = [
        'https://sturdy-space-giggle-qg77pgg946244gx-8000.app.github.dev/',
        'http://localhost:8000/'
    ]
    return Response({
        'users': [url + 'api/users/' for url in base_urls],
        'teams': [url + 'api/teams/' for url in base_urls],
        'activities': [url + 'api/activities/' for url in base_urls],
        'leaderboard': [url + 'api/leaderboard/' for url in base_urls],
        'workouts': [url + 'api/workouts/' for url in base_urls],
    })

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
