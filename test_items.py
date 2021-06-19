import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestCatalog():
    def test_basket_button(self, browser):
        print("\nstart test...")
        browser.get(link)
        assert browser.find_element_by_css_selector('button.btn-add-to-basket')
        print("\nend test...")
