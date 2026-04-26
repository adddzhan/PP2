class PhoneBook:
    def __init__(self, id, first_name, last_name, email, birthday, group, phones):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birthday = birthday
        self.group = group
        self.phones = phones  # список [(phone, type)]

    def __repr__(self):
        return f"{self.first_name} {self.last_name} | {self.email} | {self.group} | {self.phones}"