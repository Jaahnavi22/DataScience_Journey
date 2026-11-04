# HYPOTHESIS TESTING
# Used to test an assumption about a population.

import scipy.stats as stats

data = [20, 22, 24, 26, 28]

# Null Hypothesis (H0): No significant difference.
# Alternative Hypothesis (H1): Significant difference exists.

t_stat, p_value = stats.ttest_1samp(data, 25)

print("P-value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
else:
    print("Fail to Reject Null Hypothesis")
