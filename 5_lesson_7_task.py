import json

sum_profit = int()

end_list = []

with open('file_7_task.txt', 'r', encoding='UTF-8') as file:
    end_list_dict_firm = {}
    for line in file:
        firm_info_list = line.split(' ')
        end_list_dict_firm[firm_info_list[0]] = int(firm_info_list[2]) - int(firm_info_list[3])
        sum_profit += int(firm_info_list[2]) - int(firm_info_list[3])
    end_list.append(end_list_dict_firm)
    end_list.append({'average_profit': sum_profit})

with open('file_7_task.json', 'w') as file:
    json.dump(end_list, fp=file)
