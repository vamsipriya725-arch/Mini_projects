class InvalidAgeError(Exception):
    pass
try:
    age = int(input())
    if age < 18:
        raise InvalidAgeError("Age Must Be Above 18")
except Exception as e:
    print(e)
