import csv
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','trainer_project.prod_settings')


import django
django.setup()

from trainer_app.models import *
from django.contrib.auth.models import User

def read_csv_new():
	with open('workout_programs/group2_nov20.csv', newline = '') as f:
		reader = csv.reader(f)

		for row in reader:
			group = Group.objects.get_or_create(group_name=row[1])[0]
			workout = Workout.objects.get_or_create(group=group, workout_number=int(row[0]))[0]
			workout.save()

			unit = Unit.objects.create(times_to_repeat = row[2])

			loop_index = 3
			while not(loop_index > len(row[3:]) + 1) and row[loop_index] != '':
					exercise = Exercise.objects.get_or_create(name = row[loop_index])[0]
					unit.exercises.add(exercise)
					print('exercise: ' + row[loop_index] + '... reps: ' + row[loop_index + 1])
					rep_scheme = Rep_Scheme.objects.create(unit = unit, exercise = exercise, reps = row[loop_index + 1])
					loop_index += 2

			workout.units.add(unit)	

def read_csv_old():
	with open('sample2.csv', newline = '') as f:
		reader = csv.reader(f)
		for row in reader:
			#workout = Workout.objects.get_or_create(id=int(row[0]))[0]
			group = Group.objects.get_or_create(group_name=row[1])[0]
			workout = Workout.objects.get_or_create(group=group, workout_number=int(row[0]))[0]
			workout.save()

			unit = Unit.objects.create()
			for cell in row[2:]:
				if cell != '':
					exercise = Exercise.objects.get_or_create(name = cell)
					unit.exercises.add(exercise[0])
			workout.units.add(unit)

def create_user():
#	group1 = Group.objects.get(group_name='group1')
	group2 = Group.objects.get(group_name='group2')

#	workout1 = Workout.objects.get(group=group1, workout_number=1)
	workout2 = Workout.objects.get(group=group2, workout_number=1)

#	u1 = User(username='Zach', password = 'pass')
#	u1.set_password(u1.password)
#	u1.save()
#	u1 = UserProfile(user = u1, name='Zach', group=group1, current_workout=workout1)
#	u1.save()

	u2 = User(username='Kate', password = 'pass')
	u2.set_password(u2.password)
	u2.save()

	u2 = UserProfile(user=u2, name='Kate', group=group2, current_workout=workout2)
	u2.save()




if __name__ == "__main__":
	read_csv_new()
	create_user()
