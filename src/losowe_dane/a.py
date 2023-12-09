from faker import Faker
# fake = Faker(['it_IT', 'en_US', 'ja_JP', 'pl_PL'])
fake = Faker(['pl_PL'])
for _ in range(20):
    print(fake.name())
    print(fake.address())
    print(fake.phone_number())
    print(fake.pesel())
    print('----')


