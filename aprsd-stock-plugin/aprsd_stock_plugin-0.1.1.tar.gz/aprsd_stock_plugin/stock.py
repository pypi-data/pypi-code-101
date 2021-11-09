import logging
import re

import yfinance as yf
from aprsd import plugin, trace

import aprsd_stock_plugin


LOG = logging.getLogger("APRSD")


class YahooStockQuote(plugin.APRSDRegexCommandPluginBase):

    version = aprsd_stock_plugin.__version__

    # Look for any command that starts with s or S
    command_regex = "^[sS]"

    # the command is for ?
    command_name = "stock"

    enabled = False

    def setup(self):
        # Do some checks here?
        self.enabled = True

    @trace.trace
    def process(self, packet):
        LOG.info(self.__class__.__name__)

        # fromcall = packet.get("from")
        message = packet.get("message_text", None)
        # ack = packet.get("msgNo", "0")

        a = re.search(r"^.*\s+(.*)", message)
        if a is not None:
            searchcall = a.group(1)
            stock_symbol = searchcall.upper()
        else:
            reply = "No stock symbol"
            return reply

        LOG.info(f"Fetch stock quote for '{stock_symbol}'")

        try:
            stock = yf.Ticker(stock_symbol)
            reply = "{} - ask: {} high: {} low: {}".format(
                stock_symbol,
                stock.info["ask"],
                stock.info["dayHigh"],
                stock.info["dayLow"],
            )
        except Exception as e:
            LOG.error(
                f"Failed to fetch stock '{stock_symbol}' from yahoo '{e}'",
            )
            reply = f"Failed to fetch stock '{stock_symbol}'"

        return reply.rstrip()
