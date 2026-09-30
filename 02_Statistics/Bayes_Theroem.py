# BAYES THEOREM

# P(A|B) = P(B|A) * P(A) / P(B)

p_A = 0.01
p_B_given_A = 0.90
p_B = 0.05

p_A_given_B = (p_B_given_A * p_A) / p_B

print(p_A_given_B)
