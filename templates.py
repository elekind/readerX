import requests
from bs4 import BeautifulSoup

def TheEconomist (link, headers):
    r = requests.get("https://archive.is/latest/" + link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    soup = soup.article.div.div
    for i in soup.find(string="■").find_all_next(True):  #delete everything after ■.
        i.decompose()
    
    soup.aside.decompose()
    return soup.prettify()

def TheHindu (link, headers):
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    """ soup = soup.find(class_ = 'mt-4') """
    """ soup = soup.div.div.div """
    
    for tag in soup.find(id = "arthardpv").find_previous('p').find_all_next(True):
        tag.decompose()
        #tag.clear()

    for tag in soup.find_all(class_ = "also-read print-hide"):
        tag.decompose()
        #tag.clear()

    #for tag in soup.find(class_ = 'mt-4').find_previous_siblings(True):
        #tag.decompose()
        #tag.clear()    

    soup.header.decompose()
    soup.section.decompose()
    #soup.find(class_ = "header-end").decompose()

    #clear() everything after comments. """

    return soup.prettify()

def IndianExpress (link, headers):
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    #use p tags and siblings instead
    soup.footer.decompose()
    soup.header.decompose()

    for tag in soup.find_all(class_ = "adboxtop adsizes"):
        tag.decompose()

    for tag in soup.find_all(class_ = "ie-adtext"):
        tag.parent.decompose()
    
    for tag in soup.find_all(class_ = "embed-youtube"):
        tag.decompose()
    

    soup.find(class_ = 'rightpanel').decompose()
    soup.find(class_ = "container-header").decompose()
    soup.find(class_ = "more-from").decompose()
    soup.find(class_ = "budget-band").decompose()
    soup.find(id="id_newsletter_subscription").decompose()   

    try:
        soup.find(class_ = 'premium_widget_below_article').decompose()
    except:
        pass

    try:
        soup.find(class_ = "subscriber_hide").decompose()
    except:
        pass

    return soup.prettify()

def clean_up (link, headers):
    if link.find(".economist.") != -1:
        return TheEconomist (link, headers)
    elif link.find(".thehindu.") != -1:
        return TheHindu (link, headers)
    elif link.find("indianexpress") != -1:
        return IndianExpress (link, headers)



"""soup.section.div.span.span.get_text() #Asia
soup.article.div.div.section.div.span.span.get_text() #| No business like sow business
soup.article.div.div.section.div.get_text() #Asia | No business like sow business
 article.div.div has 3 further divs- title, image, and div.div
1st div has section. Section has smaller title, h1, h2.
2nd is image with caption.
3rd is div.div. 
div.div.div for date and place.
div.div.section for body.
div.div.section.div has divs for paras.

delete style data

keep wrapping for images?

render soup.article or soup.article.div. Multiply font sizes by a factor.
 """

