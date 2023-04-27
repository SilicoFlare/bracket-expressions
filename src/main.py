from __CORE__ import number_convert, tokenize, evaluate

exp = '(/ (* (- (+ 12 4) (* 3 4)) (+ 5 6 7)) (+ 8 9 10))'

tokens = tokenize(exp)

# number_convert(tokens)

# print(tokens)

ans = evaluate(tokens)
print(ans)