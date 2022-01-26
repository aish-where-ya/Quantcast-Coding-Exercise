import os
from most_active_cookie import mostActiveCookie
from pathlib import Path

class runTests:
    def __init__(self):
        self.test_cases = {}

    def run_single_test(self, testFile):
        with open(testFile) as f: 
            lines = f.read().split()
            fileName = lines[0]
            date = lines[1]
            expectedOutput = lines[2].split(',')
            classObj = mostActiveCookie()
            actualOutput = classObj.main(fileName,date)

            if set(expectedOutput) == set(actualOutput):
                return "Passed"
            return "Failed"

    def main(self):
        pathlist = Path('tests')
        for filename in pathlist.iterdir():
            print(filename, self.run_single_test(filename))

if __name__ == "__main__":
    classObj = runTests()
    classObj.main()

