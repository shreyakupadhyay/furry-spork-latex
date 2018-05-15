# Circle Detection Module:

To run the circle detection module,

```bash
python DFA/shapes/circle_detection.py /path/to/image
```

**_Note_** : opencv, numpy are dependencies
## Some sample runs: 

1. Perfect test case:

   test/test1.png
   
   ![screenshot 1][test1]

   Here the circles are detected almost perfectly. But the accept state is not detected as 2 circles,
   because the circles are so close to each other.

2. Semi-perfect test case:

   test/test2.png

   ![screenshot 2][test2]

   test/test3.png

   ![screenshot 3][test3]

   test/test4.png

   ![screenshot 4][test4]

   test/test5.png

   ![screenshot 5][test5]

   Here the states are all detected normally (except the accept state). But beyond a certain increase in curvature of arrows
   there are extra circles detected.
   
3. Bad test cases:
   
   test/badtest1

   ![screenshot 6][badtest1]

   test/badtest2
   
   ![screenshot 7][badtest2]

   Here even the states are not detected properly.

I think this can be fixed when arrow detection is done.

The circles which share a common arc with the arrows must be deleted.

[test1]: https://github.com/anirudh-c/furry-spork-latex/blob/dfa-shape-detection/testout/test1.png "Test 1"

[test2]: https://github.com/anirudh-c/furry-spork-latex/blob/dfa-shape-detection/testout/test2.png "Test 2"

[test3]: https://github.com/anirudh-c/furry-spork-latex/blob/dfa-shape-detection/testout/test3.png "Test 3"

[test4]: https://github.com/anirudh-c/furry-spork-latex/blob/dfa-shape-detection/testout/test4.png "Test 4"

[test5]: https://github.com/anirudh-c/furry-spork-latex/blob/dfa-shape-detection/testout/test5.png "Test 5"

[badtest1]: https://github.com/anirudh-c/furry-spork-latex/blob/dfa-shape-detection/testout/badtest1.png "Bad Test 1"

[badtest2]: https://github.com/anirudh-c/furry-spork-latex/blob/dfa-shape-detection/testout/badtest2.png "Bad Test 2"
