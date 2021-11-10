from onebrain.exceptions import OnebrainException, INVALID_PARAMETER_VALUE


class OneflowHostCreds(object):
    def __init__(
        self,
        host,
        username=None,
        password=None,
        token=None,
        ignore_tls_verification=False,
        client_cert_path=None,
        server_cert_path=None,
    ):
        if not host:
            raise OnebrainException(
                message="host is a required parameter for OneflowHostCreds",
                error_code=INVALID_PARAMETER_VALUE,
            )
        if ignore_tls_verification and (server_cert_path is not None):
            raise OnebrainException(
                message=(
                    "When 'ignore_tls_verification' is true then 'server_cert_path' "
                    "must not be set! This error may have occurred because the "
                    "'ONEBRAIN_TRACKING_INSECURE_TLS' and 'ONEBRAIN_TRACKING_SERVER_CERT_PATH' "
                    "environment variables are both set - only one of these environment "
                    "variables may be set."
                ),
                error_code=INVALID_PARAMETER_VALUE,
            )
        self.host = host
        self.username = username
        self.password = password
        self.token = token
        self.ignore_tls_verification = ignore_tls_verification
        self.client_cert_path = client_cert_path
        self.server_cert_path = server_cert_path