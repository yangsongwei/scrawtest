import re

content='Hello 123 4567 World_This is a Regex Demo'

result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)

# print(result)
#
# print(result.group())

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

# pattern='<li.*?active.*?singer="(.*?)">(.*?)</a>'
#
# result=re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
#
# print(result.group(2))

content = '54aK54yr5oiR54ix5L2g'
content = re.sub('[a-z A-Z]', '', content)
print(content)