class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards member: {self.is_rewards_member}")
        print(f"Points: {self.gold_card_points}")
        return self
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User is already a member!")
        return self
    
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Insufficient points!")
        return self

user_1 = User("Joe", "Smith", "joesmith@gmail.com", 35)
user_2 = User("Jim", "Scott", "jimscott@gmail.com", 40)
user_3 = User("Amy", "Johnson", "amyjohnson@gmail.com", 45)

user_1.display_info().enroll().spend_points(50).display_info()
# user_1.spend_points(50)
# user_2.enroll()
# user_2.spend_points(80)
# user_1.enroll()
# user_3.spend_points(40)
# user_1.display_info()
# user_2.display_info()
# user_3.display_info()