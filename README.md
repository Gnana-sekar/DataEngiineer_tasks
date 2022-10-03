# Dataweave_Intern
**Note: Here the json files are downloaded and saved in a local location. If you run the code on your PC, please put your file in the file path of the code.** 

1. No of URLH which are overlapping.

2. For all the URLH which are overlapping, calculate the price difference (wrt available_price) if there is any between yesterday's and today's crawls. There might be duplicate URLHs in which case you can choose the first valid (with http_status 200) record.

3. No of Unique categories in both files.

4. List of categories which is not overlapping.

5. Generate the stats with count for all taxonomies (taxonomy is concatenation of category and subcategory separated by " > ").
Eg:
Cat1 > Subcat1: 3500
Cat1 > Subcat2: 2000
Cat2 > Subcat3: 8900

6. Generate a new file where mrp is normalized. If there is a 0 or a non-float value or the key doesn't exist, make it "NA".



I begin by importing some coding dependencies. Here I created a class because I use some functions. The function method is very easy to read, and since I only use functions.
#import json
#from collections import Counter

I created global variables and some empty arrays. After that, I created a function to load the json data file. create a loop to add some fields to an empty array.
After that, I create variables . The types of variables are set. Because a set does not have duplicate values, I used a set data type for the first question.

For the second question, I created some arrays and functions. After collecting the data, with http_status is 200 in the array, and creating a for loop to find the price difference.

first question, like, create a variable as set and code for the required answer.

In the fifth section, create a for-loop with a function to add a category and subcategory and find the count of both.

For a sixth section, create a separate code file. create that file to normalise the mrp section with the loop concept  
