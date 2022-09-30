def evaluación(nota):
	valoración="aprobado"
	if nota<5:
		valoración="Suspenso"
	return valoración

	print (evaluación(4))