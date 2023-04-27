# Bracket Expressions

## Introduction
The term 'Bracket Expressions' doesn't really make sense. In fact, it doesn't make sense to me, too. But then, when writing a tech-related exam, I came across this question: 


The expression '(+ 1 2 3)' refers to the expression '1 + 2 + 3', also extending to the operators -, * and /. Given this data, evaluate: 
`(/ (* (- (+ 12 4) (* 3 4)) (+ 5 6 7)) (+ 8 9 10))`


It took me around 5 minutes to solve this problem, but yeah, it was worth every second. After the exam, I thought, "Why shouldn't I write a program to solve such expressions?" 

In a couple of hours, I was ready with a perfectly working program, which can solve *correct* expressions (I didn't add any error checking, yet).

Since I dodn't know what they are called, I stuck to the name **"Bracket Expressions"**.

## Release Notes

### Version 1.0.0
The first public release of the code.
- Works for non-nested and nested expressions
- NO error checking
- Example included in main.py