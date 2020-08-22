## Disclaimer

>The code for this question is not include. Only the approch and algorithm one could use to solve is discussed here

## Solving the problem
# Two agorithm given below will be mainly used to show how the problem could be solved
- Segregate 0s and 1s in an array (https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/)
- Maximum size square sub-matrix with all 1s (https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/)

# All possible combination will calculated to find the largest square tile
- We can rotate the wall any number of time before putting it in furnace. This give 4 possiblity for which side will face the bottom of furnace
- the largest square possible for all side will be calculated 
- By using the segreate algorithm mentioned above ,the melting of bricks and it taking space by good bricks can be simuated
- Further there are two approch to solve this problem
  - we rotate the matrix once ,then segregate and solve for largest square for that posistion OR
  - we assing one side as bottom and the oppsite side as UP ,segregate and  solve for largest square touching the UP side
  
- largest square in matrix could be found by modifying the 2nd algorithm mentioned above
