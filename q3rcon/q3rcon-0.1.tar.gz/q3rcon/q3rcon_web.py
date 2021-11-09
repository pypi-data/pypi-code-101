#!/usr/bin/env python3

import argparse
import http.server
import logging
import os
import pkg_resources
import q3rcon
import string
import urllib


class RconHTTPServer(http.server.HTTPServer):
    def __init__(self, server_address, RequestHandlerClass, rconsole):
        http.server.HTTPServer.__init__(self, server_address, RequestHandlerClass)
        self.cache = {}
        self.rconsole = rconsole
    

class RconHandler(http.server.BaseHTTPRequestHandler):
    
    class Templates:

        def page(self, **kwargs):
            page_template = pkg_resources.resource_string(__name__, 'data/templates/page.html').decode()
            return string.Template(page_template).substitute(**kwargs)
            
        def map(self, name):
            map_template = pkg_resources.resource_string(__name__, 'data/templates/map.html').decode()
            return string.Template(map_template).substitute(
                href="javascript:run('map %s')" % name,
                name=name
            )

        def index(self):
            def mapnames():
                def irange(start, stop):
                    return range(start, stop + 1)
                return \
                    ["q3dm%s" % i for i in irange(1, 19)] + \
                    ["q3tourney%s" % i for i in irange(1, 6)] + \
                    ["q3ctf%s" % i for i in irange(1, 4)]
            return self.page(
                title="q3rcon",
                body="".join([self.map(name=name) for name in mapnames()])
            )
    
    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        
        if url.path.startswith("/static"):
            self.send_response(200)
            self.end_headers()
            
            if url.path in self.server.cache:
                content = self.server.cache[url.path]
            else:
                # filepath = os.path.join(os.path.dirname(__file__), url.path[1:])
                # content = open(filepath, 'rb').read()
                content = pkg_resources.resource_string(__name__, os.path.join("data", url.path[1:]))
                self.server.cache[url.path] = content
            self.wfile.write(content)
        
        elif url.path.startswith("/run"):
            def allowed_cmd():
                return ["map"]

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            query = urllib.parse.parse_qs(url.query)
            if "cmd" in query:
                cmd = query["cmd"][0]
                if cmd.split()[0] in allowed_cmd():
                    self.server.rconsole.run(cmd)
                
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self.Templates().index().encode())


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--verbose', action='store_true')
        
    group1 = parser.add_argument_group("rcon", description="Quake 3 server")
    group1.add_argument("--rcon_host", type=str, default="localhost", help="Hostname or IP address")
    group1.add_argument("--rcon_port", type=int, default=27960, help="UDP port")
    group1.add_argument("--rcon_password", type=str, default="", help="Passport")
    
    group2 = parser.add_argument_group("http", description="Web rcon")
    group2.add_argument("--http_host", type=str, default="0.0.0.0", help="Hostname or IP address")
    group2.add_argument("--http_port", type=int, default=9344, help="UDP port")
    args = parser.parse_args()
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    rcon_args = {k.split("_")[1]:v for (k,v) in vars(args).items() if k.startswith("rcon") and v is not None}
    rconsole = q3rcon.Rcon(**rcon_args)
    rconsole.connect()

    client_address = (args.http_host, args.http_port)
    httpd = RconHTTPServer(client_address, RconHandler, rconsole)
    try:
        logging.info("HTTPServer listening on: %s:%s" % client_address)
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


if __name__ == '__main__':
    main()
