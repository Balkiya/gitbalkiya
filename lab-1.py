from functools import reduce

sandar = [4, 7, 10, 5]
f_san = filter(lambda x: x > 1, map(lambda x, idx: x / (idx + 1), sandar, range(len(sandar))))
summa = reduce(lambda x, y: x + y, f_san)

print("берілген сандар:", sandar)
print("1-ден артық сұрыпталған сандар :", summa)
print('Bul Karlygash')
