from p6_POM_DBB_Page_Object_Model_Behaviour_Driven_Development.Curs12_POM_BDD.browser import Browser
from p6_POM_DBB_Page_Object_Model_Behaviour_Driven_Development.Curs12_POM_BDD.pages.login_page import LoginPage


# before_all este o metoda care este recunoscuta de libraria behave.ini si care se va executa inainte de toate testele
def before_all(context):  # context ne ajuta sa accesam toate paginilie care vor putea fi folosite in alte fisiere
    context.browser = Browser()
    context.login_page = LoginPage()


# after_all este o metoda care este recunoscuta de libraria behave.ini si care se va executa dupa toate testele
def after_all(context):
    context.browser.close()