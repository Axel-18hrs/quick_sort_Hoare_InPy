import random
import random
import time

class QuickSort:
    def __init__(self):
        self._Random = random.Random()
        self._Option = 0
        self._ContainExchange = 0
        self._ContainPartition = 0
        self._ContainRecursive = 0
        self._ArrayOne = [4, 8, -3, 10, -7, -9, 2, -5, 6, 1]
        self._ArrayTwo = [4, 8, -3, 10, -7, -9, 2, -5, 6, 1]
        self._ArrayThree = [4, 8, -3, 10, -7, -9, 2, -5, 6, 1]

    def main(self):
        Information = ["[1]Initial Pivot", "[2]Middle Pivot", "[3]Final Pivot", "[4]Random Pivot", "[5]Exit"]

        while self._Option != 5:
            self._ContainExchange = 1
            self._Option = 0
            print("Quicksort")
            for i in Information:
                print(i)
            while True:
                try:
                    self._Option = int(input("Choose one: "))
                    break  # Salir del bucle si la conversión fue exitosa
                except ValueError:
                    print("Please enter a valid integer.")

            if self._Option == 1:
                print("Initial Pivot")
                self.measure_time(self._ArrayOne)
                input()
            elif self._Option == 2:
                print("Middle Pivot")
                self.measure_time(self._ArrayTwo)
                input()
            elif self._Option == 3:
                print("Final Pivot")
                self.measure_time(self._ArrayThree)
                input()
            elif self._Option == 4:
                self._Option = self._Random.randint(0, 10000)
                print("Random Generator")
                self.measure_time(self.generate_vector(0, self._Random.randint(0, 100), 10))
                input()

    def partition(self, array, first_index, last_index):
        self._ContainPartition += 1
        if self._Option == 1:
            index_pivot = first_index
        elif self._Option == 2:
            index_pivot = (last_index + first_index) // 2
        elif self._Option == 3:
            index_pivot = last_index
        else:
            index_pivot = self._Random.randint(first_index, last_index)

        array[first_index], array[index_pivot] = array[index_pivot], array[first_index]
        self.print_swap(array, first_index, index_pivot)
        self._ContainExchange += 1

        pivot = array[first_index]
        left = first_index + 1
        right = last_index

        while True:
            while left <= right and array[left] <= pivot:
                left += 1

            while left <= right and array[right] >= pivot:
                right -= 1

            if right < left:
                break

            array[left], array[right] = array[right], array[left]
            self.print_swap(array, left, right)
            self._ContainExchange += 1

            left += 1
            right -= 1

        array[first_index], array[right] = array[right], array[first_index]
        self.print_swap(array, first_index, right)
        self._ContainExchange += 1

        return right

    def quick_sort(self, array, first_index, last_index):
        if first_index < last_index:
            self._ContainRecursive += 1
            pivot = self.partition(array, first_index, last_index)
            self.quick_sort(array, first_index, pivot - 1)
            self.quick_sort(array, pivot + 1, last_index)

    def print_array(self, arr):
        self.quick_sort(arr, 0, len(arr) - 1)
        print("\nResult: [ " + ", ".join(map(str, arr)) + " ]")
        print("Swaps: " + str(self._ContainExchange) + "\nPartitions: " + str(self._ContainPartition) +
              "\nRecursions: " + str(self._ContainRecursive))
        self._ContainExchange = 0
        self._ContainPartition = 0
        self._ContainRecursive = 0

    def print_swap(self, array, left, right):
        print("[", end=" ")
        for i in range(len(array)):
            if right == i == left:
                print("\033[93m" + str(array[i]) + "\033[0m", end=" ")
            elif i == left or i == right:
                print("\033[91m" + str(array[i]) + "\033[0m", end=" ")
            else:
                print(array[i], end=" ")

            if i < len(array) - 1:
                print(", ", end="")
        print("]")

    def generate_vector(self, minon, length, val=5):
        _list = random.sample(range(minon, length), min(val, length - minon))
        return _list

    def measure_time(self, array):
        start_time = time.time()
        self.quick_sort(array, 0, len(array) - 1)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("\nResult: [ " + ", ".join(map(str, array)) + " ]")
        print("Swaps: " + str(self._ContainExchange) + "\nPartitions: " + str(self._ContainPartition) +
              "\nRecursions: " + str(self._ContainRecursive))
        print(f"Elapsed Time: {elapsed_time:.6f} seconds")
        self._ContainExchange = 0
        self._ContainPartition = 0
        self._ContainRecursive = 0

# Uso del algoritmo
quick_sort_instance = QuickSort()
quick_sort_instance.main()
