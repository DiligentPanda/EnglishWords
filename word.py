import configuration


class Word:

    def __init__(self, data):
        self.dataMap=dict([(configuration.headers[i],data[i]) for i in range(len(configuration.headers))])

    def __getitem__(self,key):
        return self.dataMap.get(key,"wrong key")

    def __setitem__(self, key, value):
        self.dataMap[key]=value

    def getData(self):
        data = [self.dataMap[key] for key in configuration.headers]
        for i in range(len(data)):
            if configuration.types[i] == configuration.TYPE_INT:
                data[i] = str(data[i])
        return data