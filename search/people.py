from pullgerFootPrint.com.linkedin import general as linkedinGeneral


def getCountOfResults(squirrel):

    resCount = None;

    resElements = squirrel.find_xpath("//h2[@class='pb2 t-black--light t-14']")

    if resElements != None:
        resInner = resElements.text
        splitInner = resInner.split(" ")
        if len(splitInner) == 3:
            resCount = int(splitInner[1].replace(",",""))
        elif len(splitInner) == 2:
            resCount = int(splitInner[0].replace(",", ""))
    else:
        resCount = None

    return resCount;


def get_list_of_peoples(squirrel):

    result_data = []

    personsList = squirrel.finds_xpath("//div[@class='entity-result']")

    for el in personsList:
        review_data = {
            "id": None,
            "nick": None,
            "first_name": None,
            "second_name": None,
            "full_name": None,
            "description": None,
            "url": None
        }

        idAttr = el.get_attribute('data-chameleon-result-urn')
        idAttrArray = idAttr.split(':')
        if len(idAttrArray) == 4:
            try:
                review_data["id"] = int(idAttrArray[3])
            except:
                continue

        NameEl = el.find_xpath(".//a[@class='app-aware-link ']")

        if NameEl is not None:
            url = NameEl.get_attribute('href')
            url = linkedinGeneral.get_cleaned_url(url)
            review_data["url"] = url

            review_data["nick"] = linkedinGeneral.getNickFromURL(url)

            resNameElement = NameEl.find_xpath(".//span[@aria-hidden='true']")
            if resNameElement is not None:
                review_data["full_name"] = resNameElement.text

        # Get first and second names
        if review_data["full_name"] is not None:
            splitedFullName = review_data["full_name"].split(" ")
            if len(splitedFullName) > 1:
                review_data["first_name"] = splitedFullName[0];
                review_data["second_name"] = ''.join(map(str, splitedFullName[1:]))

        description_el = el.find_xpath(
            ".//div[@class='entity-result__primary-subtitle t-14 t-black t-normal']"
        )
        if description_el is not None:
            review_data["description"] = description_el.text

        result_data.append(review_data)

    return result_data

def getNumberCurentPaginationPage(squirrel):
    result = None;

    paginationSection = squirrel.find_xpath('//ul[@class="artdeco-pagination__pages artdeco-pagination__pages--number"]')
    if paginationSection != None:
        curPagPageEl = paginationSection.find_xpath('./li[@class="artdeco-pagination__indicator artdeco-pagination__indicator--number active selected ember-view"]')
        if curPagPageEl != None:
            try:
                result = int(curPagPageEl.get_attribute('data-test-pagination-page-btn'))
            except Exception as e:
                result = None;

    return result

def getNumberLastPaginationPage(squirrel):
    result = None;

    paginationSection = squirrel.find_xpath('//ul[@class="artdeco-pagination__pages artdeco-pagination__pages--number"]')
    if paginationSection != None:
        allPaginationButton = paginationSection.finds_xpath('./li[@class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view"]')

        for curPagDome in allPaginationButton:
            try:
                result = int(curPagDome.get_attribute('data-test-pagination-page-btn'))
            except Exception as e:
                pass

    return result

def getNextPaginationButton(squirrel):
    result = squirrel.find_xpath('//button[@aria-label="Next"]')
    return result

def pushNextPaginationButton(squirrel):
    result = None

    NextButton = getNextPaginationButton(squirrel);
    if NextButton != None:
        NextButton.click()
        result = True

    return result;