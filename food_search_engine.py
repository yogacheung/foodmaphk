import json
import math
import re

class Food_Search_Engine:
    # original data from crawled json file
    original_data = []
    # the result after filter/ranking/similarity
    query_result = []
    # more data structures can be added here    
    def __init__(self, json_file_name):
        self.load_data(json_file_name)
        self.reset()
    def load_data(self, json_file_name):
        # we provide the code
        with open(json_file_name) as json_file:
            self.original_data = json.load(json_file)

    def filter(self, filter_cond):
        self.query_result = []               
        for original in self.original_data:  
            #print(original.items())          
            for item_key, item_value in original.items(): 
                #print(item_key, item_value)               
                for key, value in filter_cond.items():
                    #print(key, value) 
                    check = len(filter_cond)
                    if key in item_key and key in "rating":                                            
                        if value >= item_value:
                            #print(value)                                                    
                            check = check - 1                            
                    elif key in item_key and key in "price-range":                                            
                        price =  re.match( r'(\d+)-(\d+)', value, re.M|re.I)
                        oprice =  re.match( r'(\d+)-(\d+)', item_value, re.M|re.I)
                        if oprice:
                            #print(value)
                            if price.group(1) >= oprice.group(1) and price.group(2) <= oprice.group(2):                                
                                check = check - 1
                        else:                            
                            oprice =  re.match( r'(\w+) \$(\d+)', item_value, re.M|re.I)
                            if oprice:
                                if oprice.group(1) in "Above":                                
                                    if price.group(1) >= oprice.group(2) and 1000 <= oprice.group(2):                                    
                                        check = check - 1
                                else:
                                    if price.group(1) >= 0 and oprice.group(2) <= oprice.group(2):                                        
                                        check = check - 1
                    elif key in item_key:
                        if item_value in value:
                            #print(item_value)                            
                            check = check - 1               
                if check == 1:
                    self.query_result.append(original)                       

    def rank(self, ranking_weight):     
        #print(len(self.query_result))                   
        for pt in range(1, len(self.query_result)):            
            curvalue = self.query_result[pt]
            pos = pt
            v1 = 0
            v2 = 0
            v3 = 0
            v4 = 0            
            for key, value in curvalue.items():          
                if(key in "rating"): 
                    v1 = value
                if(key in "address"): 
                    v2 = math.sqrt(pow(value[0]-22.417875,2)+pow(value[1]-114.207263,2))
                if(key in "price_range"): 
                    price =  re.match( r'(\d+)-(\d+)', vlaue, re.M|re.I)                    
                    if price:                        
                        v3 = (price.group(1) + price.group(2))/2
                    else:                            
                        price =  re.match( r'(\w+) \$(\d+)', item_value, re.M|re.I)
                        if oprice.group(1) in "Above":                                
                            v3 = (price.group(2) + 1000)/2
                        else:
                            v3 = price.group(2)/2

                if(key in "reviews"): 
                    v4 = value[2]/(value[0]+value[1]+value[2])
            cw = ranking_weight[0]*v1 + ranking_weight[1]*v2 + ranking_weight[2]*1 + ranking_weight[3]*v4
            #print(cw)
            #print(pt, "---->")
            while pos > 0:                
                frontvalue = self.query_result[pos-1]            
                for key, value in frontvalue.items():            
                    if(key in "rating"): 
                        v1 = value
                    if(key in "address"):
                        v2 = math.sqrt(pow(value[0]-22.417875,2)+pow(value[1]-114.207263,2))
                    if(key in "price_range"): 
                        v3 = 1.0
                    if(key in "reviews"):
                        v4 = value[2]/(value[0]+value[1]+value[2])
                fw = ranking_weight[0]*v1 + ranking_weight[1]*v2 + ranking_weight[2]*1 + ranking_weight[3]*v4
                #print(cw, fw)
                if(cw > fw):
                    self.query_result[pos] = self.query_result[pos-1]
                pos = pos - 1
            #print(pos, curvalue)                    
            self.query_result[pos] = curvalue
            
    def find_similar(self, restaurant, similarity_weight, k):        
        print('Optional')

    def print_query_result(self):        
        print(self.query_result)

    def reset(self):        
        self.query_result = self.original_data


search = Food_Search_Engine("openrice_data.json")
#filter_data = {'name': ['Chan Kun Kee', 'PizzaExpress'], 'name_contains': ['Chan Kun', 'Pai Dong'], 'district': 'Mong Kok', 'price-range': '51-200', 'rating': 3.0, 'cuisine': ['Guangdong', 'Indian']}
filter_data = {'district': 'Sha Tin', 'price-range': '50-100'}
search.filter(filter_data)
rank_data = [1, 0, -0.02, -1]
search.rank(rank_data)
#search.find_similar()
search.print_query_result()