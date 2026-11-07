#!/usr/bin/env python3
import json, re

with open('/home/haider/Desktop/Chores/sta301_objective.json') as f:
    mcqs = json.load(f)

# Rules for Measures of Central Tendency & Measures of Dispersion
DISP_CT_RULES = [
    # Factorials / Combinatorics appearing in Disp/CT
    (r'4 books can be arranged', '24'),
    (r'four books can be arranged', '24'),
    (r'letters of the word\s*[\'"]?leading[\'"]?', '5040'),
    (r'letters of the word\s*[\'"]?optical[\'"]?', '720'),
    (r'letters of the word\s*[\'"]?leader[\'"]?', '360'),
    (r'letters of the word\s*[\'"]?corporation[\'"]?', '50400'),
    (r'5c5', '1'),
    (r'10!', '3628800'),

    # Central Tendency Formulas & Definitions
    (r'five number summery consist of', 'x 0 , q1 , median, q3 , andx m'),
    (r'five-number summary', 'x 0 , q1 , median, q3 , andx m'),
    (r'middle value of an ordered array', 'median'),
    (r'median is\s*_+', 'middle point'),
    (r'which of the following is a true statement about the median', 'it is the middle value of the data values'),
    (r'most frequent value', 'mode'),
    (r'most frequently occurring', 'mode'),
    (r'number which occurs most frequently', 'mode'),
    (r'mode value from raw data can be obtained by the help of', 'dot plot'),
    (r'mode in the word mathematics', 'm, a and t'),
    (r'mode in the word tomato', 't and o'),
    (r'reciprocal of arithmetic mean of the reciprocals', 'harmonic mean'),
    (r'reciprocal of arithmetic mean of reciprocals', 'harmonic mean'),
    (r'harmonic means? is the reciprocal of', 'arithmetic mean of reciprocals'),
    (r'algebraic sum of deviations from mean', 'zero'),
    (r'sum of deviations of the observation from their mean', 'zero'),
    (r'sum of deviations from mean', 'zero'),
    (r'sum of squares of deviations from mean', 'minimum'),
    (r'sum of squared deviations from mean', 'minimum'),
    (r'mean is obtained by', 'dividing the sum of all observations by their number'),
    (r'mean is defined as', 'dividing the sum of all observations by their number'),
    (r'does not divide a set of observ', 'standard deviations'),
    (r'does not divide a set of data into equal parts', 'standard deviations'),
    (r'relationship among the averages', 'am > gm > hm'),
    (r'am\s*>=?\s*gm\s*>=?\s*hm', 'am > gm > hm'),
    (r'car is running at the rate of 15km/hr', 'harmonic mean'),
    (r'level of measurement is required for the median', 'ordinal'),
    (r'median can be found only when', 'data is arranged'),
    (r'open-ended class.*mean', 'mean can-not be computed'),
    (r'in case of an open-ended class', 'mean can-not be computed'),
    (r'geometric mean of 4 and 16', '8'),
    (r'mean of the values 2,\s*4,\s*6,\s*8', '5'),
    (r'median of this set of numbers:\s*4,\s*6,\s*7,\s*9,\s*2000', '7'),
    (r'median for the following data:\s*1,\s*1,\s*2,\s*2,\s*5,\s*5,\s*6,\s*6', '3.5'),
    (r'observations 2,3,4,5,4,6,4,\s*the mode is', '4'),
    (r'1,2,1,1,2,2,2,3,4,5,3,2,3,1,4,2,3 mode', '2'),
    (r'empirical relation.*mode', '3 median – 2 mean = mode'),
    (r'3\s*median\s*–\s*2\s*mean', '3 median – 2 mean = mode'),
    (r'f\s*m.*formula of mode', 'maximum frequency'),
    (r'lower class boundary when.*30.*40.*50.*60', '50'),
    (r'median to be measured must lie in', '50th'),
    (r'75th percentile and third quartile', 'equal'),
    (r'percentiles, median to be measured must lie in', '50th'),
    (r'equal to mean in a symmetrical distribution', 'mean = median = mode'),
    (r'equidistance from median', 'q1 and q3'),
    (r'set of 10 values all the values are 5.*5th', '5'),
    (r'set of 10 values all the values are 5.*median', '5'),
    (r'set of 10 values all the values are 5.*mean', '5'),
    (r'quantiles are', 'points on a distribution which split it into equal sized portions'),
    (r'value of harmonic mean depends on', 'all the observations'),
    (r'geometric mean gives the equal weightage to', 'ratio'),
    (r'not included in measures of central tendency', 'quartile deviation'),
    (r'not based on all the observations', 'mode'),
    (r'if any value in the data is zero.*not possible to have', 'harmonic mean'),
    (r'value of a common variable in the form of grouped bars', 'multiple bar chart'),

    # Dispersion Formulas & Properties
    (r'standard deviation of 7,\s*7,\s*7,\s*7,\s*7', '0'),
    (r'standard deviation of -1,\s*-1,\s*-1,\s*-1', '0'),
    (r'standard deviation of c\s*\(constant\)', '0'),
    (r'standard deviation of 64 is', '8'),
    (r'variance of a sample.*equal to 64.*standard deviation', '8'),
    (r'standard deviation of a population is 5.5.*variance', '30.25'),
    (r'mean is 25 and s\.d is 5 then c\.?v', '20%'),
    (r'mean\s*=\s*25\s*&\s*s\.d\s*is\s*5\s*then c\.?v', '20%'),
    (r'μ=3.82 and s\.d\(x\)=1.2, then c\.v\(x\)', '31.4%'),
    (r'coefficient of variance = 50% and standard deviation=\s*2', '4'),
    (r'y\s*=\s*3x\s*\+\s*5.*s\.d of y', '3 s.d(x)'),
    (r'y\s*=\s*bx.*variance of y', 'b2 var(x)'),
    (r'range of the scores 29,\s*3,\s*143,\s*27,\s*99', '140'),
    (r'range for the following data:\s*22,\s*22,\s*30,\s*32,\s*37,\s*48,\s*60,\s*88', '66'),
    (r'range for the following data:\s*10,\s*32,\s*33,\s*34,\s*37,\s*42,\s*55,\s*58', '48'),
    (r'range of the values\s*-10,\s*-\s*19,\s*-9,\s*-15,\s*-28,\s*-26,\s*-25', '19'),
    (r'range of -2,-3,-5,-10', '8'),
    (r'range of the values -2.50, -3.70', '7.5'),
    (r'formula of mid quartile range', '(q1 + q3)/2'),
    (r'formula of mid-range', 'xm + x0'),
    (r'which one is the formula of mid range', 'xm + x0'),
    (r'which one is the formula of mid-range', 'xm + x0'),
    (r'formula of range', 'xm − x0'),
    (r'least affected by extreme values', 'quartile deviation'),
    (r'least affected by the extreme values', 'quartile deviation'),
    (r'not measure of dispersion', '50th percentile'),
    (r'which one is the not measure of dispersion', '50th percentile'),
    (r'measure of dispersion.*free from the units', 'coefficient of variation'),
    (r'unit of measurement remains.*relative dispersion', 'unitless'),
    (r'measures of relative dispersion unit of measurement', 'vanish'),
    (r'relative measure of dispersion is one that is expressed', 'ratio'),
    (r'co-efficient of standard deviation is', 'a pure number'),
    (r'co-efficient of standard devia', 'a pure number'),
    (r'standard deviation divided by mean is known as', 'co-efficient of standard deviation'),
    (r'measure of dispersion is used to compare variation between two', 'c.v'),
    (r'measures the dispersion around mean', 'mean deviation'),
    (r'chebychev.*not hold for k', '1'),
    (r'chebyshev.*not hold for k', '1'),
    (r'for any number k.*at least 1.*1/k2', 'greater than 1'),
    (r'empirical rule.*approximately 68%', '(mean - s.d, mean + s.d)'),
    (r'empirical rule.*approximately 95%', '(mean - 2s.d, mean + 2s.d)'),
    (r'empirical rule.*approximately 99.7%', '(mean - 3s.d, mean + 3s.d)'),
    (r'measure of dispersion can never be', 'negative'),
    (r'best measure of variation', 'standard deviation'),
    (r'variance is expressed in _______ units', 'squared'),
    (r'serious disadvantage of using range', 'maximum values'),
    (r'range as a measure of dispersion.*based on only', 'both minimum and maximum values'),
    (r'positive square root of variance', 'standard deviation'),
    (r'dispersion means the', 'variability'),
    (r'mean deviation can also be caluculated around', 'median'),
    (r'mean deviation can also be calculated around', 'median'),
    (r'quartile deviation is also defined as', 'semi-interquartile range'),
    (r'quartile deviation is based on', 'not all values'),
    (r'first and third quartile are 21.16 and 56.36.*quartile deviation', '17.1'),
    (r'first and third quartiles are 22.*16 and 56.*36', '17.1'),
    (r'q1=62 and q3=87.*mid-quartile range', '74.5'),
    (r'f-distribution always ranges from', '0 to '),
    (r'analysis of variance \(anova\) is a test for equality of', 'means'),
    (r'what does it mean when a data set has a standard deviation equal to zero', 'all values of the data appear to be the same'),
    (r'condition standard deviation could assume a negative value', 'never'),
    (r'which dispersion is used to compare variability', 'c.v.')
]

disp_ct_qs = [q for q in mcqs if q.get('topic') in ['Measures of Dispersion', 'Measures of Central Tendency']]
print(f"Total Disp & CT: {len(disp_ct_qs)}")

matched = 0
unmatched = []
for q in disp_ct_qs:
    qtext = q['question'].lower()
    m = False
    for pat, ans in DISP_CT_RULES:
        if re.search(pat, qtext):
            m = True
            break
    if m:
        matched += 1
    else:
        unmatched.append(q)

print(f"Matched {matched} / {len(disp_ct_qs)} ({matched*100/len(disp_ct_qs):.1f}%)")
print(f"Unmatched: {len(unmatched)}")
