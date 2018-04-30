import random

class Person():
    def __init__(self):
        self.preferences = {}
        self.preferences_num = {}
        self.no_preferences = True
        self.partner = ""

    def set_preferences(self, n, members):
        if self.no_preferences:
            used_nums = set()
            for member in members:
                rank = random.randint(1, n)
                while rank in used_nums:
                    rank = random.randint(1, n)
                used_nums.add(rank)
                self.preferences[member.get_name()] = rank
                self.preferences_num[rank] = member
            self.no_preferences = False

    def get_preference(self, name):
        return self.preferences[name]

class A(Person):
    members = []
    def __init__(self, num, n):
        self.name = "A " + str(num)
        self.preferred = n
        super().__init__()
        A.members.append(self)

    def get_name(self):
        return self.name

    def get_members():
        return A.members

    def get_partner(self):
        return self.partner

    def propose(self):
        if self.partner == "":
            accepts = self.preferences_num[self.preferred].set_proposal(self)
            if accepts:
                self.partner = self.preferences_num[self.preferred].get_name()
            self.preferred -= 1
    def set_leave(self):
        self.partner = ""

class B(Person):
    members = []
    def __init__(self, num):
        self.name = "B " + str(num)
        super().__init__()
        B.members.append(self)

    def get_name(self):
        return self.name

    def get_members():
        return B.members

    def get_partner(self):
        return self.partner

    def set_proposal(self, name):
        if self.partner == "":
            self.partner = name
            print(self.name + " accepts " + name.get_name())
            return True
        else:
            if self.get_preference(name.get_name()) > self.get_preference(self.partner.get_name()):
                print(self.name + " left " + self.partner.get_name() + " for " + name.get_name())
                self.partner.set_leave()
                self.partner = name
                return True
            else:
                print(self.name + " rejects " + name.get_name())
                return False

n = int(input("How many people of each group are there?"))
for i in range(n):
    x = A(i + 1, n)
    y = B(i + 1)
a_list = A.get_members()
b_list = B.get_members()
for member in a_list:
    member.set_preferences(n, b_list)
for member in b_list:
    member.set_preferences(n, a_list)

not_married = True
a = 1
while not_married:
    for member in a_list:
        member.propose()
    not_married = False
    for member in b_list:
        if member.get_partner() == "":
            not_married = True
    a += 1

for member in b_list:
    print(member.partner.get_name() + " married " + member.get_name())
    print(member.get_name() + " was " + str(member.partner.get_preference(member.get_name())) + " for " + member.partner.get_name())
    print(member.partner.get_name() + " was " + str(member.get_preference(member.partner.get_name())) + " for " + member.get_name())
    print()
