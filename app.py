input_str = "0101101011101011011101101000111"
output_str = ""

count = 0
for i in range(len(input_str)):
    if input_str[i] == '1':
        count += 1
    else:
        count = 0
        
    if count == 3:
        output_str += '1'
        count = 0
    else:
        output_str += '0'

print(output_str)
