
# the following to be run on scrapy shell
'''
t = 0
for link in xrange(len(article_links)):
    fetch(article_links[link])
    r = response.css('div.Normal::text').extract()
    p = response.css('meta[itemprop="dateModified"]::attr(content)').extract()
    print p,r
    if r != [] and p != []:
        text = ' '.join(r).encode('utf-8')
        string = 'article_data/'+p[0]+'->'+str(link+1)+'.txt'
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

'''

#batch size = 1000

# batch number-1
	#starting number - 0
	#ending number - 1138

# batch number-2
	#starting number - 1139
	#ending number - 2314

# batch number-3
	#starting number - 2314
	#ending number - 3424

# batch number-4
	#starting number - 3424
	#ending number - 4582

# batch number -5
	#starting number - 4582
	#ending number - 5692

# batch number -6
	#starting number - 5692
	#ending number - 6848

# batch number -7
	#starting number - 6848
	#ending number - 7961

# batch number - 8
	#starting number - 7961
	#ending number - 9112

# batch number - 9
	#starting number - 9112
	#ending number - 10316

# batch number - 10
	#starting number - 10316
	#ending number - 11446

# batch number - 11
	#starting number - 11446
	#ending number - 12611

# batch number - 12
	#starting number - 12611
	#ending number - 13694

# batch number - 13
	#starting number - 13694
	#ending number - 14850


# batch number - 14
	#starting number - 15966
	#ending number - 17098

# batch number - 15
	#starting number - 17098
	#ending number - 18187

# batch number - 15
	#starting number - 18187
	#ending number - 19311	

# batch number - 16
	#starting number - 19311
	#ending number - 20455


# batch number - 16
	#starting number - 20455
	#ending number - 21619

# batch number - 16
	#starting number - 21619
	#ending number - 












