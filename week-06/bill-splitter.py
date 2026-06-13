import random

# Using set seed for consistent result
random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750

def split_bill(friends, total):
    # Returns the amount each friend has to pay
    return total / len(friends)


def pick_lucky(friends):
    # Returns one random friends name
    return random.choice(friends)


def final_summary(friends, total):
    # Dispays the total summary of what each friend has to pay plus who plays the extra 50
    share = split_bill(friends, total)
    lucky_friend = pick_lucky(friends)

    print(f"Total Bill: NPR {total}")
    print(f"Number of Friends: {len(friends)}\n")

    print("Bill Split Summary:")
    for friend in friends:
        if friend == lucky_friend:
            # Creating a local variable for the lucky persons share
            taxed = share + 50
            print(f"  {friend}: NPR {share:.2f} + NPR 50 (lucky tax) = NPR {taxed:.2f}")
        else:
            print(f"  {friend}: NPR {share:.2f}")

    print(f"\nLucky Person: {lucky_friend} (pays extra NPR 50)")

final_summary(friends, total_bill)
