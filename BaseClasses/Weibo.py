# python3
import json

class Weibo(object):
    def __init__(self,id,created_at=None,text=None,gps_lat=None,gps_lng=None,userid=None,time=None):
        self.wid = id
        self.created_at = created_at
        self.text = text
        self.gps_lat = gps_lat
        self.gps_lng = gps_lng
        self.userid = userid
        self.time = time

    def __str__(self):
        res_str = ""
        res_str += "{key:<15}:{value}".format(key="Weibo Id",value = self.wid)
        res_str += "{key:<15}:{value}".format(key="Created At",value = self.created_at)
        res_str += "{key:<15}:{value}".format(key="Location",value = "lat %.3f lng %.3f" % (float(self.gps_lat),float(self.gps_lng) ))
        res_str += "{key:<15}:{value}".format(key="User Id",value = self.userid)
        res_str += "{key:<15}:{value}".format(key="Time",value = self.time)
        res_str += "{key:<15}:{value}".format(key="Text",value = self.text)
        return res_str

    def __hash__(self):
        return self.wid
    
    def convert_to_json(self):
        return json.dumps(self.convert_to_dict())

    def convert_to_dict(self):
        return_dict = {}
        return_dict['wid'] = self.wid
        return_dict['created_at'] = self.created_at
        return_dict['text'] = self.text
        return_dict['gps_lat'] = self.gps_lat
        return_dict['gps_lng'] = self.gps_lng
        return_dict['userid'] = self.userid
        return_dict['time'] = self.time
        return return_dict


if __name__ == "__main__":
    pass
