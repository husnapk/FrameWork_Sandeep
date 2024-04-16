from selenium.webdriver.chrome.webdriver import WebDriver

driver=WebDriver()

driver.get("https://demowebshop.tricentis.com/")

titles=driver.find_elements('xpath','//div[@class="product-item"]//h2/a')
prices=driver.find_elements('xpath','//div[@class="prices"]/span')
d={}
for i in range(len(titles)):
    d[titles[i].text]=prices[i].text
print(d)
# driver.get("https://www.amazon.com/s?k=Jeans&rh=n%3A1040660%2Cn%3A1048188%2Cp_36%3A-5000&dc&ds=v1%3AZrh2YeJ%2Bmo6tc5p1QJD9idnCpBDTF2pKNTUbGqlhFKk&_encoding=UTF8&content-id=amzn1.sym.b0c3902d-ae70-4b80-8f54-4d0a3246745a&crid=1TZCO6ZC2HZVA&pd_rd_r=9b2b4db4-048e-4be8-9292-b53a67ba6f38&pd_rd_w=PCqk7&pd_rd_wg=mTZG2&pf_rd_p=b0c3902d-ae70-4b80-8f54-4d0a3246745a&pf_rd_r=GFPNNPQ90VRGCVE52AZB&qid=1684823801&rnid=2941120011&sprefix=jeans%2Caps%2C155&ref=pd_gw_unk")
# allnames = driver.find_elements("xpath","//div[@class='a-section a-spacing-base']//h2/a")
# allprices=driver.find_elements("xpath","//div[@class='a-section a-spacing-base']//div//span")
