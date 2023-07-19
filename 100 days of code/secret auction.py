logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
should_continue = True
print("Welcome to the secret auction program.")
winner_check = {}
highest = 0

while should_continue:
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))

    winner_check[name] = bid
    other = input("Are there any other bidders? ").lower()
    if other == 'no':
        should_continue = False
for key in winner_check:
    if winner_check[key] > highest:
        highest = winner_check[key]
        winner = key


print(winner)