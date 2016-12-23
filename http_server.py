import socket
import sys
import threading

#inisialisasi
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#proses binding
server_address = ('localhost', 8011)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#listening
sock.listen(1)

def response_hal_depan():
	filedepan = open('index.html','r').read()
	panjang = len(filedepan)
	
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/html; charset=utf-8\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filedepan)
	return hasil

def response_hal_wrong():
	filedirect = open('wrong.html','r').read()
	panjang = len(filedirect)

	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: text/html; charset=utf-8\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filedirect)
	return hasil

def response_video_mp4():
	filevideo = open('vidmp4','r').read()
	panjang = len(filevideo)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: video/mp4\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filevideo)
	return hasil

def response_video_flv():
	filevideo = open('vidflv','r').read()
	panjang = len(filevideo)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: video/x-flv\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filevideo)
	return hasil

def response_video_3gp():
	filevideo = open('vid3gp','r').read()
	panjang = len(filevideo)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: video/3gp\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filevideo)
	return hasil

def response_icon():
	filegambar = open('myicon.png','r').read()
	panjang = len(filegambar)
	hasil = "HTTP/1.1 200 OK\r\n" \
		"Content-Type: image/png\r\n" \
		"Content-Length: {}\r\n" \
		"\r\n" \
		"{}" . format(panjang, filegambar)
	return hasil

def response_redirect():
	hasil = "HTTP/1.1 301 Moved Permanently\r\n" \
		"Location: {}\r\n" \
		"\r\n"  . format('http://www.its.ac.id')
	return hasil


#fungsi melayani client
def layani_client(koneksi_client,alamat_client):
    try:
       print >>sys.stderr, 'ada koneksi dari ', alamat_client
       request_message = ''
       while True:
           data = koneksi_client.recv(64)
	   data = bytes.decode(data)
           request_message = request_message+data
	   if (request_message[-4:]=="\r\n\r\n"):
		break

       baris = request_message.split("\r\n")
       baris_request = baris[0]
       print baris_request
 	
       a,url,c = baris_request.split(" ")
       
       
       if (url=='/front'):
          respon = response_hal_depan()
       elif (url=='/front/videomp4'):
          respon = response_video_mp4() 
       elif (url=='/front/videoflv'):
          respon = response_video_flv() 
       elif (url=='/front/video3gp'):
          respon = response_video_3gp()
	else:
          respon = response_hal_wrong()
       koneksi_client.send(respon)
    finally:
        # Clean up the connection
        koneksi_client.close()


while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    koneksi_client, alamat_client = sock.accept()
    s = threading.Thread(target=layani_client, args=(koneksi_client,alamat_client))
    s.start()


