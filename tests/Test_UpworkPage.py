from verify import expect
from Core.CUpworkPage import CUpworkPage
from tests import common

def fromFile(filename):
  def f(url):
    expect(url).is_equal('url')
    return common.fromFile(filename)
  return f

class Test_UpworkPage:
  def test_returnFirstPage(self):
    page = CUpworkPage('url', http=fromFile('jobs.json'))
    expect(len(page.jobs())).is_equal(50)
    return
  
  def test_correctShortText(self):
    # TODO: Fix test
    page = CUpworkPage('url', http=fromFile('jobs.json'))
    expect(page.jobs()[0].asShortText()).is_equal(
      '0$ | Integrate Jupyter Notebook with Hubspot | https://www.upwork.com/freelance-jobs/apply/~019a41055df0ec2d2e/'
    )
    return