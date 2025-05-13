from json2xml import json2xml
import json

# Sample JSON data
json_data = {
    "widget": {
        "debug": "on",
        "window": {
            "name": "main_window",
            "width": 640,
            "height": 480
        },
        "image": {
            "src": "Images/Sun.png",
            "name": "sun1",
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
        },
        "text": {
            "data": "Click Here",
            "size": 36,
            "style": "bold",
            "name": "text1",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
        }
    }
}

# Convert JSON to XML
data = json2xml.Json2xml(json_data)

# Print the XML output
print(data.to_xml())

#writing data to xml file after converting json into xml
with open("xml_data_file.xml", "w") as xml_file:
		xml_file.write(data.to_xml())


