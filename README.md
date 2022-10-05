# Eonlabs-Data-Collection-TTA
TECH ASSESSMENT
by Aurelle TCHAGNA KOUANOU (tkaurelle@gmail.com)
## General Idea

The goal is to create a script that collects Google Trends weekly, 
daily and hourly data with the keyword ‘bitcoin’ since 2015-01-01 and save results in csv or json file. 
To do it, we need to connect to the Google Trends API through an HTTP request and fetch data from it, 
then we save the response data into a csv. Since we are dealing with a big amount of data, we will use Python.

## Time

It tooks 2-3 Hours to understand the documentation of Google Trends API. 30-45 minutes to write the code.
## Approach & Difficulties
Try to code the entire function that makes requests and fetches data from Google trends API was not necessary 
because there is a Python library that does the job. So we used [pytrends](https://pypi.org/project/pytrends/) 

The main problem with this approach is the fact that Google Trends API changes the periodicity of the results 
based on the timeframe e.g : if I want to have Google Trends data Weekly from 5 years i have to use this format
"today 5-y" or a "YYYY-MM-DD YYYY-MM-DD" date interval fromat. Changing it to more than 5 years date interval
will provide monthly data.To solve it we fetch data fron 2015-01-01 to 2019-01-01 and then from 2019-01-02 to
now after that we concatenate the two sets of data


## Instructions

To run this code you have to install Pytrends first

```console
pip install pytrends
```

After that just run the script.py file

```console
python script.py
```
