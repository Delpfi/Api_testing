from api.client import Client


class HttpBinApi(Client):
    HTML = '/html'
    BASE_URL = 'https://httpbin.org'
    HTML_ROBOTS = '/robots.txt'
    HTML_IP = '/ip'
    TIME = '/delay'
    def list_html(self):
        url = self.BASE_URL + self.HTML
        return self.get(url)

    def get_robots(self):
        url = self.BASE_URL + self.HTML_ROBOTS
        return self.get(url)

    def get_ip(self):
        url = self.BASE_URL + self.HTML_IP
        return self.get(url)

    def time_out(self, delay = 1):
        url = self.BASE_URL + self.TIME + f'/3'
        try:
            return self.get(url, timeout=delay)
        except Exception as ex:
            return False,ex
#т.к не будет разных объектов, с разными свойства(нет иницелизации в классе) , то можно создать сразу объект и к нему обращаться.
http_bin_api = HttpBinApi()