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



from random import randint
AMT_TRIALS = 1000
AMT_YEARS = 10
AMT_SECTIONS_PER_YEAR = 12
AMT_STOCKS = 10
GAIN_CUT_OFF = 0.1
GUT_CHECK = -0.05
STARTING_BALANCE = 6000
WIN_PROBABILITY = 0.5
# MIN_WIN_PROB = -GUT_CHECK / (GAIN_CUT_OFF - GUT_CHECK)


ADD_YEARLY_INVESTMENT = STARTING_BALANCE

ACCURACY = 1.e6

SP_500_AVG_GAIN_YEAR = 0.1

total_balance = 0
for trials in range(0,AMT_TRIALS):
	balance = STARTING_BALANCE
	for year in range(0,AMT_YEARS):
		for sections in range(0,AMT_SECTIONS_PER_YEAR):
			amt_per_stock = balance / AMT_STOCKS
			stocks = {"ups": 0, "downs": 0}
			for j in range(0, AMT_STOCKS):
				if randint(0,ACCURACY) <= WIN_PROBABILITY * ACCURACY:
					stocks["ups"] += 1
				else:
					stocks["downs"] += 1
			balance = 0
			for j in range(0, stocks["ups"]):
				balance += amt_per_stock * (1 + GAIN_CUT_OFF)
			for j in range(0, stocks["downs"]):
				balance += amt_per_stock * (1 + GUT_CHECK)
		if year != AMT_YEARS - 1:
			balance += ADD_YEARLY_INVESTMENT
	total_balance += balance
average_balance = total_balance / AMT_TRIALS

avg_cash_flow = [-STARTING_BALANCE]
for i in range(0, AMT_YEARS-1):
	avg_cash_flow.append(-ADD_YEARLY_INVESTMENT)
avg_cash_flow.append(average_balance)
irr = irr_calculator(avg_cash_flow)
sp_500_bal = STARTING_BALANCE
for year in range(0,AMT_YEARS):
	sp_500_bal += sp_500_bal * SP_500_AVG_GAIN_YEAR
	if year != AMT_YEARS - 1:
		sp_500_bal += ADD_YEARLY_INVESTMENT
avg_cash_flow = avg_cash_flow[:-1]
avg_cash_flow.append(sp_500_bal)
spirr = irr_calculator(avg_cash_flow)
print(f"STARTING BALANCE   : ${STARTING_BALANCE:,.2f}")
print(f"YEARLY INVESTMENT  : ${ADD_YEARLY_INVESTMENT:,.2f}")
print(f"EST. ENDING BALANCE: ${average_balance:,.2f}")
print(f"ESTIMATED IRR VALUE: {irr * 100:+,.2f}%")
print(f"({AMT_YEARS}-YEAR, {AMT_TRIALS:,}-TRIAL ESTIMATE @ {GAIN_CUT_OFF*100:+.2f}% GAIN CUT-OFF, {GUT_CHECK*100:.2f}% GUT-CHECK, {WIN_PROBABILITY*100:.2f}% WIN PROBABILITY, {AMT_STOCKS:,} STOCKS, {AMT_SECTIONS_PER_YEAR} CASH-INS PER YEAR)")
print(f"EST. SP END BALANCE: ${sp_500_bal:,.2f}")
print(f"EST. SP IRR VALUE  : {spirr * 100:+,.2f}%")
print(f"({AMT_YEARS}-YEAR ESTIMATE @ {SP_500_AVG_GAIN_YEAR*100:+.2f}% S&P-500 AVERAGE GAIN PER YEAR)")