# Circle Detection Module:

To run the circle detection module,

```bash
python DFA/shapes/circle_detection.py /path/to/image
```

**_Note_** : opencv, numpy are dependencies
## Some sample runs: 

1. Perfect test case:

   test/test1.png
   
   Here the circles are detected almost perfectly. But the accept state is not detected as 2 circles,
   because the circles are so close to each other.

2. Semi-perfect test case:

   test/test2.png

   test/test3.png

   test/test4.png

   test/test5.png

   Here the states are all detected normally (except the accept state). But beyond a certain increase in curvature of arrows
   there are extra circles detected.
   
3. Bad test cases:
   
   test/badtest1

   test/badtest2
   
   Here even the states are not detected properly.

I think this can be fixed when arrow detection is done.

The circles which share a common arc with the arrows must be deleted.
