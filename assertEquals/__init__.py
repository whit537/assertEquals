import logging

__author__ = "Chad Whitacre <chad@zetaweb.com>"
__version__ = "0.4.4"

if 0:
    format = "%(name)-16s %(levelname)-8s %(message)s"
    format = "%(asctime)s %(module)s:%(lineno)d %(message)s"
    logging.basicConfig( filename='/tmp/assertEquals.log'
                       , level=logging.DEBUG
                       , format=format
                        )
