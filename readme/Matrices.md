
# Matrices
Design choices are still being made over the Vec3 and Vec4 classes. Mostly due to graphical rotation matrices supporting both Vec3 and Vec4 classes.
<br />
The matrix module currently consists of three classes, Mat2, Mat3 and Mat4.
<br />
The matrix itself is stored as a flat structure and implemented as row-major. e.g, the matrix,
```
| 0, 1 |
| 2, 3 |
```
is stored as,
```
[0, 1, 2, 3]
```
The current layout is also subject to change due to opengl using column-major matrices (functionality will most likely be put in place to support both matrice layouts).
<br/>
Currently a large number of functions are not implemented, or are only implemented for some classes.


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
    * [Matrix](#matrix)
    * [Load Zero](#load-zero)
    * [Load Identity](#load-identity)
    * [Transpose](#transpose)
    * [Rotate](#rotate)
5. [Mat3 Only Functions](#mat3-only-functions)
    * [Set Value](#set-value)
    * [Translate](#translate)
    * [Scale](#scale)
    * [Share](#share)
    * [Convert 2D](#conver-2d)
6. [Mat4 Only Functions](#mat4-only-functions)
    * [Rotate](#rotate)

## Initalisation
Calling the matrix with out parameters will initalise a zero matrix

```python
>>> pyclid.Mat2()
| 0 0 |
| 0 0 |

>>> pyclid.Mat3()
| 0 0 0 |
| 0 0 0 |
| 0 0 0 |

>>> pyclid.Mat4()
| 0 0 0 0 |
| 0 0 0 0 |
| 0 0 0 0 |
| 0 0 0 0 |

```

Array parameters can be passed in as an array (subject to change)

``` python
>>> pyclid.Mat2([0, 1, 2, 3])
| 0 1 |
| 2 3 |
```
## Standard
### Addition
Addition is applied on an element by element basis
```python
>>> a = pyclid.Mat2([1, 1, 1, 1])
>>> b = pyclid.Mat2([1, 2, 3, 4])
>>> a+b
| 2 3 |
| 4 5 |
```

### Subtraction
```python
>>> a = pyclid.Mat2([1, 2, 3, 4])
>>> b = pyclid.Mat2([1, 1, 1, 1])
>>> a-b
| 0 1 |
| 2 3 |
```
### Multiplication
This can be used with a number, Vec2 or a matrix of the same size.
```python
>>> a = pyclid.Mat2([1, 2, 3, 4])
>>> a*2
| 2 4 |
| 6 8 |
```
Multiplication by a vector must be applied in the correct order. A matrix multiplied by a vector is correct.
``` python
>>> a = pyclid.Mat2([1, 2, 3, 4])
>>> b = pyclid.Vec2(1, 2)
>>> a*b
<5, 11>
```
Multiplication by a matrix must use matrices of the same size
``` python
>>> a = pyclid.Mat2([1, 2, 4, 8])
>>> b = pyclid.Mat2([1, 2, 3, 4])
>>> a*b
|  7 10 |
| 28 40 |
```

### Division
Division can only be used with a number

```python
>>> a = pyclid.Mat2([1, 2, 3, 4])
>>> a/2.0
| 0.5 1.0 |
| 1.5 2.0 |
```
## Comparison
Comparison is performed on an matrix element by element basis

### Equal

```python
>>> a = pyclid.Mat2([1, 2, 3, 4])
>>> b = pyclid.Mat2([1, 2, 3 ,4])
>>> a == b
True
```

### Not Equal
```python
>>> a = pyclid.Mat2([4, 3, 2, 1])
>>> b = pyclid.Mat2([1, 2, 3 ,4])
>>> a != b
True
```

## Extra functionality
### Matrix
Return the current matrix as a flat array (not a function call)
```python
>>> a = pyclid.Mat2([1, 2, 3, 4])
>>> a.matrix
[1, 2, 3, 4]
```

### Load Zero
Sets all elements in the matrix to zero
```python
>>> a = pyclid.Mat2([1, 2, 3 ,4])
>>> a.load_zero()
| 0 0 |
| 0 0 |
```


### Load Identity
Sets the matrix elements to the identity of the matrix

```python
>>> a = pyclid.Mat2([1, 2, 3, 4])
>>> a.load_identity()
| 1 0 |
| 0 1 |
```
### Transpose

``` python
>>> a = pyclid.Mat2([1, 2, 3 4])
>>> a
| 1 2 |
| 3 4 |
>>> a.transpose()
| 1 3 |
| 2 4 |
```

### Rotate
Applies a rotation to the matrix based on an angle (Currently broken in Mat2 and Mat4).
Uses the angle passed in to generate a rotation matrix, which is multiplied to the original matrix
```python
>>> a = Mat3([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a
| 1 2 3 |
| 4 5 6 |
| 7 8 9 |

>>> a.rotate(1.5)
|   2.06572717488 -0.856020583269               3 |
|   5.27042373969  -3.63629393808               6 |
|   8.47512030451  -6.41656729289               9 |
```


## Mat3 only functions
These functions need to be updated to work on Mat2 and Mat4
### Set Value
Sets the value of an element within the matrix. element can be indexed with either by 1D or 2D [x, y].
Takes parameters (value, index)
``` python
>>> a = pyclid.Mat3()
>>> a
| 0 0 0 |
| 0 0 0 |
| 0 0 0 |

>>> a.set_value(1, 1)
>>> a
| 0 1 0 |
| 0 0 0 |
| 0 0 0 |

>>> a.set_value(2, [1, 1])
>>> a
| 0 1 0 |
| 0 2 0 |
| 0 0 0 |
```

### Translate
Translates a matrix by parameters (x, y)
```python
>>> a = pyclid.Mat3([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a
| 1 2 3 |
| 4 5 6 |
| 7 8 9 |

>>> a.translate(1, 0)
|  1  2  4 |
|  4  5 10 |
|  7  8 16 |
```

### Scale
Scales a matrix by parameters (x, y)
``` python
>>> a = pyclid.Mat3([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.scale(2.0, 1.0)
|  2.0  2.0    3 |
|  8.0  5.0    6 |
| 14.0  8.0    9 |
```
### Share
Shares a matrix by parameters (x, y)
``` python
>>> a = pyclid.Mat3([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.share(2.0, 1.0)
|  3.0  4.0    3 |
|  9.0 13.0    6 |
| 15.0 22.0    9 |
```

### Convert 2D
This requires parameters (x, y) and returns the index of the element in 1D for the current matrix
```python
>>> a = pyclid.Mat3([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> a.convert_2d(0, 1)
3
```

## Mat4 Only Functions
### Rotate

The next set of functions apply only to Mat4 (Should also apply to Mat3). These apply rotations about the Euler angles x, y and z.
An angle is supplied to the function (rotate_x, rotate_y, rotate_z depending on the require rotation) and the resulting rotation of the matrix is returned

``` python
>>> a = pyclid.Mat4()
>>> a.load_identity()
| 1 0 0 0 |
| 0 1 0 0 |
| 0 0 1 0 |
| 0 0 0 1 |
>>> a.rotate_x(1.5)
|               1             0.0             0.0               0 |
|               0 0.0707372016677  0.997494986604               0 |
|               0 -0.997494986604 0.0707372016677               0 |
|               0             0.0             0.0               0 |
```
