from .handler_base import HandlerBase
from shutil import rmtree


class Handler(HandlerBase):
    def do_job(self, path, item_name, handler_dict):
        rmtree(path)
        return "item {} removed from {}".format(item_name, path), False
