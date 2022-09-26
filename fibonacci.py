def fibonocci(n):
	ini = [1, 1]
	count = 1
	a = 1

	if n == 2:
		return ini

	while a < n-1:
		count += ini[-2]
		a += 1;
		ini.append(count)

	return ini


result = fibonocci(5)

print(result)
