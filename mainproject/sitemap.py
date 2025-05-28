from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class TourismSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1

    def items(self):
        return ["signinpage", "signuppage", "homepage"]

    def location(self, item):
        return reverse( item) 
allsitemaps={"TourismApplinks": TourismSitemap}