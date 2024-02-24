list_objs = [
    {
        "id":1,
        "name":"Ken"
    },{
        "id":2,
        "name":"dllewwe"
    },{
        "id":3,
        "name":"dslsd"
    }
]

with open(f"csva.csv","w") as f:
            header = list(list_objs[0].keys() if list_objs else [])
            newstr = ",".join([attr for attr in header])
            f.write(newstr+"\n")
            newli = ""

            for obj in list_objs:
                newstr = ",".join(str(obj[attr]) for attr in header)
                f.write(newstr+ "\n")