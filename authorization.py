# from selenium.webdriver.common.by import By

def getUserInputElement(squirrel):
    elementFind = squirrel.find_XPATH("//input[@id='session_key']");

    return elementFind;

def setUserName(squirrel, inUserName):
    result = None;

    userInput = getUserInputElement(squirrel);
    if userInput != None:
        result = userInput.send_string(inUserName);

    return result;

def getPasswordInputElement(squirrel):
    elementFind = squirrel.find_XPATH("//input[@id='session_password']");

    return elementFind;

def setPassword(squirrel, inPassword):
    result = None;

    passwordInput = getPasswordInputElement(squirrel);
    if passwordInput != None:
        result = passwordInput.send_string(inPassword);

    return result;

def getSingInButton(squirrel):
    elementFind = squirrel.find_XPATH("//button[@class='sign-in-form__submit-button']");

    return elementFind;


def singIn(squirrel):
    result = None;

    singInButton = getSingInButton(squirrel);
    if singInButton != None:
        import time
        time.sleep(1)
        result = singInButton.click();

    return result;



# def setUserName():

# def getCountOfReviewsElements(squirrel):
#     return len(squirrel.driver.find_elements(By.XPATH, "//li[@class='review_list_new_item_block']"));
#
# def getListOfReviews(squirrel):
#     import dateparser
#     listOfReviews = [];
#
#     dataList = squirrel.driver.find_elements(By.XPATH, "//li[@class='review_list_new_item_block']");
#
#     for el in dataList:
#         reviewData = {};
#
#         try:
#             reviewData["name"] = el.find_element(By.XPATH, ".//span[@class='bui-avatar-block__title']").text
#         except:
#             reviewData["name"] = None;
#
#         try:
#             reviewData["uuid_reviews"] = el.get_attribute("data-review-url")
#         except:
#             reviewData["uuid_reviews"] = None;
#
#         try:
#             midleWEl = el.find_element(By.XPATH, ".//div[@class='bui-grid__column-9 c-review-block__right']");
#             post_date = midleWEl.find_element(By.XPATH, ".//span[@class='c-review-block__date']").text;
#             splitclearDate = post_date.split(":")
#             clearDate = splitclearDate[1]
#
#             reviewData["post_date"] = dateparser.parse(clearDate);
#         except:
#             reviewData["post_date"] = None;
#
#         try:
#             reviewData["rate"] = el.find_element(By.XPATH, ".//div[@class='bui-review-score__badge']").text;
#         except:
#             reviewData["rate"] = None;
#
#         reviewData["review_good"] = None;
#         reviewData["review_good_lang"] = None;
#         reviewData["review_bad"] = None;
#         reviewData["review_bad_lang"] = None;
#
#         try:
#             reviewBlock = el.find_element(By.XPATH, ".//div[@class='c-review']");
#             reviewRows = reviewBlock.find_elements(By.XPATH, "*");
#
#             for elReviewRow in reviewRows:
#                 try:
#                     svgBlock = elReviewRow.find_element_by_css_selector('svg');
#
#                     try:
#                         ThisIsBadBlockReview = False;
#                         ThisIsGoodBlockReview = False;
#                         classSVG = svgBlock.get_attribute("class")
#
#                         if classSVG == 'bk-icon -iconset-review_poor c-review__icon':
#                             ThisIsBadBlockReview = True;
#                         elif classSVG == 'bk-icon -iconset-review_great c-review__icon':
#                             ThisIsGoodBlockReview = True;
#
#                         if ThisIsBadBlockReview == True or ThisIsGoodBlockReview == True:
#                             try:
#                                 reviewBlock = elReviewRow.find_element(By.XPATH, ".//span[@class='c-review__body']");
#                                 reviewText = reviewBlock.text;
#                                 reviewLang = reviewBlock.get_attribute("lang")
#                             except:
#                                 try:
#                                     reviewText = ""
#                                     reviewLang = ""
#
#                                     listElAnalitic = elReviewRow.find_elements(By.XPATH, ".//p/*")
#                                     for elAnalitic in listElAnalitic:
#                                         if elAnalitic.get_attribute("class").strip() == "c-review__body c-review__body--original":
#                                             reviewText = elAnalitic.text
#                                             reviewLang = elAnalitic.get_attribute("lang")
#                                             break;
#
#                                     #elReviewRow.find_element_by_css_selector('span.c-review__body c-review__body--original\n');
#                                     #reviewBlock = elReviewRow.find_element(By.XPATH, ".//span[@class='c-review__body c-review__body--original\n']");
#                                     #reviewText = reviewBlock.text;
#                                 except:
#                                     reviewText = "";
#
#                             if ThisIsBadBlockReview == True:
#                                 reviewData["review_bad"] = reviewText;
#                                 reviewData["review_bad_lang"] = reviewLang;
#                             elif ThisIsGoodBlockReview == True:
#                                 reviewData["review_good"] = reviewText;
#                                 reviewData["review_good_lang"] = reviewLang;
#
#
#                     except:
#                         err = ""
#
#                 except:
#                     err = ""
#
#         except:
#             test = 33;
#
#         listOfReviews.append(reviewData)
#
#     return listOfReviews;
#
# def getCurrentPaginationNumber(squirrel):
#     dataPagination = squirrel.driver.find_elements(By.XPATH, "//div[@class='bui-pagination__list']");
#
#     if len(dataPagination) == 1:
#         pagElements = dataPagination[0].find_elements(By.XPATH, "./child::*");
#
#         for elPagination in pagElements:
#             if elPagination.get_attribute("class") == "bui-pagination__item bui-pagination__item--active":
#                 numElement = elPagination.find_elements(By.XPATH, ".//span[@aria-hidden]");
#                 if len(numElement) == 1:
#                     return int(numElement[0].text)
#
#     return None;
#
#
# def goToNextPaginationPage(squirrel):
#     dataPagination = squirrel.driver.find_elements(By.XPATH, "//div[@class='bui-pagination__list']");
#
#     if len(dataPagination) == 1:
#         pagElements = dataPagination[0].find_elements(By.XPATH, "./child::*");
#
#         thisIsCurrentElement = False;
#         for elPagination in pagElements:
#             if thisIsCurrentElement == True:
#                 nexpPag = elPagination.find_elements(By.XPATH, "./a")
#                 if len(nexpPag) == 1:
#                     nextPage = nexpPag[0].get_attribute("href");
#                     #driver.execute_script('window.location.href = "' + nextPage + '"');
#                     #driver.get(nextPage);
#                     squirrel.get(nextPage)
#
#                     return True;
#                 else:
#                     return False;
#
#             if elPagination.get_attribute("class") == "bui-pagination__item bui-pagination__item--active":
#                 thisIsCurrentElement = True;
#
#     return None;