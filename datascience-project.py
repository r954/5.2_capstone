# Store the API key as a string - according to PEP8, constants are always named in all upper case
API_KEY = '4CxnW2Q4p7yiXmc1TQs6'

START_END = '2017-01-01'
END_DATE = '=2017-12-31'

# First, import the relevant modules
import requests

# into the JSON structure that will be returned
url = 'https://www.quandl.com/api/v3/datasets/FSE/AFX_X.json?start_date='+START_END+'&end_date='+END_DATE+'&api_key='+API_KEY
response  = requests.get(url)
response .json()['dataset'].keys()


if (response.status_code == 200):
    stock_dict =  response.json()
    stock_dict_keys =  response.json()['dataset'].keys()
    column_names = stock_dict['dataset']['column_names']
    data_list = stock_dict['dataset']['data']

    #print(response .json()['dataset'].keys())
    #print(stock_dict_keys)


else:
    print("Error fetching data")


# Dictionary -  keys: columns, values:list of values on all days
required_cols = ['Open', 'High','Low','Close','Traded Volume']
formatted_stock_dict = {}
for data in data_list:
    for col in required_cols:
        index_in_data = column_names.index(col)
        formatted_stock_dict.setdefault(col, []).append(data[index_in_data])
print(formatted_stock_dict)

opening_prices_sorted = list(filter(None,formatted_stock_dict['Open']))
opening_prices_sorted.sort()
print("The highest opening price:" , opening_prices_sorted[-1])
print("The lowest opening price:" , opening_prices_sorted[0])

high_low_diff_per_day = [formatted_stock_dict['High'][i] - formatted_stock_dict['Low'][i] for i in range(len(formatted_stock_dict['High']))]
high_low_diff_per_day.sort()
print("The largest change in any one day:",round(high_low_diff_per_day[-1],4))

close_diff = []
for i in range(len(formatted_stock_dict['Close'])-1):
    j = i+1
    diff = abs(formatted_stock_dict['Close'][i] - formatted_stock_dict['Close'][j])
    close_diff.append(diff)
close_diff.sort()
print("The largest change between any 2 days:", round(close_diff[-1],4))

avg_daily_traded_volume = sum(formatted_stock_dict['Traded Volume'])/len(formatted_stock_dict['Traded Volume'])
print("The average trading volume:", round(avg_daily_traded_volume,4))

def median(list_to_sort):
    if(len(list_to_sort)) > 1:
        list_to_sort.sort()
        mid_value = int(str(len(list_to_sort)/2).split(".")[0])
        if len(list_to_sort)%2 != 0:
            return list_to_sort[mid_value]
        else:
            second_index = mid_value
            first_index = second_index-1
            return (list_to_sort[first_index] + list_to_sort[second_index])/2
    else:
        print("Median does not exist")
        
median_trading_volume = median(formatted_stock_dict['Traded Volume'])
print("The median trading volume:",median_trading_volume)