class Party:
    def __init__(self):
        self.people = []

party = Party()
while True:
    new_people = input()
    if new_people == 'End':
        break
    else:
        party.people.append(new_people)
        continue

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
