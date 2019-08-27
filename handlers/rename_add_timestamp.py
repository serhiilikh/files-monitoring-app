from os import rename
from .handler_base import HandlerBase
from time import time


class Handler(HandlerBase):
    def do_job(self, path, item_name, handler_dict):
        ts = str(int(time()))
        item_name_list = item_name.split(sep=".")
        if len(item_name_list) > 1:
            item_name_list[-2] = item_name_list[-2] + "_" + ts
            new_name = ""
            for string in item_name_list:
                new_name += string + "."
            new_name = new_name[:-1]
        else:
            new_name = item_name + "_" + ts
        # we reverse string to rename only one (last) name, because it can occur early,
        # eg. "c:/test/test" -> "c:/test/test123456"
        reversed_string = lambda x: x[::-1]
        item_name = reversed_string(item_name)
        new_name = reversed_string(new_name)
        new_path = reversed_string(path).replace(item_name, new_name)
        new_path = reversed_string(new_path)
        rename(path, new_path)
        return "item {} renamed to {} - {}".format(item_name, new_name, handler_dict["handler"]), new_path
