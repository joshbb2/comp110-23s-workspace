"""Randomy rolls dice and sums total"""
from random import randint

roll1: int = randint(1,6)
roll2: int = randint(1,6)
roll3: int = randint(1,6)

dice_rolls: list[int] = [roll1, roll2, roll3]
dice_idx: int = 0
dice_sum: int = 0

while dice_idx <= len(dice_rolls) - 1:
    print(dice_rolls[dice_idx])
    dice_sum += dice_rolls[dice_idx]
    dice_idx += 1
print(dice_sum)