# Brick and Mortar Mapping

## Problem Statement

A retail company, Big Box Inc., has several stores located in different cities. The company wants to build a system that can find the closest store to a customer's location, so they hired you, their favorite software engineer. Given the coordinates of each store and the customer's location, the system should find the closest store and return its location. The company holds a queue of customers looking to find the nearest store to them. Your program will take the list of store locations and a list of customers' locations and find the closest store to each customer.

NOTE: Distance should be determined by [Euclidian Distance](https://www.cuemath.com/euclidean-distance-formula/).

## Input Format

The first line contains **n** and **m** separated by a space.

The second line contains **n** x,y pairs separated by spaces representing the coordinates for each store.

The third line contains **m** x,y pairs separated by spaces representing the coordinates for each customer.

## Constraints

$$10 \le n \le $10,000$$
$$1 \le m \le 100$$
$$-10,000 \le x \le 10,000$$
$$-10,000 \le y \le 10,000$$

There will never be a tie. There will never be two stores at the same coordinates. There will never be a customer at the same coordinates as a store.

## Output Format

Output **m** lines, each being the location of the store closest to the $$m_i$$th customer. The format should be x,y.

# Instructions for Problem Writers

Replace all filler with your own information. This is what will go in HackerRank.

Modify mkin.py to print the problem input to the console.

Run genSamples.sh to only generate the inputs for the sample cases. You may want special checks on test number if you want to generate a certain number of very large tests. 

Run runSampleInput.sh to generate sample outputs using your **correct** solution (solutions/sol.py). Make sure these are valid.

Run testgen.sh to generate the remaining test cases. Modify this if you need more/fewer test cases. The cases.zip file is what will be uploaded to HackerRank. 

# Acknowledgements

Special thanks to Colter Boudinot (@Goldenlion5648) for putting together this template.