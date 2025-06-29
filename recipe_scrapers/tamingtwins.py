from ._abstract import AbstractScraper

class TamingTwins(AbstractScraper):
    @classmethod
    def host(cls):
        return "tamingtwins.com"