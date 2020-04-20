inputs = [1.2,5.1,2.1]
weights = [3.1,2.1,8.7]

bias = 3

output = 0

for index, input in enumerate(inputs):
    output = output + (inputs[index]*weights[index]) 

    if index == len(weights)-1:
        output = output + bias

print(output)