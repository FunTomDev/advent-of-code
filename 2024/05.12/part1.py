def verify_update(update:str, rules:list[str]):

	update_order = update.split(",")
	n = len(update_order)

	wrong = False

	for rule in rules:
		a, b = rule.split("|")

		if wrong:
			break

		for i in range(n//2):

			if any([x not in update_order for x in [a,b]]): #if one of given rules not present in the update
				break

			if update_order[i] == a or update_order[n-i-1] == b: #if correct order
				break

			if update_order[i] == b or update_order[n-i-1] == a: #if wrong order
				wrong = True
				break
	if not wrong:
		return int(update_order[n//2])
	else:
		return 0

def main():

	suma = 0

	with open("input.txt", "r") as file:
		lines = file.read().strip().split("\n\n")
		rules, updates = [x.split("\n") for x in lines]
		for update in updates:
			suma += verify_update(update, rules)

	print(suma)

if __name__ == "__main__":
	main()