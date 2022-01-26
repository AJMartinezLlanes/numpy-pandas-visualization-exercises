# Use the following code for the questions below:

from audioop import avg
from statistics import mean, variance
from turtle import shape
import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 2. How many negative numbers are there?
negative_n = a[a < 0]
print(negative_n)
# 4 negative numbers

# 2. How many positive numbers are there?

positive_n = a [a > 0]
print(positive_n)
# 5 positive numbers

# 3. How many even positive numbers are there?

even_pos_n = positive_n[positive_n % 2 == 0]
print(even_pos_n)
# 3 positive even numbers

# 4. If you were to add 3 to each data point, how many positive numbers would there be?

plus_three = a + 3
pos_plus_3 = plus_three [plus_three>0]
print(pos_plus_3)
# 10 positive numbers after adding 3 to each point

# 5. If you squared each number, what would the new mean and standard deviation be?

squared = a ** 2
mean_sq = squared.mean()
print(mean_sq)
# new mean would be 74
std_sq = squared.std()
print(std_sq)
# new standard deviation is 144.0243035046516

# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

mean_a = a.mean()
centered_a = a - mean_a
print(centered_a.mean())
print(centered_a)


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# Z = x−μ / σ

z = (a - a.mean()) / (a.std())
print(z)

# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# Life w/o numpy to life with numpy
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a/(len(a))
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for n in a: 
    product_of_a *= n
print(product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [n**2 for n in a]
print(squares_of_a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [n for n in a if n % 2 == 0]
print(odds_in_a)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [n for n in a if n % 2 == 1]
print(evens_in_a)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares 
# for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b = np.array(b)
print(b)

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(sum_of_b)

sum_of_b = b.sum()
print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print(min_of_b)

min_of_b = b.min()
print(min_of_b)


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(max_of_b)

max_of_b = b.max()
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(mean_of_b)

mean_of_b = b.mean()
print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
print(product_of_b)

product_of_b = b.prod()
print(product_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
print(squares_of_b)

squares_of_b = np.square(b)
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
print(odds_in_b)

odds_in_b = b[b % 2 == 1]
print(odds_in_b)

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
print(evens_in_b)

evens_in_b = b[b % 2 == 0]
print(evens_in_b)

# Exercise 9 - print out the shape of the array b.
[len(b_len) for b_len in b]

print(b.shape)

# Exercise 10 - transpose the array b.
transpose_of_b = np.transpose(b)
print(transpose_of_b)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
reshape_1by6_b = np.reshape(b,(1,6))
print(reshape_1by6_b)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
reshape_6by1_b = np.reshape(b,(6,1))
print(reshape_6by1_b)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)
print(c)

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = c.min()
print(min_of_c)

max_of_c = c.max()
print(max_of_c)

sum_of_c = c.sum()
print(sum_of_c)

product_of_c = c.prod()
print(product_of_c)

# Exercise 2 - Determine the standard deviation of c.
std_of_c = np.std(c)
print(std_of_c)

# Exercise 3 - Determine the variance of c.
variance_of_c = np.var(c)
print(variance_of_c)

# Exercise 4 - Print out the shape of the array c
shape_of_c = np.shape(c)
print(shape_of_c)

# Exercise 5 - Transpose c and print out transposed result.
transpose_of_c = np.transpose(c)
print(transpose_of_c)

# Exercise 6 - Get the dot product of the array c with c. 
dot_prod_c = np.dot(c, c)
print(dot_prod_c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. 
# Answer should be 261
cxc_trans = transpose_of_c * c
sum_of_cxc_trans = cxc_trans.sum()
print(sum_of_cxc_trans)

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.
product_of_cxc_trans = cxc_trans.prod()
print(product_of_cxc_trans)

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
print(d)

# Exercise 1 - Find the sine of all the numbers in d
sine_of_d = np.sin(d)
print(sine_of_d)

# Exercise 2 - Find the cosine of all the numbers in d
cosine_of_d = np.cos(d)
print(cosine_of_d)

# Exercise 3 - Find the tangent of all the numbers in d
tanget_of_d = np.tan(d)
print(tanget_of_d)

# Exercise 4 - Find all the negative numbers in d
negatives_in_d = d[d < 0]
print(negatives_in_d)

# Exercise 5 - Find all the positive numbers in d
positives_in_d = d[d > 0]
print(positives_in_d)

# Exercise 6 - Return an array of only the unique numbers in d.
unique_n_in_d = np.unique(d)
print(unique_n_in_d)

# Exercise 7 - Determine how many unique numbers there are in d.
len_unique_in_d = len(unique_n_in_d)
print(len_unique_in_d)

# Exercise 8 - Print out the shape of d.
shape_of_d = np.shape(d)
print(shape_of_d)

# Exercise 9 - Transpose and then print out the shape of d.
transpose_of_d = np.transpose(d)
transpose_of_d_shape = np.shape(transpose_of_d)
print(transpose_of_d_shape)

# Exercise 10 - Reshape d into an array of 9 x 2
reshape_9by2_d = np.reshape(d,(9,2))
print(reshape_9by2_d)