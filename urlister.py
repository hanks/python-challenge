from sgmllib import SGMLParser

class URLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []
        
    def start_a(self, attrs):
        href = [v for k, v in attrs if k == "href"]
        if href:
            self.urls.extend(href)
            
    def getUrl(self):
        return self.urls
    
    def start_peakhell(self, attrs):
        href = [v for k, v in attrs if k == "src"]
        if href:
            self.urls.extend(href)