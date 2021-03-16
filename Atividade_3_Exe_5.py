import statistics

#Temps = [-4, -2, 10, 5, 11, 204, -17, 12, 20, 22, -58, 21, 19, 17, 999]
#Temps = [-10, 4, 8, 12, 425, 19, 28, 30, -140, 29]
TempCorrigida = [x for x in temperaturas if -10 <= x <= 100]

print(temperaturas)
print(TempCorrigida)
Media = statistics.mean(TempCorrigida)
print("Média igual a %.1f " % Media)