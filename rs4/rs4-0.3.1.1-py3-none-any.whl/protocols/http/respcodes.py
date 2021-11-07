responses = {
		100: "Continue",
		101: "Switching Protocols",
		200: "OK",
		201: "Created",
		202: "Accepted",
		203: "Non-Authoritative Information",
		204: "Deleted",
		205: "Reset Content",
		206: "Partial Content",
		300: "Multiple Choices",
		301: "Moved Permanently",
		302: "Moved Temporarily",
		303: "See Other",
		304: "Not Modified",
		305: "Use Proxy",
		306: "Switch Proxy",
		307: "Temporary Redirect",
		308: "Permanent Redirect",
		400: "Bad Request",
		401: "Unauthorized",
		402: "Payment Required",
		403: "Forbidden",
		404: "Not Found",
		405: "Method Not Allowed",
		406: "Not Acceptable",
		407: "Proxy Authentication Required",
		408: "Request Timeout",
		409: "Conflict",
		410: "Gone",
		411: "Length Required",
		412: "Precondition Failed",
		413: "Request Entity Too Large",
		414: "Request-URI Too Large",
		415: "Unsupported Media Type",
		416: "Range Not Satisfiable",
		500: "Internal Server Error",
		501: "Not Implemented",
		502: "Bad Gateway",
		503: "Service Unavailable",
		504: "Gateway Time-out",
		505: "HTTP Version Not Supported",
		506: "Proxy Error",
		507: "Failed Establishing Connection",
		530: "Parameter Mismatch",
		700: "Socket Error",
		701: "Exception Occured",
		702: "Socket Timeout",
		703: "Socket Panic",
		704: "DNS Not Found",
		705: "Entered Shutdown Process",
		706: "Unknown Authedentification Method",
		707: "HTTP Entity Error",
		708: "No Data Recieved",
		709: "Invalid Content",
		710: "Channel Closed",
		711: "Redirect Error",
		712: "Controlled Shutdown",
		713: "SSL Handshake Failure",
		714: "Connection Failure",
		715: "Response Header Error",
		716: "Protocol Switching Failure",
		717: "Invalid Cotennt Type",
		718: "Unacceptable Content Type",
		719: "Too Large Content",
		720: "HTTP2 Connection Closed",
		721: "HTTP2 Stream Reset",
		722: "Object Timeout"
}

def get (code, default = "Undefined Error"):
	return responses.get (code, default)


