Dear Spotify Anchor Team,

Thanks for this fun little puzzle! Here is my approach to solving this problem:

1. Convert the input string into a hash table where each key is a unique character with a value of the character's frequency in 
the original string.
This required one for-loop to generate and runs in O(n) time.

2. Sort the hash table in ascending order of frequency. 
Using Python's native "sorted" function, this step runs in O(n * log(n)) time.

3. Remove the least frequent characters until we meet our character limit.
Again, only requires one for-loop with simple calculations so O(n) time.

And that's it! The output is a unique set of characters to remove from the original string to cut it down to a specific length. 
Overall time complexity: O(n * log(n)).
Overall space complexity: O(n) (to make the hash table)

Some additional notes thoughts:

- While this program guarantees a unique set of characters to meet the limit, it's always possible that other unique sets exist. 
This simply finds ***one*** posssible solution

- Due to the design of the program, it's very easy to add restrictions to what characters can/can't be removed. If you want to ensure 
that the letter 'a' is not removed, we can simply remove it from the hash table before running the main program. If you want to ensure 'a' is removed, we remove it before running the main program.

- I had originally solved this problem via the Knapsack problem, but upon closer analysis, a dynamic programming solution was not required. 
Using the knapsack problem as an analogy, we can think of the "weight" of each character as the frequency with which it appears in the string, and the "value" of each character as the length it adds to our final set. Since each character has the same length (1), they are all of equal "value"! So all we need to do is add the "lightest" items (i.e. the least frequent characters) to our "knapsack". This can be solved much more clearly with a greedy-type solution.

Thanks again, and I look forward to hearing from you!
 
