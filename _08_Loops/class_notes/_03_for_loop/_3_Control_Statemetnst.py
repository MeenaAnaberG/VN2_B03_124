import queue


def task(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f"Task {name} running")
            for x in range(count):
                total += 1
            print(f"Task {name} total: {total}")


def main():
    work_queue = queue.Queue()
    for work in [15, 10, 5, 2]:
        work_queue.put(work)
    tasks = [(task, "One", work_queue), (task, "Two", work_queue)]
    for t, n, q in tasks:
        t(n, q)


if __name__ == "__main__":
    main()
#
# # class A:
# #     def __init__(self, val):
# #         self.val = val
# #         self._val1 = val
# #         self._val2 = self._val1
# # obj=A(10)
# # print(obj._val2)
# # print(A.__init__.__repr__)
# # print(len(obj.__dict__))
# class Run(object):
#
#
# # Constructor
#     def __init__(boy, why):
#         boy.why = "Gump"
#
#
#     def Identity(boy):
#         return boy.why
#
#
#     def isBoy(boy):
#         return False
#
#
# class Forrest(Run):
#
#     def isBoy(boy):
#         return True
#
# x = Run("John")
# print(x.Identity(), x.isBoy())
#
# x = Forrest("Abram")
# print(x.Identity(), x.isBoy())
# def myFunc(x, *y):
#     return type(y)
#
#
# b = myFunc(1, 2, 3, 4, 5, 6, 7, 8)
# print(b)

# ages = {'max':23, 'tim': 23, 'jim':22}
# print(ages.popitem())
# print(ages)