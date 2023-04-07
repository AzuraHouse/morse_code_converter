class DictSearch:
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def get_key_by_value(self, search_value):
        for key, value in self.my_dict.items():
            if value == search_value:
                return key
        else:  # If the value is not found int the dictionary
            return " "
