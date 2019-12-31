from django.shortcuts import render, redirect
from django.http import HttpResponse
from trainer_app.models import Workout, UserProfile, Unit, Rep_Scheme, CircuitComplete, Exercise
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

def checker(request):
	time_now = datetime.now().replace(tzinfo=timezone.utc)
	time = request.user.userprofile.last_workout_completed
	print (time_now - time)
	if time_now - time > timedelta(seconds = 15):
		return True
	else:
		return False

@login_required
def current_workout(request):

	if checker(request):

		user_profile = UserProfile.objects.get(user=request.user)
		workout = user_profile.current_workout
		units = workout.units.all()

		#how many exercises are in each unit. to determine the label of each unit ('circuit, superset, solo')
		for unit in units:
			length = len(unit.exercises.all())
			if length == 1:
				unit.type = 'solo'
			elif length == 2:
				unit.type = 'superset'
			else:
				unit.type = 'circuit'

			unit.all_exercises = Rep_Scheme.objects.filter(unit=unit)


		cardio = {'fast': ['12 mins total. On treadmill: 15 seconds at high speed followed by 45 seconds moderate speed. Repeat 12 times.'],
		'smooth':['20min on one of: row, elliptical, treadmill, or stairs'],
		'variety': ['treadmill - 7min max incline walk', 'stairs - 7min', 'elliptical - 7min']}

		#warmup = {'trx':['first', 'second', 'third', 'fourth'], 'barbell': ['one', 'two', 'three'], 'movement': ['first', 'second', 'third', 'fourth'], 'machine':['5 min on elliptical or row']}
		#warmup = [Exercise.objects.get(name=exercise_name) for exercise_name in ['trx', 'barbell', 'machine', 'movement']]
		warmup = Unit.objects.all()[60:64]

		context_dict = {'warmup':warmup, 'cardio': cardio, 'units': units, 'workout': workout, 'completed':False}

		return render(request, 'trainer_app/index3.html', context=context_dict)

	else:
		return redirect(reverse('trainer_app:home'))
		#return render(request, 'trainer_app/home.html', context=context_dict)

@login_required
def last_workout(request):

	user_profile = request.user.userprofile
	workout_number = user_profile.current_workout.workout_number
	try:
		workout = Workout.objects.get(group = user_profile.group, workout_number=workout_number - 1)
		print('good'+ str(workout_number))
	except ObjectDoesNotExist:
		workout = Workout.objects.get(group = user_profile.group, workout_number=workout_number)
		print('or' + str(workout_number))
	print('eeee')
	print(workout_number)

	units = workout.units.all()

		#how many exercises are in each unit. to determine the label of each unit ('circuit, superset, solo')
	for unit in units:
		length = len(unit.exercises.all())
		if length == 1:
			unit.type = 'solo'
		elif length == 2:
			unit.type = 'superset'
		else:
			unit.type = 'circuit'

		unit.all_exercises = Rep_Scheme.objects.filter(unit=unit)
	
	context_dict = {'units': units, 'workout': workout, 'completed':True}

	return render(request, 'trainer_app/index3.html', context=context_dict)


@login_required
def workout_complete(request):
	user_profile = request.user.userprofile
	user_profile.last_workout_completed = datetime.now()
	
	workout_number = user_profile.current_workout.workout_number
	try:
		user_profile.current_workout = Workout.objects.get(group = user_profile.group, workout_number=workout_number + 1)
		print('EXCEPTION: ' + str(user_profile.current_workout.workout_number))
	except Exception as e:
			print('*********' + str(e))
	user_profile.save()

	return redirect(reverse('trainer_app:home'))

@login_required
def home(request):
	user_profile = request.user.userprofile
	workout_number = user_profile.current_workout.workout_number

	next_workout = user_profile.current_workout
	try:
		last_workout = Workout.objects.get(group = user_profile.group, workout_number=workout_number - 1)
		print(user_profile.current_workout.workout_number)

	except:
		last_workout = next_workout
		print(user_profile.current_workout.workout_number)


	ready = checker(request)

	return render(request, 'trainer_app/home.html', context={'ready': ready,'last_workout':last_workout, 'next_workout':next_workout})

def trainer_portal(request):
	clients = User.objects.all()
	for client in clients:
		try:
			last_workout = Workout.objects.get(workout_number = client.userprofile.current_workout.workout_number-1, group = client.userprofile.group)
			client.last_workout = [str(exercise) for unit in last_workout.units.all() for exercise in unit.exercises.all()]
		except:
			client.last_workout = 'has not yet completed first workout'

		current_workout = Workout.objects.get(workout_number = client.userprofile.current_workout.workout_number, group = client.userprofile.group)
		client.current_workout = [str(exercise) for unit in current_workout.units.all() for exercise in unit.exercises.all()]

	return render(request, 'trainer_app/trainer_portal.html', context={'clients': clients})


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
				return redirect(reverse('trainer_app:current_workout'))
			else:
				return HttpResponse("Your account is disabled")
		else:
			return HttpResponse("Invalid login details supplied.")

	else:
		return render(request, 'trainer_app/login.html')

def circuit_complete_tracker(request):
	unit_id = request.GET['unit_id']
	try:
		unit = Unit.objects.get(id=int(unit_id))
	except Unit.DoesNotExist:
		return HttpResponse(-1)
	except ValueError:
		return HttpResponse(-1)

	circuit_complete = CircuitComplete(user = request.user, workout = request.user.userprofile.current_workout,
		unit = unit)
	circuit_complete.save()

	return HttpResponse(str(unit_id) + str(request.user))

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