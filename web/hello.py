def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    query_string = environ.get('QUERY_STRING', "")
    res = (el + "\n" for el in query_string.split('&'))
    return res
