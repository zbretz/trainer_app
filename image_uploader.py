
for file in os.listdir():
	exercise_name = file.split('.')[0]
	try:
		exercise = Exercise.objects.get(name=exercise_name)
		exercise.image = 'exercise_demos/{0}'.format(file)
		exercise.save()
		print('success: ' + exercise_name)
	except Exception as e:
		print(exercise_name)
		print(e)
