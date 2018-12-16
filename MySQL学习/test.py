import re
info = """<div id="info">
        <span ><span class='pl'>导演</span>: <span class='attrs'><a href="/celebrity/1047973/" rel="v:directedBy">弗兰克·德拉邦特</a></span></span><br/>
        <span ><span class='pl'>编剧</span>: <span class='attrs'><a href="/celebrity/1047973/">弗兰克·德拉邦特</a> / <a href="/celebrity/1049547/">斯蒂芬·金</a></span></span><br/>
        <span class="actor"><span class='pl'>主演</span>: <span class='attrs'><a href="/celebrity/1054521/" rel="v:starring">蒂姆·罗宾斯</a> / <a href="/celebrity/1054534/" rel="v:starring">摩根·弗里曼</a> / <a href="/celebrity/1041179/" rel="v:starring">鲍勃·冈顿</a> / <a href="/celebrity/1000095/" rel="v:starring">威廉姆·赛德勒</a> / <a href="/celebrity/1013817/" rel="v:starring">克兰西·布朗</a> / <a href="/celebrity/1010612/" rel="v:starring">吉尔·贝罗斯</a> / <a href="/celebrity/1054892/" rel="v:starring">马克·罗斯顿</a> / <a href="/celebrity/1027897/" rel="v:starring">詹姆斯·惠特摩</a> / <a href="/celebrity/1087302/" rel="v:starring">杰弗里·德曼</a> / <a href="/celebrity/1074035/" rel="v:starring">拉里·布兰登伯格</a> / <a href="/celebrity/1099030/" rel="v:starring">尼尔·吉恩托利</a> / <a href="/celebrity/1343305/" rel="v:starring">布赖恩·利比</a> / <a href="/celebrity/1048222/" rel="v:starring">大卫·普罗瓦尔</a> / <a href="/celebrity/1343306/" rel="v:starring">约瑟夫·劳格诺</a> / <a href="/celebrity/1315528/" rel="v:starring">祖德·塞克利拉</a> / <a href="/celebrity/1014040/" rel="v:starring">保罗·麦克兰尼</a> / <a href="/celebrity/1390795/" rel="v:starring">芮妮·布莱恩</a> / <a href="/celebrity/1083603/" rel="v:starring">阿方索·弗里曼</a> / <a href="/celebrity/1330490/" rel="v:starring">V·J·福斯特</a> / <a href="/celebrity/1000635/" rel="v:starring">弗兰克·梅德拉诺</a> / <a href="/celebrity/1390797/" rel="v:starring">马克·迈尔斯</a> / <a href="/celebrity/1150160/" rel="v:starring">尼尔·萨默斯</a> / <a href="/celebrity/1048233/" rel="v:starring">耐德·巴拉米</a> / <a href="/celebrity/1000721/" rel="v:starring">布赖恩·戴拉特</a> / <a href="/celebrity/1333685/" rel="v:starring">唐·麦克马纳斯</a></span></span><br/>
        <span class="pl">类型:</span> <span property="v:genre">剧情</span> / <span property="v:genre">犯罪</span><br/>
        
        <span class="pl">制片国家/地区:</span> 美国<br/>
        <span class="pl">语言:</span> 英语<br/>
        <span class="pl">上映日期:</span> <span property="v:initialReleaseDate" content="1994-09-10(多伦多电影节)">1994-09-10(多伦多电影节)</span> / <span property="v:initialReleaseDate" content="1994-10-14(美国)">1994-10-14(美国)</span><br/>
        <span class="pl">片长:</span> <span property="v:runtime" content="142">142分钟</span><br/>
        <span class="pl">又名:</span> 月黑高飞(港) / 刺激1995(台) / 地狱诺言 / 铁窗岁月 / 消香克的救赎<br/>
        <span class="pl">IMDb链接:</span> <a href="http://www.imdb.com/title/tt0111161" target="_blank" rel="nofollow">tt0111161</a><br>

</div>




                </div>"""
#director = re.search(r'导演:.*\s主演|导演:.*\.{3}',info).group()[3:-3].strip()

#print(director)

#actors = re.search(r'主演.*\.|\.',info).group()[4:-3].strip('/').strip()
#year = re.search(r'\d+',info).group()
cuntry = re.search(r'制片国家/地区:</span>(.+?)<br/>',info).group()[16:-5].strip()
#type = re.search(r'/\s[^/]+\s{50}',info).group()[2:].strip()
#print(actors,'\n',year,'\n',cuntry,'\n',type)
print(cuntry)