original_dic={"a":-5, "b":10, "c":-3, "d":7}

abs_dict={key:abs(value) for key,value in original_dic.items()}

print("dictionary with absolute values:",abs_dict)