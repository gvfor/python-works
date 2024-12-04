original_dict={"item1":45, "item2":75, "item3":60, "item4":30}

filtered_dic={key:value for key, value in original_dict.items() if value>50}
print(filtered_dic)