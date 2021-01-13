class Value:

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value - (value * instance.commission)


if __name__ == '__main__':
    class Account:
        amount = Value()

        def __init__(self, commission):
            self.commission = commission


    new_acc = Account(0.1)
    new_acc.amount = 100

    print(new_acc.amount)

# SOLUTION FROM TEACHER
# class Value:
#     def __init__(self):
#         self.amount = 0
#
#     def __get__(self, obj, obj_type):
#         return self.amount
#
#     def __set__(self, obj, value):
#         self.amount = value - value * obj.commission
