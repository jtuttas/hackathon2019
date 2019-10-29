from http.server import HTTPServer
def serve(handler):
    try:
        port = 80
        debugserver = HTTPServer(('', port), handler)
        print('Started httpserver on port', port)
        print('http://localhost:' + str(port))
        debugserver.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        debugserver.socket.close()