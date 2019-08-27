# files-monitoring-app
An application for monitoring file system events in certain directory. There are three types of handlers:
- move to directory
- delete
- rename by adding timestamp to name
## Getting started
To run the application, use (for Linux)
```bash
sudo python3 main.py
```
or run it as an administrator (for Windows). You will get output from app in terminal
- the end of first scan (it can take longer then average because app needs to wait before all being written files are ready)
- changes and new files added
- detailed information about handlers job (you can configure interval in settings.py)
#### Configuring settings.py

- workdir - defines working directory 
- rescan_interval - defines how frequently app will scan working directory for changes

- notify_interval - defines how frequently app will give user output from handlers

Here is the example of rule for handler

```python
{
    "active": True,
    "item_type": ".png",
    "handler": "handlers/move",
    "value_1": "d:/test/tmp/"
}
```
- active - defines if app will use this rule, useful for storing rarely-used rules

- item_type - defines type of the item, options are:
    - file format, usage: ".jpg", ".png", ".txt"
    - folder, usage: "folder"
    - linkj, usage: "link"

- handler - path to python handler script

- additional parameters - all parameters are sent to handler, so you can define your parameters and then use them in your script, for example, here i used value_1 as destination_folder for "move" handler

#### How to add new handlers
1. add handler script to main script dir or subdir
2. add usage of your handler to settings.py
