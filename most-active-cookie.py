import argparse
from datetime import datetime

class mostActiveCookie:
    def __init__(self):
        self.cookies = []
        self.timestamps = []

    def get_bound(self,date,boundType="upper"):
        N = len(self.timestamps)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            if self.timestamps[mid] == date:
                if boundType=="upper":
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
        return -1

    def get_most_active_cookie(self,firstIndex, lastIndex):
        frequency, max_frequency = {},0
        most_active_cookies = []
        for i in range(firstIndex, lastIndex+1):
            frequency[self.cookies[i]] = frequency.get(self.cookies[i],0)+1
            max_frequency = max(max_frequency, frequency[self.cookies[i]])
        
        print(frequency)
        for cookie, freq in frequency.items():
            if freq == max_frequency:
                most_active_cookies.append(cookie)

        print(most_active_cookies)

        return most_active_cookies


    def read_input(self,fileName):
        with open(fileName) as f:       
            for line in f:         
                split_data = line.split()[0].split(',')
                self.cookies.append(split_data[0])
                self.timestamps.append(datetime.strptime(split_data[1],'%Y-%m-%dT%H:%M:%S+00:00').date())

    def main(self,fileName, date=None):
        self.read_input(fileName)
        firstIndex, lastIndex = 0, len(self.cookies)-1
        if date is not None:
            date = datetime.strptime(date,'%Y-%m-%d').date()
            firstIndex = self.get_bound(date,"upper")
            lastIndex = self.get_bound(date,"lower")
        
        print([firstIndex, lastIndex])    
        return self.get_most_active_cookie(firstIndex,lastIndex)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", help="date for most active cookie")
    args = parser.parse_args()

    fileName = "tests/test1.csv"
    classObj = mostActiveCookie()
    if args.date:
        classObj.main(fileName, args.date)
    else:
        classObj.main(fileName)