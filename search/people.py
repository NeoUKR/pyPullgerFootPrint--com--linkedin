from pullgerFootPrint.com.linkedin import general as linkedinGeneral


def getCountOfResults(squirrel):

    resCount = None;

    resElements = squirrel.find_XPATH("//h2[@class='pb2 t-black--light t-14']")

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

def getListOfPeoples(squirrel):

    resultData = [];

    personsList = squirrel.finds_XPATH("//div[@class='entity-result']")

    for el in personsList:
        reviewData = {};
        reviewData["id"] = None
        reviewData["nick"] = None
        reviewData["first_name"] = None
        reviewData["second_name"] = None
        reviewData["full_name"] = None
        reviewData["discription"] = None
        reviewData["url"] = None

        idAttr = el.get_attribute('data-chameleon-result-urn')
        idAttrArray = idAttr.split(':')
        if len(idAttrArray) == 4:
            try:
                reviewData["id"] = int(idAttrArray[3]);
            except:
                continue;

        NameEl = el.find_XPATH(".//a[@class='app-aware-link']")

        if NameEl != None:
            url = NameEl.get_attribute('href')
            url = linkedinGeneral.getCleanedURL(url)
            reviewData["url"] = url

            reviewData["nick"] = linkedinGeneral.getNickFromURL(url)

            resNameElement = NameEl.find_XPATH(".//span[@aria-hidden='true']")
            if resNameElement != None:
                reviewData["full_name"] = resNameElement.text

        # Get first and second names
        if reviewData["full_name"] != None:
            splitedFullName = reviewData["full_name"].split(" ")
            if len(splitedFullName) > 1:
                reviewData["first_name"] = splitedFullName[0];
                reviewData["second_name"] = ''.join(map(str, splitedFullName[1:]))


        discriptionEl = el.find_XPATH(".//div[@class='entity-result__primary-subtitle t-14 t-black t-normal']")
        if discriptionEl != None:
            reviewData["discription"] = discriptionEl.text

        resultData.append(reviewData);


    return resultData;

def getNumberCurentPaginationPage(squirrel):
    result = None;

    paginationSection = squirrel.find_XPATH('//ul[@class="artdeco-pagination__pages artdeco-pagination__pages--number"]')
    if paginationSection != None:
        curPagPageEl = paginationSection.find_XPATH('./li[@class="artdeco-pagination__indicator artdeco-pagination__indicator--number active selected ember-view"]')
        if curPagPageEl != None:
            try:
                result = int(curPagPageEl.get_attribute('data-test-pagination-page-btn'))
            except Exception as e:
                result = None;

    return result

def getNumberLastPaginationPage(squirrel):
    result = None;

    paginationSection = squirrel.find_XPATH('//ul[@class="artdeco-pagination__pages artdeco-pagination__pages--number"]')
    if paginationSection != None:
        allPaginationButton = paginationSection.finds_XPATH('./li[@class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view"]')

        for curPagDome in allPaginationButton:
            try:
                result = int(curPagDome.get_attribute('data-test-pagination-page-btn'))
            except Exception as e:
                pass

    return result

def getNextPaginationButton(squirrel):
    result = squirrel.find_XPATH('//button[@aria-label="Next"]')
    return result

def pushNextPaginationButton(squirrel):
    result = None

    NextButton = getNextPaginationButton(squirrel);
    if NextButton != None:
        NextButton.click()
        result = True

    return result;