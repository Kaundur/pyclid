# Quaternions

The quaternion class contains parameters q0, q1, q2 and q3

TODO - which one is real

<br/>
Currently the quaternion class is still very much in development, therefore many quaternion operations are missing



# Functions
1. [Initalisation](#initalisation)
2. [Standard](sStandard)
    * [Addition](#addition)
    * [Subtraction](#subtraction)
    * [Multiplication](#multiplication)
    * [Division](#division)
3. [Comparison](#Comparison)
    * [Equal](#Equal)
    * [Not Equal](#not-equal)
4. [Extra functionality](#Extra Functionality)
    * [Magnitude](#Magnitude)
    * [Unit](#Unit)

## Initalisation
Calling the matrix with out parameters will initalise a zero quaternion

```python
>>> pyclid.Quat()
<0, 0, 0, 0>
```
or values can be set by passing in parameters
``` python
>>> pyclid.Quat(1, 2, 3, 4)
<1, 2, 3, 4>
```
## Standard
### Addition
```python
>>> a = pyclid.Quat(1, 2, 3, 4)
>>> b = pyclid.Quat(1, 2, 3, 4)
>>> a+b
<2, 4, 6, 8>
```

### Subtraction
```python
>>> a = pyclid.Quat(4, 4, 4, 4)
>>> b = pyclid.Quat(1, 2, 3, 4)
>>> a-b
<3, 2, 1, 0>
```
### Multiplication
Quaternions can be multiplied by a number or another quaternion

Multiplication by a number
```python
>>> a = pyclid.Quat(1, 2, 3, 4)
>>> a*2
<2, 4, 6, 8>
```

Multiplication by a quaternion
``` python
>>> a = pyclid.Quat(1, 2, 3, 4)
>>> b = pyclid.Quat(1, 2, 3, 4)
>>> a*b
<-28, 4, 6, 8>
```

### Division
Missing

## Comparison
Comparison is performed on an element by element basis between two quaternions
### Equal
```
>>> a = pyclid.Quat(1, 2, 3, 4)
>>> b = pyclid.Quat(1, 2, 3, 4)
>>> a==b
True
```

### Not Equal
```python
>>> a = pyclid.Quat(1, 2, 3, 4)
>>> b = pyclid.Quat(5, 2, 3, 4)
>>> a!=b
True
```

## Extra Functionality
### Magnitude

```python
>>> a = pyclid.Quat(1, 2, 3, 4)
>>> a.magnitude()
5.477225575051661
```

### Unit
Returns the unit quaternion
```python
>>> a = pyclid.Quat(1, 2, 3, 4)
>>> a.unit()
<0.182574185835, 0.36514837167, 0.547722557505, 0.73029674334>
```
