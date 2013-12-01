# -*- coding: utf-8 -*-
                             
import re, urllib, urllib2
                             
class Xiami(object):
                             
    def __init__(self, url_song):
        self.url_song = url_song       
        self.url_xml = self.get_xml()
        self.info = self. get_info()
        self.loc = self.info[0]
        self.lyc = self.info[1]
        self.pic = self.info[2]
                                 
    def get_xml(self):
         return 'http://www.xiami.com/song/playlist/id/%s/object_name/default/object_id/0' % re.search('\d+', self.url_song).group()
                             
    def get_info(self):
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        req = urllib2.Request(
            url = self.url_xml,
            headers = headers
        )
        try:
            xml = urllib2.urlopen(req).read()
        except Exception, e:
            raise u'网络错误！，请重试！'
        location = re.search(r'(<location>)(.+)(<\/location>)', xml).group(2)
        lyc = re.search(r'(<lyric>)(.+)(<\/lyric>)', xml).group(2) 
        pic = re.search(r'(<pic>)(.+)(<\/pic>)', xml).group(2) 
        return (location, lyc, pic)
                             
    def get_url(self):
        strlen = len(self.loc[1:])
        rows = int(self.loc[0])
        cols = strlen / rows
        right_rows = strlen % rows
        new_str = self.loc[1:] 
        real_url = ''
                             
        for i in xrange(strlen):
            x = i % rows
            y = i / rows
            p = 0
            if x <= right_rows:
                p = x * (cols + 1) + y
            else:
                p = right_rows * (cols + 1) + (x - right_rows) * cols + y
            real_url += new_str[p]
        return urllib2.unquote(real_url).replace('^', '0')
                             
if __name__ == '__main__':
                             
    url = raw_input('please enter the url of the song: ')
    xi = Xiami(url)
    url_download = xi.get_url()
    url_pic = xi.pic
    url_lyc = xi.lyc
                             
    print u'下载地址是: %s' % url_download
                             
    print u"下载开始..."
                           
    try:
        urllib.urlretrieve(url_download, r'new.mp3')
        urllib.urlretrieve(url_pic, r'new.jpg')
        urllib.urlretrieve(url_lyc, r'new.lyc')
    except:
        raise(u'请求错误，请重试')
                                 
    print u"完成下载..."
