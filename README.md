## Quantcast Coding Challenge

This is my submission for the Quantcast Coding challenge.

### How to run

Run the following line to run the code with the default log file.

`python3 most_active_cookie.py -d 2018-12-09`

To run all the tests, run the following line.

`python3 run_tests.py`

### Adding additional tests

In the tests directory, create your test file and enter input in the following format

```
Name of log file
Date
Expected output
```

To add your own log file, create one in the log-files directory and enter the name in the test file.

### Note

The behaviour of the algorithm when the date is not specified is not mentioned. I have assumed this case to return the most active cookie in the complete log file.