'''
using the JSON provided, 
1. read it into a python script as a python dictionary (of dictionaries)
2. drill down and edit ["image"]["name"] "moon1"
3. drill down and edit ["image"]["src"] "Images/Moon.png"
4. this will also requre an edit in ["text"]["onmouseup"]
5. write the modified widget to a NEW JSON file modified-widget.json
you should be able to solve this in 7 LOC
'''
import json
# open json file for modification
with open("widget.json") as widget_file:
    # read contents into a Python dictionary
    print(type(widget_file))
    print(widget := json.load(widget_file))#loads cannot work with TextIOWrapper object

# edit python steps 2-4
widget["widget"]["image"]["name"] = "moon1"
widget["widget"]["image"]["src"] = "Images/Moon.png"
# widget["widget"]["text"]["onMouseUp"] = "moon1.opacity = (moon1.opacity / 100) * 90;"
widget["widget"]["text"]["onMouseUp"] = widget["widget"]["text"]["onMouseUp"].replace("sun1", "moon1")

# step 5 write modified python to new json file
with open("modified-widget.json", mode="w") as modified_widget_file:
    # json.dump(widget, modified_widget_file)
    json.dump(widget, modified_widget_file, indent=4)
