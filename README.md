# unit-convert
Easily convert units to different quantities.

For conveniance, abbreviations are accepted, where an attempt will be made to calculate the type based on the other inputs (eg. "m" can evaluate as either "minute" or "metre").

## Example Usage
```python
>>> from unit_convert import UnitConvert

# Yards + kilometres to miles
>>> UnitConvert(yards=136.23, kilometres=60).miles
37.3597678005

# Bytes to terabytes
>>> UnitConvert(b=19849347813875).tb
18.0528766704

# Nanometres to metres
>>> UnitConvert(nanometres=19849347813875).m
19849.3478139

# Tablespoons to cups
>>> UnitConvert(tablespoons=14).cups
0.875

# Millilitres to cups - most SI/Imperial conversions end up with a lot of decimal places
>>> UnitConvert(ml=7640614).cups
32294.98677
```

Data, time, distance and mass are currently supported.
