from os import rename, mkdir
from .handler_base import HandlerBase


class Handler(HandlerBase):
    def do_job(self, path, item_name, handler_dict):
        path_to_new_folder = handler_dict["value_1"]
        new_path = path_to_new_folder + item_name
        mkdir(path_to_new_folder)
        rename(path, new_path)
        return "item {} moved from {} to {}".format(item_name, path, new_path), new_path
