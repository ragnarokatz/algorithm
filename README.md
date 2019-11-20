# algorithm
Some algorithm practise, including sorting, maximum finding, etc.

## problem
Given 2 lists of numbers and a maximum, find the maximum of sum of a number from list1 + a number from list2 that is smaller or equal to the given maximum, as well as the number of occurrences.

## inefficient algorithm
Just bashing with a hammer. Iteratively loops through everything.

## better algorithm
sorts the lists ascending first. Iteration starts with the smallest numbers. It will break the current iteration as soon as the sum exceeds the given maximum.

## even better algorithm
sorts the lists descending first. Iteration starts with the biggest numbers. It will break the current ieration as soon as the sum is smaller than a previously recorded maximum.
