# Initial list
result = []

# Write your code here
for i in range(1,10):
    if i % 2 == 0:
       result.append(i ** 2)
    else:
        result.append(i)

# Testing
print('Updated list:', result)