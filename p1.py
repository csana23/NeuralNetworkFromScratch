inputs = [1,2,3]
weights = [0.2,0.8,-0.5]

bias = 2

output = 0

for index, input in enumerate(inputs):
    output = output + (inputs[index]*weights[index]) 

    if index == len(weights)-1:
        output = output + bias

print(output)