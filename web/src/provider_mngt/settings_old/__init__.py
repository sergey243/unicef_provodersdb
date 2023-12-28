import socket

if socket.gethostname() in ["serge-Latitude-5490",'localhost.localdomain']:
    from .dev import *
else:
    from .prod import *