
# the following to be run on scrapy shell

t = 0
for link in xrange(len(article_links)):
    fetch(article_links[link])
    r = response.css('div.Normal::text').extract()
    p = response.css('meta[itemprop="dateModified"]::attr(content)').extract()
    print p,r
    if r != [] and p != []:
        text = ' '.join(r).encode('utf-8')
        string = 'article_data/'+p[0]+'--'+str(t)+'.txt'
        f = open(string, 'w')
        f.write(text)
        f.close()
        t += 1
        print ''
        print 'an article has been extracted'
        print ''
        print t
    if t == 1000:
        break
    print link     

#batch size = 1000

# batch number-1
	#starting number - 0
	#ending number - 1138

# batch number-2
	#starting number - 1139
	#ending number - 
