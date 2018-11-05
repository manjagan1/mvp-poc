import pyRserve

# conn = pyRserve.connect(host='172.17.0.2', port=6311)
conn = pyRserve.connect(host='127.0.0.1', port=6311)
print(conn)
print(not conn.isClosed)

a = conn.eval('3 + 5')

print(a)

conn.close()

