import json
from collections import Counter
# 1.Number of Overlapped urlh
class dataweave:
    global tday, yday, tday_urlh, yday_urlh, tday_cat,yday_cat,tday_scat, yday_scat,today_file,yesterday_file,day
    tday, yday, tday_urlh, yday_urlh, tday_cat,yday_cat,tday_scat, yday_scat = [],[],[],[],[],[],[],[]

    def getJSON(file, day):
        with open(file, 'r+') as f:
            for line in f:
                day.append(json.loads(line))
        return day
    #subcat_today, subcat_yesterday = [], []
    today_file = getJSON('C:\\Users\dell\Downloads\DW_Json\\today.json.gz_out', tday)
    yesterday_file = getJSON('C:\\Users\dell\Downloads\DW_Json\\yesterday.json.gz_out', yday)
    def function_one(self):

      for item in today_file:
        tday_urlh.append(item['urlh'])
        tday_cat.append(item['category'])
        tday_scat.append(item['subcategory'])

      for item in yesterday_file:
        yday_urlh.append(item['urlh'])
        yday_cat.append(item['category'])
        yday_scat.append(item['subcategory'])

      a1=set(tday_urlh)
      a2=set(yday_urlh)
      a3=list(a1.intersection(a2))
      a4=len(a3)
      print("1. Number of overlapped urlh: ",a4)
      #print(a1)

    def function_two(self):
        # 2 .Price different
        global required_today_list,required_yesterday_list
        required_today_list,required_yesterday_list = [],[]

        for i in range(len(today_file)):
             if today_file[i]['http_status'] == "200":
                required_today_list.append(today_file[i])

        for j in range(len(yesterday_file)):
            if yesterday_file[j]['http_status'] == "200":
                required_yesterday_list.append(yesterday_file[j])

        global set_overlapped_urlh
        a1=set(tday_urlh)
        a2=set(yday_urlh)
        a3=list(a1.intersection(a2))
        set_overlapped_urlh = set(a3)

        print("2. Price differnces: ")

        for line_t in required_today_list[0:10000]:

            for line_y in required_yesterday_list[0:10000]:
                if line_t['urlh'] == line_y['urlh'] and line_t['urlh'] in set_overlapped_urlh:
                    t_price = line_t['available_price']
                    y_price = line_y['available_price']
                    if t_price != None and y_price != None:
                        t_price = float(t_price)
                        y_price = float(y_price)
                        if (type(t_price) == 'int' or type(t_price == 'float')) and (type(y_price) == 'int' or type(y_price == 'float')):
                            if t_price != y_price:
                                print("%.2f" %abs(t_price-y_price))
                                set_overlapped_urlh.remove(line_t['urlh'])
                    break



    # 3.unique categories in both file
    def function_three(self):
        global c1,c2,c3,c4
        c1= set(tday_cat)
        c2=set(yday_cat)
        c3=c1.intersection(c2)
        c4=len(c3)
        print("3. Number of unique categories in both files:",c4)


    #4. List of categories which is not overlapping
    def function_four(self):
        d1 = yday_cat + tday_cat
        d2=set(d1)
        d3=d2.difference(c3)
        d4=list(d3)
        print("4.List of categories which is not overlapping: ", d4)

    def function_five(self):

        global total_file,unique_cat,set_scat,dict_scat
        set_scat = set(tday_scat).intersection(yday_scat)
        total_scat = tday_scat + yday_scat
        total_file = today_file + yesterday_file
        dict_scat = Counter(total_scat)

        unique_cat = set(tday_cat).intersection(yday_cat)
        print("5. Taxonomies: ")

        for line in total_file:
            if line['category'] in unique_cat and line['subcategory'] in set_scat:
                print (line['category'] + " > " + line['subcategory'] + ": " + str(dict_scat[line['subcategory']]))
                set_scat.remove(line['subcategory'])

if __name__ == "__main__":

    obj_one=dataweave()
    obj_one.function_one()
    obj_one.function_two()
    obj_one.function_three()
    obj_one.function_four()
    obj_one.function_five()
