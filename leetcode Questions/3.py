def minT(points):
    output = 0
    for i in range(0, len(points)-1):
        a = abs(points[i+1][0] - points[i][0])
        b = abs(points[i+1][1] - points[i][1])
        output += max(a, b)
    return output
n=int(input("No. of Points = "))
points=[[int(i) for i in input().split()] for j in range(n)]
print(minT(points))