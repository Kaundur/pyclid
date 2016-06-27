# Pyclid
A simple mathematics module supporting Vectors, Matrices and Quaternions.

## [Vectors](readme/Vectors.md)
Current available vector classes are the Vec2, Vec3 and Vec4 classes.
See the [vectors](readme/Vectors.md) page for details on class functionality.

``` python
>>> import pyclid
>>> pyclid.Vec2()
<0, 0>
>>> pyclid.Vec3()
<0, 0, 0>
>>> pyclid.Vec4()
<0, 0, 0, 0>
```

## [Matrices](readme/Matrices.md)
Current available matrix classes are the Mat2, Mat3 and Mat4 classes. The classes support standard matrix algebra as well advanced formula used for graphical calculations. Currently the Mat3 and Mat4 are subject to change, since there is still a design decision to be made over their compatibility with Vec3 and Vec4 classes for graphical use (i.e. Vec3 used with a Mat4 rotation matrix). Current functionality can be found on the [matrices](readme/Matrices.md) readme.

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

## [Quaternions](readme/Quaternions.md)
Limited support is currently available for quaternions. Currently there is a single Quaternion class (Quat), and contains four parameters (q0, q1, q2 and q3). Few functions have been added for the quaternion class and is very much a work in progress. Current functionality can be found on the [quaternions](readme/Quaternions.md) readme.

```python
>>> python.Quat()
<0, 0, 0, 0>
```
