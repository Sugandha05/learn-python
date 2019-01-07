""" Logical operators are and(even if one is false ans would be false), or(even if one is true ans would be true) , not (opposite would be answer)

Bitwise operator is a lot like logical operator but we work on bit values of a specified number
&     a & b (even if one number is 0 ans would be 0 , also & is & here and not and)
or    a | b (even if one number is 1 ans would be 1)
XOR   a ^ b (output is 1 only if odd numbers of 1 are there)
left shift a << 2 (No. a is leftshifted to 2 position, left shift is bit tricky , simply append no of zeros on the right and you will  get the ans)
right shift a >> 3 (No. a is rightshifted by 3 positions - strinke the numbers on the right and apppend zeros equal to the movement on the left)
"""

a = 5
b = 7

print ("a and b", a & b)
print ("a or b", a | b)
print ("a XOR b", a ^ b)

"""solution
a = 101(5)            
b = 111(7)  """

print ("a is leftshifted by 2 is ", a << 2)   # 101
print ("a is rightshifted by 3 is ", a >> 3)   # 101  0