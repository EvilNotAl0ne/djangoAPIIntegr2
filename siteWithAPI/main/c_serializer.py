from struct import unpack

class SerializedObject:
    def __init__(self, ser):
        self.__dict__.update(ser)

class Serializer:
    def unpack(self, obj):
        if not isinstance(obj, dict):
            return None
        return SerializedObject(obj)

# class Serializer:
#     def __init__(self):
#         self.ser_queue = []
#
#     def unpack(self, obj):
#         return list(obj.values())
#
#     def unpack(self, obj):
#         _tmp =[]
#         if len(obj.keys()) > 1:
#             _tmp.append([[k,v] for k,v in obj.items()])
#         else:
#             _tmp.append([list(obj.keys())[0], list(obj.values())])
#
#         return _tmp
#
#     def recursice_unpack(self, obj):
#         if not isinstance(obj, dict):
#             return obj
#         for i in obj.values():
#             if not isinstance(i, dict):
#                 self.ser_queue.append(i)
#             else:
#                 unpack_ = self.unpack(i)
#                 print(unpack_)
#                 self.ser_queue.append(unpack_)
#                 if len(unpack_) > 1:
#                     self.recursice_unpack(unpack_[1])
#                 else:
#                     return self.ser_queue


