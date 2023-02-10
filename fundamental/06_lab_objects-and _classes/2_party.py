class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    system_info = input()
    if system_info == "End":
        break
    party.people.append(system_info)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
