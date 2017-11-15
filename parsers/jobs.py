from time import time
import runner
from runner import Dataset


dt = '2017-06-01'


start = time()
assert runner.CBR_USD(dt).upload()
assert runner.BrentEIA(dt).upload()
assert runner.USTbonds(dt).upload()
assert runner.RosstatKEP_Monthly(dt).upload()
assert runner.RosstatKEP_Quarterly(dt).upload()    
assert runner.RosstatKEP_Annual(dt).upload() 
print("Uploaded dataset:", round(time() - start, 1), "sec")

# FIMXE: code below fails with 

#  File "C:\Users\Евгений\Documents\GitHub\parser-template\parsers\helpers.py", line 27, in make_date
#    return datetime.strptime(date_string, fmt).date()
#   TypeError: strptime() argument 1 must be str, not datetime.date

start = time()
Dataset('2017-09-01').upload()
print("Uploaded dataset:", round(time() - start, 1), "sec")


# Suggestions (to discuss):
    
#    1. can have a verbose version what prints results:
#
#      'Uploaded 350 datapoints in 0.12 seconds in 1 attempt(s)'
#      'Failed with 350 datapoints in 10.52 seconds in 3 attempt(s)'
#
#       may introduce timing as decorator

#
#    2. WONTFIX: can have a less restrictive BaseParser interface for the dates, eg accept
#       '2000-06', (2000, 6), 2000
#
#       can be done with 'arrow' 

#
#    3. NOT TODO:  generator vs list?

#
#    4. how risky and how long is this: Dataset(dt).upload() ?
    