# 1037. Valid Boomerang
# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return true if these points are a boomerang.
# A boomerang is a set of three points that are all distinct and not in a straight line.

points = [[1,1],[2,3],[3,2]]

# Solution
def boomeranger(points):
    if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
        return False
    x1 = points[0][0]
    y1 = points[0][1]
    x2 = points[1][0]
    y2 = points[1][1]
    x3 = points[2][0]
    y3 = points[2][1]
    if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
        return False
    return True

print(boomeranger(points))