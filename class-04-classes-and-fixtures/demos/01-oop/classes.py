# class Human(object):
class Human:
    """Base class
    """
    eye_color = None

    def get_eye_color(self):
        """
        """
        raise NotImplementedError


class Person(Human):
    """
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def set_eye_color(self, eye_color):
        self.eye_color = eye_color

    def get_eye_color(self):
        if self.eye_color is not None:
            output = f'I have {self.eye_color} colored eyes.'
            return output

        return 'Eye Color is currently unavailable.'


class Employee(Person):
    """
    """
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id

        super().__init__(name, age)
        # self.name = name
        # self.age = age

    def __str__(self):
        output = f'Employee: {self.name}'
        return output

    def __repr__(self):
        output = f'<Employee ID: {self.emp_id}, NAME: {self.name}>'
        return output
