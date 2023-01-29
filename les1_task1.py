# Задача №1 За день машина проезжает n километров. Сколько дней нужно, чтоюы проехать 
# маршрут длиной m километров? (без if и циклов)

import math

print('Сколько километров проезжает ваша машина за один день? = ', end='')
dist1d = int(input())
print('Сколько километров Вам надо проехать? = ', end='')
needdist = int(input())
result = math.ceil(needdist / dist1d)
print(result)