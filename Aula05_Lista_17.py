#Agora conte os dias em que a temperatura ao meio-dia era de pelo menos 20 ℃:

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# A matriz é magicamente atualizada aqui.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "dias estavam quentes.")