from Sniffer.Output.Message import Message
from Sniffer.Selectors import Selector
from Sniffer.Selectors.FTPServerSelector import FTPServerSelector
from Sniffer.Selectors.HTTPHostSelector import HTTPHostSelector
from Sniffer.Selectors.IPAddressSelector import IPAddressSelector
from Sniffer.Selectors.TwitterUsernameSelector import TwitterUsernameSelector


class Selectors:
    selectors = None

    def __init__(self) -> None:
        # We should be doing this dynamically. Scan all selectors within the Sniffer.Selectors module.
        self.selectors = [
            IPAddressSelector,
            HTTPHostSelector,
            TwitterUsernameSelector,
            FTPServerSelector
        ]

    def choose(self) -> Selector:
        for i, selector in enumerate(self.selectors):
            Message.info('{0}: {1}'.format(i, selector().get_name()))

        selector = self.selectors[int(Message.input('<Choose selector type (DNI)>: '))]

        return selector
