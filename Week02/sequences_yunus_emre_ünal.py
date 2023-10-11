my_list=[1,2,3,4,5]
my_tuple=(1,5,7,9)
my_set={9,6,3,1}
my_dict={'Name':"Yunus"}

def remove_duplications(input_element:list) -> list:
    return list(set(my_list))


def list_counts(input_element: list) -> dict:
     my_dict_second={}
     for item in input_element:
          if my_dict_second.get(item):
               my_dict_second[item] += 1
          else:
              my_dict_second[item] = 1
     return my_dict_second

def reverse_dict(input_element: dict) ->dict:
      my_dict_third={}
      for key,value in input_element.items():
          my_dict_third[value]=key
      return my_dict_third

 

            
