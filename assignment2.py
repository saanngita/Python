data = [
    {
        "name":"Sangam",
        "type":[
            {
                "name":"NTC",
                "number":986652
            },
           

        ]
    },
     {
        "name":"Sudan",
        "type":[
            {
                "name":"NTC",
                "number":9844906571
            },
            {
                "name":"Ncell",
                "number":9806245117
            },
             {
                "name":"Smart cell",
                "number":0
            }

    ]
}
]
list_data = data[0]
name = list_data['name']
print(name)
dict_data = list_data['type']
for i in dict_data:
    print(f"{i['name']} number of {name} is {i['number']}")
for i in data:
    name = i['name'] 
    dict_data = i['type']
    for i in dict_data:
        print(f"{i['name']} number of {name} is {i['number']}") 