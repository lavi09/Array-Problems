# Assignment-4
Array problems

1.Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

2.You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

3.Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

Examples :

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33

Ouptut: Sum found between indexes 2 and 4 

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7

Ouptut: Sum found between indexes 1 and 4 

Input: arr[] = {1, 4}, sum = 0

Output: No subarray found 

4.Given an unsorted array of integers, find a subarray which adds to a given number. If there are more than one subarrays with sum as the given number, print any of them.
Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33

Ouptut: Sum found between indexes 2 and 4 

Input: arr[] = {10, 2, -2, -20, 10}, sum = -10

Ouptut: Sum found between indexes 0 to 3 

Input: arr[] = {-10, 0, 2, -2, -20, 10}, sum = 20

Ouptut: No subarray with given sum exists

5.Write a program to sort an array of 0's,1's and 2's in ascending order.

6.Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an array A:
Example :

Input : A[] = {-7, 1, 5, 2, -4, 3, 0}

Output : 3

3 is an equilibrium index, because:

A[0] + A[1] + A[2]  =  A[4] + A[5] + A[6]

Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n, returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.

7.Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.

8.Given an array and a number k where k is smaller than size of array, we need to find the k’th smallest element in the given array. It is given that ll array elements are distinct.
 

Examples:
Input: arr[] = {7, 10, 4, 3, 20, 15}

       k = 3

Output: 7 

Input: arr[] = {7, 10, 4, 3, 20, 15}

       k = 4

Output: 10 

9.Given a 2D array, print it in spiral form. See the following examples.
Examples:

Input:

        1    2   3   4

        5    6   7   8

        9   10  11  12

        13  14  15  16

Output:

1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

Input:

        1   2   3   4  5   6

        7   8   9  10  11  12

        13  14  15 16  17  18

Output:

1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

10.Print the elements of an array in the decreasing frequency if 2 numbers have same frequency then print the one which came first.
 Examples: 

Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}

Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6} 

Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}

Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}


Video Explanation:
https://www.youtube.com/user/lavanyaboj/videos?view_as=subscriber
