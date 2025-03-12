##Menwuyelet_CSEC_10

s1 = input("")
s2 = input("")
s3 = input("")
 
F = bool(s1 == "scissors" and s2 == s3 == "paper" or s1 == "paper" and s2 == s3 == "rock" or s1 == "rock" and s2 == s3 == "scissors")
M = bool(s2 == "scissors" and s1 == s3 == "paper" or s2 == "paper" and s1 == s3 == "rock" or s2 == "rock" and s1 == s3 == "scissors")
S = bool(s3 == "scissors" and s2 == s1 == "paper" or s3 == "paper" and s2 == s1 == "rock" or s3 == "rock" and s2 == s1 == "scissors")

if F:
    print("F")
elif M:
    print("M")
elif S:
    print("S")
else:
    print("?")