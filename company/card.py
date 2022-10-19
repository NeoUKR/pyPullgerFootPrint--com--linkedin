def goToAbout(**kwargs):
    squirrel = None
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        sectionNavigation = squirrel.find_XPATH('//ul[@class="org-page-navigation__items "]')
        if sectionNavigation != None:
            result = 'ok'
            # sectionNavigation = squirrel.finds_XPATH('.//a')
            # for curSection

    return result

def getOverview(inSquirrel = None, **kwargs):
    squirrel = inSquirrel
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        overviewCard = squirrel.find_xpath('//section[@class="artdeco-card p5 mb4"]')
        if overviewCard != None:
            overviewSection = overviewCard.find_xpath('.//p')
            if overviewSection != None:
                result = overviewSection.text
    return result

def getID(**kwargs):
    squirrel = None
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        res1 = squirrel.find_XPATH('//*[@data-entity-hovercard-id]')
        if res1 != None:
            entityList = res1.get_attribute('data-entity-hovercard-id').split(":")
            if len(entityList) == 4:
                try:
                    result = int(entityList[3])
                except:
                    pass

    return result

def getNick(**kwargs):
    squirrel = None
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        navigateBlock = squirrel.find_XPATH('//ul[@class="org-page-navigation__items "]')
        if navigateBlock != None:
            navButton = navigateBlock.find_xpath('.//a')
            if navButton != None:
                href = navButton.get_attribute('href')
                if href != None:
                    hrefSplited = list(filter(None, href.split("/")))
                    if len(hrefSplited) >= 2:
                        result = hrefSplited[3]

    return result

def getLocations(inSquirrel=None, **kwargs):
    squirrel = inSquirrel
    result = []

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        locationsList = squirrel.finds_xpath('//p[@class="t-14 t-black--light t-normal break-words"]')
        for curLocation in locationsList:
            result.append(curLocation.text)

    return result



def getAboutData(**kwargs):
    squirrel = None
    result = None

    if 'squirrel' in kwargs:
        squirrel = kwargs['squirrel']

    if squirrel != None:
        structureAbout = {
            'ID': None,
            'CARD_TYPE': None,
            'NAME': None,
            'DISCRIPTION': None,
            'LOCATION_NAME': None,
            'FOLLOWERS': None,
            'OVERVIEW': None,
            'WEBSITE': None,
            'INDUSTRY': None,
            'COMPANY_SIZE': None,
            'EMPLOYEE_LINKEDIN': None,
            'HEADQUARTERS': None,
            'FOUNDED': None,
            'SPECIALITIES': None,
            'LOCATIONS': None
        }

        # ================================================================================
        # card_type
        # ================================================================================
        if squirrel.current_url.find('/school/') != -1:
            structureAbout['CARD_TYPE'] = 'school';
        elif squirrel.current_url.find('/company/') != -1:
            structureAbout['CARD_TYPE'] = 'company';
        # ================================================================================
        # ================================================================================
        allEmployees = squirrel.find_XPATH('//div[@class="relative"]//div[@class="mt1"]//a')
        if allEmployees == None:
            allEmployees = squirrel.find_XPATH('//div[@class="relative pl5 pt3 pr4 pb4"]//div[@class="org-top-card-listing__summary"]//a')

        if allEmployees != None:
            hrefEmployees = allEmployees.get_attribute('href')
            startMarker = hrefEmployees.find('currentCompany=')
            if startMarker != -1:
                startMarkerID =  hrefEmployees.find('%22', startMarker)
                if startMarkerID != -1:
                    endMarker = hrefEmployees.find('%22', startMarkerID + 3)
                    if endMarker != -1:
                        structureAbout['ID'] = hrefEmployees[(startMarkerID+3):endMarker]
        # ================================================================================
        # ================================================================================
        headSegment = squirrel.find_XPATH('//div[@class="block mt2"]')
        if headSegment != None:
            NameTag = headSegment.find_xpath('.//h1')
            if NameTag != None:
                structureAbout['NAME'] = NameTag.text

            DiscriptionTag = headSegment.find_xpath('.//p')
            if DiscriptionTag != None:
                structureAbout['DISCRIPTION'] = DiscriptionTag.text

            MainInfoSegment = headSegment.find_xpath('.//div[@class="org-top-card-summary-info-list t-14 t-black--light"]/div[@class="inline-block"]')
            if MainInfoSegment != None:
                MainSegments = MainInfoSegment.finds_xpath('./div')
                i = 1
                for curMainInformation in MainSegments:
                    if i == 1:
                        structureAbout['LOCATION_NAME'] = curMainInformation.text
                    elif i == 2:
                        followersText = curMainInformation.text
                        if type(followersText) == str:
                            followersSplited = followersText.split(' ')
                            try:
                                structureAbout['FOLLOWERS'] = int(followersSplited[0].replace(',',''))
                            except:
                                pass
                    else:
                        break
                    i += 1

        structureAbout['OVERVIEW'] = getOverview(squirrel = squirrel)

        overviewCard = squirrel.find_XPATH('//dl[@class="overflow-hidden"]')
        if overviewCard != None:

            aboutSections = overviewCard.finds_xpath('./*')
            curentSection = None;

            for aboutElement in aboutSections:
                if aboutElement.tag_name == 'dt':
                    curentSection = aboutElement.text.upper();
                elif aboutElement.tag_name == 'dd':
                    if curentSection == 'WEBSITE':
                        linckElement = aboutElement.find_xpath('.//a')
                        if linckElement != None:
                            structureAbout[curentSection] = linckElement.get_attribute('href')
                    elif curentSection == 'INDUSTRY':
                        structureAbout[curentSection] = aboutElement.text.upper()
                    elif curentSection == 'COMPANY SIZE':
                        if aboutElement.find_xpath('.//span'):
                            structureAbout['EMPLOYEE_LINKEDIN'] = aboutElement.text[:aboutElement.text.find('\n')]
                        else:
                            structureAbout['COMPANY_SIZE'] = aboutElement.text
                    elif curentSection == 'HEADQUARTERS':
                        structureAbout[curentSection] = aboutElement.text
                    elif curentSection == 'FOUNDED':
                        structureAbout[curentSection] = aboutElement.text
                    elif curentSection == 'SPECIALITIES':
                        listOfSpecialties = aboutElement.text.split(',')
                        structureAbout[curentSection] = [name.upper() for name in listOfSpecialties]

        structureAbout['LOCATIONS'] = getLocations(squirrel = squirrel)

        result = structureAbout

    return result