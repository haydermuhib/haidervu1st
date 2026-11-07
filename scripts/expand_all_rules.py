#!/usr/bin/env python3
import json, re

EXPANDED_RULES = [
    # Data Representation & Basics
    (r'main objective of descriptive statistics', 'to describe the data we collected', "Descriptive statistics organizes, summarizes, and describes collected data."),
    (r'plot paired observed \(x,y\)', 'scatter diagram', "A scatter diagram plots bivariate paired observations (X, Y)."),
    (r'how to construct the class interval', 'find the difference between consecutive lower class limits', "Class interval size is the difference between successive lower (or upper) class limits."),
    (r'stem and leaf plot, data is measured on', 'interval scale', "Stem-and-leaf plots are used for interval or ratio continuous/quantitative data."),
    (r'more values are lying at the start of the distribution', 'positively skewed', "When data clusters at low values with a tail to the right, it is positively skewed."),
    (r'histogram consists of a set of adjacent rectangles whose bases are', 'class boundaries', "In a histogram, the bases of rectangles correspond to class boundaries."),
    (r'a ∪ b = a ⊕ b', 'a ∩ b = ∅', "A ∪ B = A ⊕ B implies there is no overlap, so A ∩ B = ∅."),
    (r'each outcome in the sample space regarded as', 'both a & b', "Each outcome is called a sample point or element of the sample space."),
    (r'frequency distribution formed considering two variables', 'bivariate frequency distribution', "A distribution of two variables is a bivariate frequency distribution."),
    (r'a – b will be', '{1,2}', "A - B = {1, 2, 3, 4} - {3, 4, 5, 6} = {1, 2}."),
    (r'then a ∩ b', '{3,4}', "A ∩ B = {1, 2, 3, 4} ∩ {3, 4, 5, 6} = {3, 4}."),
    (r'box and whisker plot, right end of the box is referred as', 'third quartile', "In a horizontal box plot, the right edge of the box represents Q3 (75th percentile)."),
    (r'box and whisker plot, left end of the box is referred as', 'first quartile', "The left edge of the box represents Q1 (25th percentile)."),
    (r'adding all the squared deviations taken from mean and dividing by the number', 'variance', "Variance = ∑(X - Mean)^2 / n."),
    (r'drawing two clubs from a well shuffled pack of 52', '1/17', "P = (13/52) × (12/51) = (1/4) × (4/17) = 1/17."),
    (r'probability of drawing two spades', '1/17', "P = (13/52) × (12/51) = 1/17."),
    (r'probability of drawing two aces', '1/221', "P = (4/52) × (3/51) = (1/13) × (1/17) = 1/221."),
    (r'approximate number of observations in a set of data covered by the interval, median  q\.d', '50 per cent', "Median ± Q.D. approximately covers the middle 50% of observations (from Q1 to Q3)."),
    (r'component bar charts are used when data is divided into', 'parts', "Component (subdivided) bar charts show the breakdown of totals into parts."),
    (r'direct personal investigation is.*when the area to be covered', 'costly', "Direct investigation over a large area is costly and time-consuming."),
    (r'series arranged according to each and every item', 'individual series', "Listing observations individually forms an individual series."),
    (r'when data are arranged at regular interval of time', 'chronological', "Classification by time is chronological classification."),
    (r'in classification, the data are arranged according to', 'similarities', "Classification groups data according to similarities and common attributes."),
    (r'quartile deviation measures the spread of data around', 'median', "Quartile deviation measures the dispersion around the median."),
    (r'measure of dispersion is used to measure.*values are disperse', 'how much values are disperse from the mean', "Measures of dispersion quantify the extent to which values deviate from the center."),
    (r'tabular arrangement for classifying data into different groups', 'frequency distribution', "A tabular grouping of data into classes and frequencies is a frequency distribution."),
    (r'which dispersion is used to compare variation', 'c.v.', "Coefficient of Variation (C.V.) compares relative variability across datasets."),
    (r'mean deviation is a measure of dispersion in which deviations are taken around', 'mean', "Mean deviation is computed by taking absolute deviations around the mean (or median)."),
    (r'dividing mean deviation by mean we get a pure number known as', 'co-efficient of mean deviation', "Coefficient of Mean Deviation = MD / Mean."),
    (r'putting the value of “k” which is greater than one in chebyshev’s inequality', 'minimum', "Chebyshev gives the minimum proportion of data within k standard deviations: 1 - 1/k^2."),
    (r'symmetrical data set mean value is 150 and standard deviation 25\. 68%', '(125,175)', "By Empirical Rule, 68% of data falls within Mean ± 1 SD: 150 ± 25 = (125, 175)."),
    (r'median<mid-quartile range<midrange then distribution will be', 'positively skewed', "When Median < Mid-Quartile < Mid-Range, the distribution is positively skewed."),
    (r'positively skewed distribution median is.*mid quartile', 'less', "In a positively skewed distribution, the median is less than the mid-quartile."),
    (r'variance s2.*\(x x \)2.*n - please choose one', 'biased estimator of σ2', "Dividing by n gives a biased estimator; dividing by n-1 gives an unbiased estimator."),
    (r'best unbiased estimator for population variance', 'sample variance', "Sample variance s^2 (with n-1 divisor) is an unbiased estimator of population variance σ^2."),
    (r'variance of the t-distribution is given by', 'ν', "Var(t) = ν / (ν - 2) for ν > 2."),
    (r'f-distribution always ranges from', '0 to +∞', "The F-statistic is a ratio of variances and ranges from 0 to +∞."),
    (r'chi-square distribution always ranges from', '0 to +∞', "Chi-square is a sum of squared standard normals, ranging from 0 to +∞.")
]

print(f"Loaded {len(EXPANDED_RULES)} expanded rules.")
