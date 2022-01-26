from most_active_cookie import mostActiveCookie
from pathlib import Path

class runTests:
    def __init__(self):
        self.test_cases = {}

    def run_single_test(self, test_file):
        """
        Runs a single test file and checks input with output.

            Input:
                test_file(str): Complete path of test file to run

            Return:
                result(str): Result of test - Passed or Failed
        """

        # Open the file, read the input and output, then compare
        with open(test_file) as f: 
            lines = f.read().split()
            file_name = lines[0]
            date = lines[1]
            expected_output = lines[2].split(',')

            classObj = mostActiveCookie()
            actual_output = classObj.main(file_name,date)
            try:
                assert set(expected_output) == set(actual_output)
                return "Passed"
            except:
                print("Expected output: ", expected_output)
                print("Actual ouput",actual_output)
            return "Failed"

    def main(self):
        """
        Main function - Run all the test files in tests directory
        """
        pathlist = Path('tests')

        # Run all the test files
        for filename in pathlist.iterdir():
            print(filename, self.run_single_test(filename))

if __name__ == "__main__":
    classObj = runTests()
    classObj.main()

