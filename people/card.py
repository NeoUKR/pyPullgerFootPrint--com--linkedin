from pullgerFootPrint.com.linkedin import general as linkedinGeneral


def getListOfExperience(squirrel):
    resultData = [];

    if squirrel.current_url.find('/be.') != -1: #Check unautorized data get
        unautorizedPage = True
    else:
        unautorizedPage = False

    if unautorizedPage == True:
        # # squirrel.find_XPATH('//main[@id="main"]').finds_XPATH('./section')
        experienceSection = squirrel.find_XPATH('//div[@class="pvs-list__outer-container"]/ul')
        if experienceSection == None:
            experienceSection = squirrel.find_XPATH('//div[@class="scaffold-finite-scroll__content"]/ul')
    else:
        # Expanded experiance
        experienceSection = squirrel.find_XPATH('//div[@class="scaffold-finite-scroll__content"]/ul')
        if experienceSection == None:
            # Main people page
            Sections = squirrel.finds_XPATH('//main[@id="main"]/section')
            experienceSection = None

            for curSection in Sections:
                experienceSectionFound = curSection.find_XPATH('./div[@id="experience"]')
                if experienceSectionFound != None:
                    experienceSection = curSection.find_XPATH('.//ul')
                    break
    # experienceSection = squirrel.find_XPATH('//ul[@class="experience__list"]')
    # squirrel.find_XPATH('//ul[@class="experience__list"]').finds_XPATH("./li")

    if experienceSection != None:
        if unautorizedPage == True:
            # experienceSectionList = squirrel.finds_XPATH('//li[@class="experience-group experience-item"]')
            experienceSectionList = squirrel.finds_XPATH('//li[@class="profile-section-card  experience-item"]')
        else:
            # experienceSectionList = [experienceSection]
            experienceSectionList = experienceSection.finds_XPATH('./li')
            # experienceSectionList = squirrel.finds_XPATH('//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "]')

        for experienceSection in experienceSectionList:
            if unautorizedPage == True:
                # expSection = experienceSection.find_XPATH('.//a[@class="experience-group-header__url"]')
                expSection = experienceSection.find_XPATH('.//a[@class="profile-section-card__image-link"]')
                # expSection = experienceSection.find_XPATH('.//a')
            else:
                # expSection = experienceSection.find_XPATH('.//div[@id="experience"]')
                expSection = experienceSection.find_XPATH('.//a')

            if expSection != None:
                if unautorizedPage == True:
                    experienceList = experienceSection.finds_XPATH('.//li[@class="profile-section-card  experience-group-position"]')
                    if len(experienceList) == 0:
                        # experienceList = experienceSection.finds_XPATH('./div')
                        experienceList = experienceSection.finds_XPATH('.//div[@class="profile-section-card__contents"]')
                else:
                    calcInner = experienceSection.finds_XPATH('.//div[@class="display-flex flex-row justify-space-between"]')
                    if len(calcInner) > 1:
                        experienceList = experienceSection.finds_XPATH('.//li')
                        # Exception on experience list
                        if len(experienceList) > len(calcInner):
                            experienceList = experienceSection.finds_XPATH('.//li[@class="pvs-list__paged-list-item  "]')
                        # ============================
                    else:
                        experienceList = [experienceSection]

                    # experienceList = expSection.finds_XPATH('.//li[@class="artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"]')

                for curExperience in experienceList:

                    experienceData = {};
                    experienceData["companyIDENTIFICATOR"] = None
                    experienceData["companyID"] = None
                    experienceData["companyNICK"] = None
                    experienceData["job_discription"] = None
                    experienceData["companyName"] = None
                    experienceData["job_timing_type"] = None
                    experienceData["companyURL"] = None

                    if unautorizedPage == True:
                        if unautorizedPage == True:
                            JobDiscriptionEl = curExperience.find_XPATH('.//h3[@class="profile-section-card__title"]')
                        else:
                            JobDiscriptionEl = curExperience.find_XPATH('.//div[@class="display-flex align-items-center"]//span[@aria-hidden="true"]')
                    else:
                        JobDiscriptionEl = curExperience.find_XPATH('.//div[@class="display-flex align-items-center"]//span[@aria-hidden="true"]')

                    if JobDiscriptionEl != None:
                        experienceData["job_discription"] = JobDiscriptionEl.text;

                    if unautorizedPage == True:
                        JobUrlEl = expSection
                    else:
                        JobUrlEl = experienceSection.find_XPATH('.//a[@data-field="experience_company_logo"]', True)
                        if JobUrlEl == None:
                            #Full list of experiance
                            JobUrlEl = experienceSection.find_XPATH('.//a')

                    if JobUrlEl != None:
                        href = JobUrlEl.get_attribute('href')
                        href = linkedinGeneral.getCleanedURL(href)

                        if href != None:
                            experienceData["companyURL"] = href

                            splitedUrl = list(filter(None,href.split("/")))
                            experienceData["companyIDENTIFICATOR"] = splitedUrl[-1]
                            try:
                                experienceData["companyID"] = int(experienceData["companyIDENTIFICATOR"])
                            except:
                                experienceData["companyNICK"] = experienceData["companyIDENTIFICATOR"]

                    if unautorizedPage == True:
                        JobNameEl = experienceSection.find_XPATH('.//h4')
                    else:
                        JobNameEl = experienceSection.find_XPATH('.//span[@class="mr1 hoverable-link-text t-bold"]/span[@aria-hidden="true"]', True)
                        if JobNameEl == None:
                            JobNameEl = curExperience.find_XPATH('.//span[@class="t-14 t-normal"]/span[@aria-hidden="true"]')


                    if JobNameEl != None:
                        JobNameSplited = JobNameEl.text.split("·")
                        experienceData["companyName"] = JobNameSplited[0]

                        if len(JobNameSplited) > 1:
                            experienceData["job_timing_type"] = JobNameSplited[1];

                    #Not appeng uncreated organization
                    if experienceData["companyIDENTIFICATOR"] == None:
                        continue

                    resultData.append(experienceData)

    return resultData
