#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

# Rules for Random Variables, Regression & Correlation, Moments Skewness & Kurtosis
RVK_RULES = [
    # Random Variables
    (r'if x is a discrete random variable.*function.*f\s*\(\s*x\s*\)', 'a probability function'),
    (r'f\s*\(\s*x\s*\).*if x is a discrete random variable', 'a probability function'),
    (r'calculate p\(x<2\)', '4/8'),
    (r'normal distribution m\.d\.\s*=', '0.7979σ'),
    (r'expected value of a random variable is equal to', 'mean'),
    (r'in normal distribution β2', '3'),
    (r'hyper geometric random variable', 'discrete variable'),
    (r'poisson.*mean value is', '2'),
    (r'parameters of the binomial distribution', 'n&p'),
    (r'normal distribution.*b2.*moment ratio', 'equal to 3'),
    (r'set of possible values that a random variable can assume and their associated probabilities', 'probability distribution'),
    (r'mean deviation of the normal distribution', '4/5 of the s.d'),
    (r'expected value of the normal distribution', ''), # mu

    # Regression & Correlation
    (r'values fall on the same straight line and the line has a positive slope', 'r = +1'),
    (r'correlation coefficient will be zero if', 'slope b = 0'),
    (r'consider in simple correlation analysis', 'strength of the association between two variables'),
    (r'regression line y=\s*a\s*\+\s*bx\+\s*€.*non-random', 'x'),
    (r'variable plotted on the horizontal or x-axis in a scatter diagram', 'independent variable'),
    (r'correlation of coefficient lies between', '- 1 to +1'),
    (r'scatter diagram the variable plotted along y-axis', 'dependent variable'),
    (r'linear regression, y=\s*a\+bx\s*,.*variable “y” will always', 'a random variable'),
    (r'linear regression, y=\s*a\+bx\s*,.*variable “x” will always', 'a non-random variable'),
    (r'in regression line y=\s*a\+bx\s*,\s*x is called', 'independent variable'),
    (r'best fitted line is obtained through', 'method of least square'),
    (r'var\s*\(x-y\)', 'var(x) + var(y)'),
    (r'scatter diagram we plot', 'x and y'),
    (r'plotted on the vertical or y-axis in a scatter diagram', 'dependent variable'),
    (r'could not represent a coefficient of correlation', 'r=1.09'),
    (r'ŷ is the predicted value.*regression line', 'ŷ = mx + b, where m = slope'),
    (r'intercept parameter is equal to zero', 'regression line will pass through the origin'),
    (r'intercept parameter is equal to 0', 'regression line will pass through the origin'),
    (r'e\s*\(xy\)', 'e(x).e(y)'),
    (r'degree of scatter of the observed values about the regression line', 'standard error of estimate'),
    (r'regression line y\^=\s*2\+\s*0\.3x', 'relationship between x and y is positive'),
    (r'values of variables are increasing or decreasing in the same direction', 'positive correlation'),
    (r'correlation coefficient of \.75', 'strong positive'),
    (r'strength of the association between x and y is very weak', 'r = 0'),
    (r'graph is very much scattered.*value of r', 'r = 0.1'),
    (r'when there is no correlation then', 'r=0'),
    (r'in regression line y=a\+bx, y is called', 'dependent variable'),
    (r'correlation coefficient measures', 'degree of linear relationship between two random variables'),
    (r'sum of square of the vertical distance between two points and fitted line is always', 'minimum'),
    (r'scatter diagram is expressed as', 'curve'), # or points/dots

    # Moments, Skewness, Kurtosis
    (r'first moment about origin is always', 'mean'),
    (r'mesokurtic.*b2', 'equal to 3'),
    (r'third moment about mean is zero', 'symmetrical'),
    (r'platykurtic.*b2', 'less than 3'),
    (r'leptokurtic.*b2', 'greater than 3'),
    (r'fourth moment about mean provides information about', 'kurtosis'),
    (r'mean of a distribution is 30, the mode is 24 and the standard deviation is 4', 'greater than zero'),
    (r'deviation of a distribution from symmetry', 'skewness'),
    (r'pearsons coefficient of skewness is not possible if standard deviation is', '0'),
    (r'pearson’s coefficient of skewness cannot be used when standard deviation is', '0'),
    (r'pearson’s coefficient of skewness is greater then zero', 'positively skewed'),
    (r'method of skewness is a pure number/unitless', 'bowleys'),
    (r'first moment about mean is', '0'),
    (r'order \(highest to lowest\).*positive skewness', 'mean, median, mode'),
    (r'mean of a distribution is 25, the mode is 25 and the standard deviation is 5', 'equal to zero'),
    (r'coefficient of skewness is equal to “0”', 'symmetrical'),
    (r'bowley’s coefficient of skewness is expressed in terms of', 'independent of units'),
    (r'skewness based on mean, median, mode', 'pearson'),
    (r'kurtosis is used to represent the degree of peakedness/flatness about a', 'unimodal distribution'),
    (r'pearson coefficient of skewness is defined as', '(median-mode)/sd'), # or (mean-mode)/sd
    (r'mean=6,median =5 and standard deviation = 4.*pearson', '0.75'),
    (r'method of skewness based on quartiles', 'bowleys'),
    (r'moment ratio b2 is used to measure', 'kurtosis'),
    (r'departs from symmetry', 'skewed'),
    (r'containers having the following weights.*second moment about mean', '0.069kg'),
    (r'third moment about mean provides information about', 'skewness'),
    (r'corrected moments are calculated by the method of', 'sheppard’s correction')
]

matched = 0
target_qs = [q for q in mcqs if q.get('topic') in ['Random Variables & Distributions', 'Simple Linear Regression & Correlation', 'Moments, Skewness & Kurtosis']]
print(f"Target questions: {len(target_qs)}")
for q in target_qs:
    qtext = q['question'].lower()
    m = False
    for pat, ans in RVK_RULES:
        if re.search(pat, qtext):
            m = True
            break
    if m:
        matched += 1
    else:
        print(f"NOT MATCHED: [{q['id']}] {q['question']}")

print(f"Matched {matched} / {len(target_qs)}")
