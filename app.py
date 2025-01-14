from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# # Define the path to the JSON file
# json_file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')

# print(json_file_path)
# # Load student marks from the JSON file
# def load_student_marks():
#     try:
#         with open(json_file_path, 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return [{"name": "Default", "marks": 0}] 

STUDENT_DATA = [{"name":"mGtnrgW","marks":88},{"name":"TRJKlmu","marks":43},{"name":"u","marks":69},{"name":"3yP83W4","marks":56},{"name":"L","marks":16},{"name":"UBz3EaIB6","marks":99},{"name":"k66y","marks":77},{"name":"8iGlXD13RX","marks":49},{"name":"rAzN","marks":21},{"name":"5qkAQLHc","marks":30},{"name":"yE9j","marks":19},{"name":"2kMMIXcq5t","marks":3},{"name":"Omyz2i","marks":10},{"name":"Ku1kl","marks":88},{"name":"dwB","marks":20},{"name":"vvE8W","marks":64},{"name":"18HMg","marks":53},{"name":"wFqwrDzTpx","marks":66},{"name":"rFuzI","marks":60},{"name":"g","marks":47},{"name":"hucjYl","marks":43},{"name":"ZlN","marks":81},{"name":"ahLvwo82","marks":40},{"name":"g6Vfcj","marks":79},{"name":"lbh","marks":2},{"name":"5r11hd","marks":97},{"name":"40ei5oXsR","marks":60},{"name":"Yv9SVAV","marks":10},{"name":"R2mJ4uow","marks":46},{"name":"posOG","marks":81},{"name":"A","marks":57},{"name":"m","marks":91},{"name":"buOS","marks":0},{"name":"1g1tlYFQ","marks":50},{"name":"JIwALn","marks":87},{"name":"RjEw5cLwfG","marks":49},{"name":"P0BFAduvpA","marks":0},{"name":"Jwb","marks":40},{"name":"a2Hb","marks":47},{"name":"pbv18J","marks":62},{"name":"Sne2WJw203","marks":12},{"name":"H2wXJDWTeD","marks":60},{"name":"fiWTR","marks":10},{"name":"p","marks":45},{"name":"dDpSb0WxH4","marks":71},{"name":"G2Fd0iCmV","marks":8},{"name":"P9I3i2","marks":80},{"name":"yNjpz","marks":50},{"name":"HWfAy0bTWn","marks":52},{"name":"uAy0ISpnr","marks":93},{"name":"F0","marks":18},{"name":"j","marks":22},{"name":"pBsk3Bp","marks":61},{"name":"JlUUBgh","marks":5},{"name":"cBjv","marks":58},{"name":"1GtR6Sn2","marks":97},{"name":"1HZHHWCN","marks":80},{"name":"JUWAah","marks":64},{"name":"cqRI","marks":74},{"name":"gXTLR","marks":92},{"name":"OOflZ","marks":57},{"name":"e7DN","marks":90},{"name":"scGPb2f","marks":13},{"name":"trT2POl","marks":58},{"name":"BWjO4Y8rPA","marks":30},{"name":"XMFT","marks":30},{"name":"e","marks":0},{"name":"1ty","marks":84},{"name":"mUeC0WGM6D","marks":31},{"name":"5pNOz3N","marks":33},{"name":"f6cxbm","marks":89},{"name":"I3fqEXb","marks":84},{"name":"Af4b7or","marks":59},{"name":"JzX5klv","marks":18},{"name":"pBmQav","marks":77},{"name":"HWg","marks":96},{"name":"F","marks":43},{"name":"jBCkA","marks":80},{"name":"w96uIbDs","marks":79},{"name":"yFmcUdHtuG","marks":0},{"name":"IIoEuZgd","marks":60},{"name":"oWcptbCN","marks":15},{"name":"wYOPA","marks":53},{"name":"PDscMU3SFJ","marks":26},{"name":"MQkX","marks":53},{"name":"6Vm4ya0","marks":6},{"name":"x","marks":9},{"name":"wx","marks":37},{"name":"b7kJ5fWRes","marks":57},{"name":"g4oqc4","marks":53},{"name":"Lt4d9","marks":23},{"name":"tBgS2nS4Tg","marks":65},{"name":"sNb","marks":53},{"name":"Pt53vAYb8l","marks":35},{"name":"z1K2","marks":19},{"name":"kgTiJvg","marks":21},{"name":"lL9ji0cYA3","marks":22},{"name":"ZBs","marks":59},{"name":"9RNcgRT","marks":85},{"name":"mv3UCNnZVH","marks":40}]
def load_student_marks():
    return STUDENT_DATA
@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def get_marks():
    # Get the list of names from the query string
    names = request.args.getlist('name')
    student_marks = load_student_marks()

    # Look for the student marks in the list of dictionaries
    marks = []
    for name in names:
        # Search for the student's mark based on the name
        student = next((item for item in student_marks if item["name"] == name), None)
        
        if student:
            marks.append(student["marks"])
        else:
            marks.append(f"Student {name} not found")

    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
