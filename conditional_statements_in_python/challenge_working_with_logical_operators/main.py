bobs_age = 17
alices_age = 20
johns_age = 10
mikes_age = 18

# Checking if both Bob and John can enter the park (both must be adults)
can_bob_and_john_enter = bobs_age or johns_age
can_bob_and_john_enter = (alices_age >= 18) and (johns_age >= 18)
# Checking if either Alice or Mike can enter the park (at least one must be an adult)
can_alice_or_mike_enter = mikes_age and alices_age
can_alice_or_mike_enter = (alices_age >=18) or (mikes_age >= 18)
# Checking if Bob, Alice, and John can all enter the park together (all must be adults)
can_bob_alice_john_enter = (bobs_age or alices_age) and johns_age
can_bob_alice_john_enter = (bobs_age >= 18) and (alices_age >= 18) and (johns_age >= 18)
# Testing
print("Can Bob and John enter the park together? ", can_bob_and_john_enter)
print("Can Alice or Mike enter the park? ", can_alice_or_mike_enter)
print("Can Bob, Alice and John all enter the park together? ", can_bob_alice_john_enter)