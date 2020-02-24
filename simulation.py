from collections import namedtuple
from typing import NamedTuple, Optional
import matplotlib.pyplot as plt
import random
import math

currentBitmons = []

class Bitmon(NamedTuple):
  father: Optional[NamedTuple]
  mother: Optional[NamedTuple]
  gender: str
  nature: int
  variant: str
  purity: int
  h: int
  a: int
  sa: int
  d: int
  sd: int

def clamp(val, mi, ma):
  return max(min(val, ma), mi)

def breedVal(fVal: int, mVal: int, purity: int, minVal: int, maxVal: int):
  rangeVals = (maxVal - minVal) / 20
  return clamp(
    round(
      0.5 * fVal +
      0.5 * mVal +
      random.randint(
        round(-purity / rangeVals),
        round(purity / rangeVals))),
    minVal, maxVal)

def breed(f: Bitmon, m: Bitmon):
  p = (f.purity + m.purity) / 2
  childPurity = p
  if random.random() > 0.5:
    childPurity = max(p - p/10 - 1, 0)
  childVariant = 'normal'
  specialChance = 0.01
  if f.variant == 'special':
    specialChance += 0.05
  elif m.variant == 'special':
    specialChance += 0.05
  if random.random() < specialChance:
    childVariant = 'special'
  elif f.variant == 'ugly' or m.variant == 'ugly' and random.random() < 0.05:
    childVariant = 'ugly'
  return Bitmon(
    father=f,
    mother=m,
    gender=random.choice(['male', 'female']),
    purity=childPurity,
    nature=breedVal(f.nature, m.nature, childPurity, 0, 30),
    h=breedVal(f.h, m.h, childPurity, 0, 100),
    a=breedVal(f.a, m.a, childPurity, 0, 100),
    sa=breedVal(f.sa, m.sa, childPurity, 0, 100),
    d=breedVal(f.d, m.d, childPurity, 0, 100),
    sd=breedVal(f.sd, m.sd, childPurity, 0, 100),
    variant=childVariant
  )

# generate 20 gen-0 bitmons
for i in range(20):
  variantRand = random.random()
  variant = 'normal'
  if variantRand < 0.1:
    variant = 'special'
  elif variantRand < 0.3:
    variant = 'ugly'
  currentBitmons.append(Bitmon(father=None, mother=None, gender=random.choice(['male', 'female']), nature=random.randint(0, 30), variant=variant, purity=100, h=random.randint(0, 100), a=random.randint(0, 100), sa=random.randint(0, 100), d=random.randint(0, 100), sd=random.randint(0, 100)))

# breed bitmons until we have 10000 bitmons
while len(currentBitmons) < 10000:
  father = None
  for b in currentBitmons:
    if b.gender == 'male':
      father = b
      currentBitmons.remove(b)
      break
  mother = None
  for b in currentBitmons:
    if b.gender == 'female':
      mother = b
      currentBitmons.remove(b)
      break
  child = breed(father, mother)
  currentBitmons.append(child)
  currentBitmons.append(father)
  currentBitmons.append(mother)

purities = list(map(lambda b: b.purity, currentBitmons))
natures = list(map(lambda b: b.nature, currentBitmons))
hs = list(map(lambda b: b.h, currentBitmons))
variants = list(map(lambda b: b.variant, currentBitmons))

print(len([x for x in variants if x == 'special']))
print(len([x for x in variants if x == 'ugly']))
print(len([x for x in variants if x == 'normal']))
