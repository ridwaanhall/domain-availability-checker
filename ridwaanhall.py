from fake_useragent import UserAgent
import requests

class RidwaanHallAPI:
    BASE_API = "https://websites-api.hostinger.com/api/"
    CATEGORIES = [
        "popular", "business", "international", "education", 
        "media_entertainment", "technology", "social_personal", 
        "professional_services", "miscellaneous"
    ]

    def __init__(self, domain_name):
        self.smo_url = self.BASE_API + "domain/search-more-options"
        self.sds_url = self.BASE_API + "domain/single-domain-search"
        self.domain_name = domain_name
        self.user_agent = UserAgent().random
        self.headers_global = {
            "Accept": "application/json",
            "Authorization": "Bearer www.hostinger.co.id",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent
        }

    def search_more_options(self, category="popular"):
        if category not in self.CATEGORIES:
            raise ValueError("Invalid category")

        tlds = self.get_tlds_for_category(category)
        
        payload_smo = {
            "domain_name": self.domain_name,
            "main_search_tld": "id",
            "tlds": tlds,
            "category": category,
            "with_promo": True
        }
        return requests.post(self.smo_url, json=payload_smo, headers=self.headers_global)

    def get_tlds_for_category(self, category):
        if category == "popular":
            return ["id", "com", "io", "online", "org", "store", "tech", "shop", "cloud", "site", "co.id", "blog", "co", "fun", "net", "click", "top", "icu", "ai", "pro"]
        elif category == "business":
            return ["com", "shop", "store", "biz", "company", "agency", "services", "consulting", "solutions", "management", "finance", "group", "marketing", "business", "support", "international", "works", "trade", "supply", "partners"]
        elif category == "international":
            return ["fr", "id", "es", "lt", "nl", "eu", "pl", "de", "me", "my.id", "co", "ch", "uk", "se", "pt", "ro", "it", "us", "org.in", "or.id"]
        elif category == "education":
            return ["edu", "ac.id", "academy", "education", "university", "institute", "college", "school", "research", "sch.id", "med.br", "ponpes.id"]
        elif category == "media_entertainment":
            return ["blog", "art", "media", "studio", "gallery", "blog.br", "music", "games", "tv", "film", "press", "news", "photo", "photography", "productions"]
        elif category == "technology":
            return ["tech", "io", "dev", "app", "systems", "digital", "technology", "software", "network", "info", "cloud", "web", "center", "solutions", "hosting", "email", "support", "consulting"]
        elif category == "social_personal":
            return ["fun", "life", "help", "community", "social", "family", "love", "blog", "club", "world", "support", "personal", "space", "dating", "art"]
        elif category == "professional_services":
            return ["biz", "pro", "services", "consulting", "agency", "solutions", "support", "marketing", "advertising", "management", "expert", "professional", "contractor"]
        elif category == "miscellaneous":
            return ["xyz", "top", "uno", "info", "me.uk", "mobi", "name", "asia", "wiki", "center", "wiki.br", "today", "cafe", "click", "cash", "bid", "cheap", "casino", "cool", "eco.br"]
        else:
            raise ValueError("Invalid category")

    def single_domain_search(self):
        payload_sds = {
            "domain_name": self.domain_name
        }
        return requests.post(self.sds_url, json=payload_sds, headers=self.headers_global)
