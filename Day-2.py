# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of the two numbers, also as a string. 
# You must not use any built-in libraries for big integers (like int() or BigInteger) 
# or convert the strings to integers directly. You must simulate multiplication manually, digit by digit. 

# Constraints: 
# ● 1 <= num1.length, num2.length <= 200 
# ● num1 and num2 consist of digits only ('0'–'9') 
# ● num1 and num2 do not contain any leading zeroes, except the number "0" itself 
# ● You may not use int() or eval() to convert strings to integers 

# Input: 
# ● num1: a string representing the first non-negative integer 
# ● num2: a string representing the second non-negative integer 

# Output: 
# ● A string representing the product of num1 and num2 

# Test Case 1: 
# Input: 
# num1 = "123" 
# num2 = "456" 

# Output: 
# product = "56088" 

# Explanation: We simulate multiplication like on paper 
#   1 2 3 
# ×     4 5 6 
# ______________ 
#       7 3 8   (123 × 6) 
#     6 1 5     (123 × 5, shift left by 1) 
#   4 9 2       (123 × 4, shift left by 2) 
# ______________ 
#   5 6 0 8 8 

#code:
num1 = input("enter first number:")
num2 = input("enter second number:")
if num1 == "0" or num2 == "0":
    print("0")
else:
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1)-1,-1,-1):
        for j in range(len(num2)-1,-1,-1):
            d1 = ord(num1[i]) - ord("0")
            d2 = ord(num2[j]) - ord("0")
            mul = d1 * d2

            pos1 = i + j
            pos2 = i + j + 1

            total = mul + result[pos2]
            result[pos2] = total % 10
            result[pos1] += total // 10

    product = ''.join(map(str, result)).lstrip('0')
    print(product)
