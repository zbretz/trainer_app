from django.shortcuts import render, redirect
from django.http import HttpResponse
from trainer_app.models import Workout, UserProfile, Unit
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def index(request, completed = 'False'):
	if completed == 'True':
		completed = True
	else:
		completed = False

	user_profile = UserProfile.objects.get(user=request.user)
	workout = user_profile.current_workout
	units = workout.units.all()

	if completed:
		workout_number = user_profile.current_workout.workout_number
		last_workout = Workout.objects.get(group = user_profile.group, workout_number=workout_number - 1)


	#how many exercises are in each unit. to determine the label of each unit ('circuit, superset, solo')
	for unit in units:
		length = len(unit.exercises.all())
		if length == 1:
			unit.type = 'solo'
		elif length == 2:
			unit.type = 'superset'
		else:
			unit.type = 'circuit'

	context_dict = {'units': units, 'workout': workout, 'completed':completed}

	return render(request, 'trainer_app/index3.html', context=context_dict)

def next_workout(request):
	user_profile = request.user.userprofile
	user_profile.last_workout_completed = datetime.now()
	
	workout_number = user_profile.current_workout.workout_number
	user_profile.current_workout = Workout.objects.get(group = user_profile.group, workout_number=workout_number + 1)
	user_profile.save()

	return redirect(reverse('home'))

def home(request):
	user_profile = request.user.userprofile
	workout_number = user_profile.current_workout.workout_number

	next_workout = user_profile.current_workout
	last_workout = Workout.objects.get(group = user_profile.group, workout_number=workout_number - 1)

	ready = True
	#if user_profile.last_workout_completed - datetime.now() > 15:
	#	ready = True
	#else
	#	ready = False

	return render(request, 'trainer_app/home.html', context={'ready': ready,'last_workout':last_workout, 'next_workout':user_profile.current_workout})




	#user_profile = UserProfile.objects.get(name='Zach')

'''
	ready=True

	if ready:
		try:
			user_profile.current_workout = Workout.objects.get(group = user_profile.group, workout_number=workout_number + 1)
			user_profile.save()
		except:
			return HttpResponse('ddfdf')
	else:
		return render(request, 'trainer_app/not_ready.html', context={'last_workout':user_profile.current_workout})

	return redirect(reverse('index'))
'''	



def user_login(request):
	if request.method == "POST":
		username = request.POST.get('name')
		password = request.POST.get('password')

		print(username + password)

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect(reverse('trainer_app:index'))
			else:
				return HttpResponse("Your account is disabled")
		else:
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'trainer_app/login.html')

def log_workout_time(request):
	user_profile = request.user.userprofile
	user_profile.last_workout_completed = datetime.now()
	user_profile.save()
	ready = 'True'
	return HttpResponse(ready)

def time_check(request):
	time = request.user.userprofile.last_workout_completed
	ready='True'
	print('poo')
	return HttpResponse(ready)


@login_required
def user_logout(request):
	logout(request)
	return redirect(reverse('trainer_app:login'))