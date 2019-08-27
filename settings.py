# working directory
filepath = 'd:/test/'
rescan_interval = 2
notify_interval = 10

rules = [
    {
        "active": True,
        "item_type": ".txt",
        "handler": "handlers/rename_add_timestamp"
    },
    {
        "active": True,
        "item_type": ".png",
        "handler": "handlers/move",
        "value_1": "d:/test/tmp/"
    },
    {
        "active": True,
        "item_type": "folder",
        "handler": "handlers/delete"
    }
]