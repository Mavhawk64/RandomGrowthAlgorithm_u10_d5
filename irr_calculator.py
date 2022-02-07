def irr_calculator(cash_flows, guess=0,limit=100):
	new_guess = guess - f(guess, cash_flows) / d(guess, cash_flows)
	if new_guess == guess or limit <= 0:
		return new_guess
	return irr_calculator(cash_flows,new_guess,limit-1)
def f(guess, cash_flows):
	s = 0
	for i in range(0, len(cash_flows)):
		s += cash_flows[i] / (1 + guess) ** i
	return s
def d(guess, cash_flows):
	s = 0
	for i in range(0, len(cash_flows)):
		s += -i * cash_flows[i] / (1 + guess) ** (i+1)
	return s

print(irr_calculator([-6,-6,17.6],0.))