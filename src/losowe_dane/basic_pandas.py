import pandas as pd
from dataclasses import dataclass

# pip install pandas

@dataclass
class Person:
    pesel: str
    name: str
    phone: str
    address: str


# Create a list of Person objects
people = [Person("12345678901", "Alice", "123-456-7890", "123 Main St"),
          Person("98765432109", "Bob", "987-654-3210", "456 Elm St")]

# Convert the list of Person objects to a DataFrame
df = pd.DataFrame([vars(person) for person in people])

# Save the DataFrame to a CSV file
df.to_csv('people.csv', index=False)

# Load the saved CSV file back into a DataFrame
df_loaded = pd.read_csv('people.csv')

# Convert the DataFrame back to a list of Person objects
persons = [Person(**row) for row in df_loaded.to_dict(orient='records')]
