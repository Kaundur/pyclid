# Vectors

Design choices are still being made over the Vec3 and Vec4 classes. Mostly due to graphical rotation matrices supporting both Vec3 and Vec4 classes. Currently a large number of function are unimplemented for the Vec4 class.

The vector classes contain parameters x, y, z and w depending on the class, as follows,

```python
Vec2 (x, y)
Vec3 (x, y, z)
Vec4 (x, y, z, w)
```

# Functions
1. [Initalisation](#Initalisation)
2. [Standard](#Standard)
    * [Addition](#Addition)
    * [Subtraction](#Subtraction)
    * [Multiplication](#Multiplication)
    * [Division](#Division)
3. [Comparison](#Comparison)
    * [Equal](#Equal)
    * [Not Equal](#Not Equal)
4. [Extra functionality](#Extra Functionality)
    * [Zero](#Zero)
    * [Distance Between Vectors](#Distance Between Vectors)
    * [Magnitude](#Magnitude)
    * [Normalize](#Normalize)
    * [Cross Product](#Cross Product)
    * [Dot Product](#Dot Product)
    * [Angle Between Vectors](#Angle Between Vectors)
    * [Midpoint Between Vectors](#Midpoint Between Vectors)
    * [Rotate Vector](#Rotate Vector)
    * [Set Vector Rotation](#Set Vector Rotation)
    * [Scalar Triple Product](#Scalar Triple Product)
    * [Vector Triple Product](#Vector Triple Product)




## Initalisation
Calling the vector with not parameters will initalise a vector to zero

``` python
>>> import pyclid
>>> pyclid.Vec2()
<0, 0>
>>> pyclid.Vec3()
<0, 0, 0>
>>> pyclid.Vec4()
<0, 0, 0, 0>
```

Or vectors can be initalised with parameters
``` python
>>> pyclid.Vec2(1, 2)
<1, 2>
>>> pyclid.Vec3(1, 2, 3)
<1, 2, 3>
>>> pyclid.Vec4(1, 2, 3, 4)
<1, 2, 3, 4>
```
## Standard
### Addition
Requires two Vec2 objects,
<br/>
Returns a Vec2 object

```python
>>> v1 = pyclid.Vec2(1, 2)
>>> v2 = pyclid.Vec2(3, 4)
>>> v3 = v1 + v2
>>> print v3
<4, 6>
```

### Subtraction
```python
>>> v1 = pyclid.Vec2(6, 2)
>>> v2 = pyclid.Vec2(1, 2)
>>> v3 = v1-v2
>>> print v3
<5, 0>
```
### Multiplication
Must be used with a scalar value
```python
>>> v = pyclid.Vec2(2, 4)
>>> print v*2
<4, 8>
```
### Division
Must be used with a scalar value
```python
>>> v = pyclid.Vec2(2, 4)
>>> print a/2
<1, 2>
```

## Comparison
Comparison is performed on the same parameters between two vector objects or the same type

### Equal
```python
>>> v1 = pyclid.Vec2(1, 2)
>>> v2 = pyclid.Vec2(1, 2)
>>> v1 == v2
True

>>> v1 = pyclid.Vec2(1, 2)
>>> v2 = pyclid.Vec2(1, 3)
>>> v1 == v2
False
```

### Not Equal

```python
>>> v1 = pyclid.Vec2(1, 1)
>>> v2 = pyclid.Vec2(1, 2)
>>> v1 != v2
True
```

## Extra functionality
### Zero
Sets the vector parameters to zero
```python
>>> v = pyclid.Vec2(1, 2)
>>> v.zero()
<0, 0>
```
### Distance Between Vectors
Find the distance between two vectors using the following equation,
```
distance = sqrt((u.x**2 - v.x**2) + (u.y**2 - v.y**2))
```
```python
>>> a = pyclid.Vec2(0, 0)
>>> b = pyclid.Vec2(1, 1)
>>> a.distance_between(b)
1.4142135623730951
```

### Magnitude
Returns a float of the magnitue of the vector. Note, the abs() operator can be used in place of magnitude

```python
>>> v = pyclid.Vec2(3, 4)
>>> v.magnitude()
5.0
>>> abs(v)
5.0
```

### Normalize
Scales the current vector so that its magnitude is equal to 1.0

```python
>>> v = pyclid.Vec2(3, 4)
>>> v.normalize()
<0.6, 0.8>
```

### Cross Product
Vector cross Product
```python
>>> v = pyclid.Vec2(1, 2)
>>> u = pyclid.Vec2(3, 4)
>>> v.cross(u)
-2
```

### Dot Product
Vector dot product
```python
>>> v = pyclid.Vec2(1, 2)
>>> u = pyclid.Vec2(3, 4)
>>> v.cross(u)
11
```
### Angle Between Vectors
Returns the angle between two vectors using <0, 0> as root
```python
>>> v = pyclid.Vec2(0, 1)
>>> u = pyclid.Vec2(1, 0)
>>> v.angle(u)
1.57079632679
(0, 1)
      |
      |
(0, 0)|_____(1, 0)
```

### Midpoint Between Vectors
Finds the midpoint between two vectors
```python
>>> v = pyclid.Vec2(0, 0)
>>> u = pyclid.Vec2(2, 2)
>>> v.mid_point(u)
<1.0, 1.0>
```
### Rotate Vector (Currently only Vec2)
Rotates a vector about <0, 0>
Accepts an angle or a rotation matrix

If a rotation matrix is used it must be of the form pyclid.Mat2()
```
Matrix
|x1, y1|
|x2, y2|

Vector.x = x1*Vector.x + y1*Vector.y
Vector.y = x2*Vector.x + y2*Vector.y

```
If a float is supplied the roation is calculated based on
```
Vector.x = cos(angle)*Vector.x - sin(angle)*Vector.y
Vector.y = sin(angle)*Vector.x + cos(angle)*Vector.y
```

``` python
>>> # Rotate by 90 deg, note floating point error
>>> v = Vec2(1, 0)
>>> v.rotate(math.pi/2.0)
<6.12323399574e-17, 1.0>
>>> v.rotate(math.pi/2.0)
<-1.0, 1.22464679915e-16>
```

### DO NOT USE - Set Vector Rotation
Similar to rotate, however sets the vector to the applied angle (does not apply a rotation ontop of the current rotation)

Currently a bug in this function


### Scalar Triple Product (Vec3 only)
Requires three Vec3 vectors, result is the dot product of one of the vectors with the cross product of the other two

```
a · (b × c)
```

```python
>>> a = pyclid.Vec3(1, 0, 0)
>>> b = pyclid.Vec3(0, 1, 0)
>>> c = pyclid.Vec3(0, 0, 1)
>>> a.triple_s(b, c)
1
```

### Vector Triple Product (Vec3 only)
Requires three Vec3 vectors, result is the cross product of one of the vectors with the cross product of the other two vectors

```
a × (b × c)
```
``` python
>>> a = Vec3(1, 2, 3)
>>> b = Vec3(2, 3, 1)
>>> c = Vec3(1, 1, 2)
>>> a.triple_v(b, c)
<7, 16, -13>
```
