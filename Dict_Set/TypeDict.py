from typing import TypedDict, NotRequired, Required

'''
https://docs.python.org/3/library/typing.html#typing.TypedDict
TypedDict is a special kind of dict that is defined in terms of its
keys and their types. This allows type checkers to support
intellisense and validation when accessing dvimictionary values.
TypedDicts can be defined with required and optional keys.
'''

Vote = TypedDict('Vote', {'name': str, 'value': int}, total=False)
Vote2 = TypedDict('Vote2', {'name': str, 'value': Required[int]}, total=True)

vote: Vote2 = {'name': 'John', 'value': 25}

class Adult(TypedDict):
    name: str
    age: int
    job: NotRequired[str]


class Person(TypedDict):
    name: str
    age: int


def get_person(name: str, age: int) -> Person:
    return Person(name=name, age=age)


def main() -> None:
    person1: Person = {'name': 'John', 'age': '25'} # type error
    person2: Person = {'name': 'John', 'age': 25} # type error
    print(f'{person1=}')
    print(f'{person2=}')
    person2: Person = get_person('John', 25)  # no type error
    print(f'{person2=}')
    print(person2['name'])
    print(person2['age'])

    adult1 = Adult(name='John', age=25, job='Software Engineer')
    adult2 = Adult(name='John', age=25)
    print(f'{adult1=}')
    print(f'{adult2=}')



if __name__ == '__main__':
    main()
