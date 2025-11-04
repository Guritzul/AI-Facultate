x = [2,1,2]
y = [1,-1,4]

dot_product = sum(a*b for a, b in zip(x, y))
print(dot_product)

vector_length_x = sum(a**2 for a in x)**0.5
vector_length_y = sum(b**2 for b in y)**0.5

print(vector_length_x)
print(vector_length_y)

cosinus_angle = dot_product / (vector_length_x * vector_length_y)
print(cosinus_angle)