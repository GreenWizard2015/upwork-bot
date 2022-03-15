from verify import expect
from bot.CParsedMessage import CParsedMessage

class Test_ParsedMessage:
  def test_NoLinks(self):
    msg = CParsedMessage(' xxxxxxxxxxxxx ')
    expect(msg.links).is_equal([]) 
    return
  
  def test_OneLink(self):
    msg = CParsedMessage(' xxxxxxxxxxxxx https://www.upwork.com/nx/jobs/search/?q=python&sort=recency&t=1&client_hires=1-9,10- xxx')
    expect(msg.links).is_equal(['https://www.upwork.com/nx/jobs/search/?q=python&sort=recency&t=1&client_hires=1-9,10-']) 
    return
  
  def test_MultipleLink(self):
    links = ['https://www.upwork.com/%d' % x for x in range(5)]
    msg = CParsedMessage(' | '.join(links))
    expect(sorted(msg.links)).is_equal(links) 
    return
  
  def test_OnlyUnique(self):
    links = ['https://www.upwork.com/%d' % x for x in range(5)]
    msg = CParsedMessage(' | '.join(links * 5))
    expect(sorted(msg.links)).is_equal(links) 
    return