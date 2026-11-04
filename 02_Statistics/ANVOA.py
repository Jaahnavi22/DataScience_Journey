from scipy.stats import f_oneway

# Three groups
group1 = [10, 12, 14, 16]
group2 = [12, 14, 16, 18]
group3 = [20, 22, 24, 26]

# ANOVA hypothesis testing
f_stat, p_value = f_oneway(group1, group2, group3)

print("F-Statistic:", f_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
