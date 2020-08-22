## Disclaimer
>The solution/code included within doesn't give the right answer. The solution is posted here to show one of the possible approach to solve the problem. 

# One of the possibility to solve the problem

For simplicity python was used to try solving the problem

- To manipulate date, **datetime** and **timedelta** was imported from datettime module
- Three functions were used to try solving the problem
  - One to check palindrome 
  - A second function which returns an incremented time of the given input in format **hhhmmss** (i.e. giving input of 000000 returns 000001; for 000059 it return 000100 and so on)
  - The third function uses the above two function to find the solution
  
The code traverse through every second (hhmmss) one by one after checking if it's palindrome in the format (nhhhmmss) .Note: **'n'** is concatenated/added before checking fpr palindrome

Check the comments in the code
// Explanation could be added later here


## Count Palindromes

>This question was asked in zone 2 of codevita 9 (2020)

**Problem Description**

A contest closes in n days hh hours, mm minutes and ss seconds. Given two values of n, how many palindromes of the format nhhmmss would we find in the indicated interval?
A string is said to be palindrome if it reads the same backwards as forwards.

**Constraints**

n2-n1 <= 10

**INPUT**

One line containing two integer nl and n2, where nl <n2

**OUTPUT**

One integer representing the number of palindromes in this countdown interval

**Time Limit**
3

**Examples**
# Example 1
Input

1 2

Output

472

Explanation

We need to check the numbers 1 000000 through 2235959 including only numbers where the last 6 digits correspond to times. We find 472 such numbers: 1000001, 1 001001, 1002001,
1 003001, 1004001 , 2231322, 2232322, 2233322, 2234322, 2235322

# Example 2

Input

0 2

Output

708

Explanation

There are 708 palindromes: 0000000, 0001000, 0002000, 0003000, 0004000, , 2231322, 2232322, 2233322, 2234322, 2235322

