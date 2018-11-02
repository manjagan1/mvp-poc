import pyRserve

conn = pyRserve.connect(host='172.17.0.2', port=6311)

a = conn.eval('3 + 5')

print(a)

