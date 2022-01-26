import argparse
from datetime import datetime

class mostActiveCookie:
    def __init__(self):
        """
        Initialize cookies and timestamps arrays to store data
        """
        self.cookies = []
        self.timestamps = []

    def get_bound(self,date,bound_type="lower"):
        """
        Get first and last occurence of a date in timestamps using binary search

            Input:
                date(str): Date that we are supposed to search
                boundType(str): "lower" for first Occurence and "upper" for lastOccurence

            Returns:
                mid(int): First or last index of date in timestamps
        """
        N = len(self.timestamps)
        begin, end = 0, N - 1

        # Binary search to get lower/upper bound
        while begin <= end:
            mid = int((begin + end) / 2)    
            if self.timestamps[mid] == date:
                if bound_type=="lower":
                    if mid == begin or self.timestamps[mid - 1] > date:
                        return mid
                    end = mid - 1
                else:
                    if mid == end or self.timestamps[mid + 1] < date:
                        return mid
                    begin = mid + 1
            elif self.timestamps[mid] < date:
                end = mid - 1
            else:
                begin = mid + 1
        
        # Return -1 if item not found
        return -1

    def get_most_active_cookie(self,first_index, last_index):
        """
        Returns the cookies that are the most active on a specific date.

            Input:
                first_index(int): lower bound in timestamps for searching cookies
                last_index(int): upper bound in timestamps for searching cookies

            Returns:
                most_active_cookies(list): List of most active cookies
        """
        frequency, max_frequency = {},0
        most_active_cookies = []

        # Find frequency of each cookie within the range
        for i in range(first_index, last_index+1):
            frequency[self.cookies[i]] = frequency.get(self.cookies[i],0)+1
            max_frequency = max(max_frequency, frequency[self.cookies[i]])
        
        # Get all cookies with highest frequency
        for cookie, freq in frequency.items():
            if freq == max_frequency:
                most_active_cookies.append(cookie)
        return most_active_cookies


    def read_input(self,file_name):
        """
        Reads a file for cookies and their respoctive timestamps. Populates the class variables.

            Input:
                file_name(str): Name of the file to read data from.
        """
        with open(file_name) as f:       
            for line in f:         
                split_data = line.split()[0].split(',')
                self.cookies.append(split_data[0])
                self.timestamps.append(datetime.strptime(split_data[1],'%Y-%m-%dT%H:%M:%S+00:00').date())

    def main(self,file_name, date=None):
        """
        Main function - Accepts file name and date and returns most active cookie on that date

            Input:
                file_name(str): File name to read data from.
                date(str): Date for which we want the most active cookie

            Returns:
                most_active_cookies(list): List of most active cookies
        """

        # Read the input into class variables
        self.read_input(file_name)
        first_index, last_index = 0, len(self.cookies)-1

        # If date is specified run the algorithm for that date
        if date is not None:
            date = datetime.strptime(date,'%Y-%m-%d').date()

            # Get first and last indices of the date's occurence
            first_index = self.get_bound(date,"lower")
            last_index = self.get_bound(date,"upper")

            # If date does not exist in the log file, return -1
            if first_index == -1 and last_index == -1:
                return ['-1']

        # If the date is not specified, algorithm will run for the whole log file.
        return self.get_most_active_cookie(first_index,last_index)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", help="date for most active cookie")
    args = parser.parse_args()

    file_name = "log-files/log-file1.csv"
    classObj = mostActiveCookie()
    if args.date:
        result = classObj.main(file_name, args.date)
        print('\n'.join(result))
    else:
        result = classObj.main(file_name)
        print('\n'.join(result))