"""
Homework #4 for CPTR454.

Problem #4 from section 5.5

Written By Ethan Beaver
"""

from math import sqrt, ceil
import random


def dist(point1, point2):
    """Return the distance between two points."""
    return sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)


def brute_force(P):
    """
    Return the length between the closest pair of points.

    Perform a brute force algorithm to find the closest pair.

    Parameter P is a list of tuples
    """
    closest_length = float("inf")
    for point1 in P:
        for point2 in P:
            d = dist(point1, point2)
            if d < closest_length:
                closest_length = d
    return closest_length


def closest_pair(P, Q):
    """
    Return the length between the closest pair of points.

    Perform the closest pair algorithm described in
    Introduction to the Design and Analysis of Algorithms by Anany Levitin

    Parameters are lists of tuples sorted by x value and then by y value
    """
    n = len(P)
    if n <= 3:
        return brute_force(P)
    else:
        half = ceil(n/2) - 1
        P_l = P[:half]
        Q_l = P_l.copy()
        Q_l.sort(key=lambda tup: tup[1])
        P_r = P[half:]
        Q_r = P_r.copy()
        Q_r.sort(key=lambda tup: tup[1])
        d_l = closest_pair(P_l, Q_l)
        d_r = closest_pair(P_r, Q_r)
        d = min(d_l, d_r)
        m = P[half][0]
        S = []
        for point in Q:
            if abs(point[0] - m) < d:
                S.append(point)
        num = len(S)
        dminsq = d**2
        for i in range(0, num-1):
            k = i + 1
            while k <= num-1 and (S[k][1] - S[i][1])**2 < dminsq:
                dminsq = min(dist(S[i], S[k])**2, dminsq)
                k += 1
        return sqrt(dminsq)


def test_cp(min_x, max_x, min_y, max_y, num_points, num_iterations):
    """Test the above algorithm vs its brute force counterpart."""
    fail_count = 0
    for i in range(0, num_iterations):
        points = [
            (random.randint(min_x, max_x), random.randint(min_y, max_y))
            for x in range(num_points)
        ]
        points_x = points.copy()
        points_x.sort(key=lambda tup: tup[0])
        points_y = points.copy()
        points_y.sort(key=lambda tup: tup[1])
        actual = brute_force(points)
        algorithm = closest_pair(points_x, points_y)
        # print("{} == {}".format(actual, algorithm))
        if actual != algorithm:
            fail_count += 1
            print("{} != {}".format(actual, algorithm))
    print("This algorithm failed {} times out of {}"
          .format(fail_count, num_iterations))


if __name__ == "__main__":
    test_cp(-100, 100, -100, 100, 25, 10000)
