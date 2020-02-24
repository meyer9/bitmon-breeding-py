# Bitmon Breeding Algorithm

Assume `random()` returns a number between 0 and 1. `random(a, b)` returns a random number between a and b inclusive.

```python
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
```

- `bitmonID = random() > 0.3 ? father.bitmonID : mother.bitmonID` - Random deterministic number from father and mother combined
  - also add child number for both mother and father
- `fatherID = father.id`
- `motherID = mother.id`
- `gender = random() > 0.5`
- `purity`
  - `p = (father.purity + mother.purity) / 2`
  - Math.random() > 0.5
    - `purity = max(p - p/10 - 1, 0)`
  - else
    - `purity = p`
- `nature = breedVal(father.nature, mother.nature, purity, 0, 30)`
- `variant`
  - special chance = 1% + 5% if father is special + 5% if mother is special
  - if father or mother is ugly: 5% chance of ugly
  - otherwise normal
- `h = breedVal(father.h, mother.h, childPurity, 0, 100)`
- `a = breedVal(father.a, mother.a, childPurity, 0, 100)`
- `sa = breedVal(father.sa, mother.sa, childPurity, 0, 100)`
- `d = breedVal(father.d, mother.d, childPurity, 0, 100)`
- `sd = breedVal(father.sd, mother.sd, childPurity, 0, 100)`

## Purity Distribution

![purity distribution](purity.png)

## Health/any other stat Distribution

![health distribution](health.png)

## Features

- If you have 2 specials, the chance of a special is 10%.
- Uglies can either be rare or common

