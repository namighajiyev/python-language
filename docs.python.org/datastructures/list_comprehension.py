squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

squares3 = [x**2 for x in range(10)]
print(squares3)

tuples1 = [ (x,y) for x in [1,2,3,4,5] for y in [1,2,3] if x!=y if x>y]
print(tuples1)

vec = [[1,2,3], [4,5,6], [7,8,9]]

flat = [num for elem in vec for num in elem]
print(flat)