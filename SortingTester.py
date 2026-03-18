import random
import time

class SortingTester:
    def __init__(self, sorting_algorithm, seed=7524):
        self.sorting_algorithm = sorting_algorithm
        random.seed(seed)
    def test_sorting_algorithm(self, test_cases):
        spendTimnes = []
        for i, (input_list, expected_output) in enumerate(test_cases):
            start_time = time.time()
            sorted_list = self.sorting_algorithm(input_list)
            end_time = time.time()
            spendTimnes.append(end_time - start_time)
            assert sorted_list == expected_output, f"Test case {i + 1} failed: expected {expected_output}, got {sorted_list}"
        print(f"All {len(test_cases)} test cases passed!")
        print(f"Average time taken: {sum(spendTimnes) / len(spendTimnes):.4f} seconds")

    @staticmethod
    def make_a_test_case(size=1000000):
        input_list = [random.randint(-100000000, 100000000) for _ in range(size)]
        expected_output = sorted(input_list)
        return (input_list, expected_output)

    @staticmethod
    def make_multiple_test_cases(num_cases=5, size=1000000):
        test_cases = []
        for i in range(num_cases):
            test_cases.append(SortingTester.make_a_test_case(size))
        return test_cases
    
    @staticmethod
    def Save_test_cases_to_file(test_cases, filename="test_cases.txt"):
        with open(filename, "w") as f:
            for input_list, expected_output in test_cases:
                f.write(f"input_list:{input_list} expected_output:{expected_output}\n")

    @staticmethod
    def Load_test_cases_from_file(filename="test_cases.txt"):
        test_cases = []
        with open(filename, "r") as f:
            for line in f:
                input_list_str, expected_output_str = line.strip().split(" expected_output:")
                input_list = eval(input_list_str.replace("input_list:", ""))
                expected_output = eval(expected_output_str)
                test_cases.append((input_list, expected_output))
        return test_cases



import bubble_sort
if __name__ == "__main__":

    #num_cases=5
    #size=3000
    #test_cases = SortingTester.make_multiple_test_cases(num_cases, size)
    # save test cases to a file
    #SortingTester.Save_test_cases_to_file(test_cases, "test_cases.txt")

    bubbleSort = SortingTester(bubble_sort.bubble_sort)
    bubbleSort.test_sorting_algorithm(SortingTester.Load_test_cases_from_file("test_cases.txt"))

    


