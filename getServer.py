import socket
import sys
import joinFunc

HOST = ""   # Symbolic name meaning all available interfaces
PORT = 5080

url = rb"%5C%22%20role%3D%5C%22soldier%5C%22%20personaref%3D%5C%22%25ZID%25%5C%22%20levelmode%3D%5C%22mp%5C%22%20logintoken%3D%5C%22WAHAHA_IMMA_ZLO_TOKEN%5C%22%3E%3C%2Fdata%3E%22"
urlc = rb"http://localhost:5080/ZLO/run?game=Z.BF3&cmd=-webMode%20MP%20-Origin_NoAppFocus%20-loginToken%20WAHAHA_IMMA_ZLO_TOKEN%20-requestState%20State_ClaimReservation%20-requestStateParams%20%22%3Cdata%20putinsquad%3D%5C%22true%5C%22%20gameid%3D%5C%22"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')
s.listen(10)

conn, addr = s.accept()

print('Socket now listening')
conn.send(bytearray(url + rb"6" + url))