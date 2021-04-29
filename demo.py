
import json
import datetime
import time

def test_data():
    today = datetime.date.today()
    today = str(today)
    print(today)

    date = datetime.date(2022, 1, 1)
    date = str(date)
    print(str(date))

    print(today > date)

def test_json():
    data=dict()
    data['ip']="127.0.0.1"
    data["port"]=34;
    data=json.dumps(data)
    print(type(data))

def test_str_to_arr():
    dsa="[2,3,4,5]"
    dsa=dsa[1:-1].split(',')
    dsa=list(map(int,dsa))
    print(dsa)
    print(type(dsa))
    print(dsa[2])


if __name__ == '__main__':
    # # dat=' {"server_ip": "127.0.0.1", "server_pub_key": [7187, 61467355717], "vaild_date": "2022-01-01"}'
    s="abcd"
    print(ord(s[0]))
    # dat=' {"server_ip": "127.0.0.1", "server_pub_key": [7187, 61467355717], "vaild_date": "2022-01-01"} '
    # print("dsadsa:",dat)


