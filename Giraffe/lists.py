
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.sort()
friends2 = friends.copy()
print(friends.index("Kevin"))