from pullgerFootPrint.com.linkedin import general as linkedinGeneral


def get_list_of_experience(squirrel):
    resultData = []

    if squirrel.current_url.find('/be.') != -1:  # Check unauthorized data get
        unauthorized_page = True
    else:
        unauthorized_page = False

    if unauthorized_page is True:
        # # squirrel.find_XPATH('//main[@id="main"]').finds_XPATH('./section')
        experience_section = squirrel.find_xpath(xpath='//div[@class="pvs-list__outer-container"]/ul')
        if experience_section is None:
            experience_section = squirrel.find_xpath(xpath='//div[@class="scaffold-finite-scroll__content"]/ul')
    else:
        # Expanded experience
        experience_section = squirrel.find_xpath(xpath='//div[@class="scaffold-finite-scroll__content"]/ul')
        if experience_section is None:
            # Main people page
            Sections = squirrel.find_xpath(xpath='//main[@id="main"]/section')
            experience_section = None

            for curSection in Sections:
                experienceSectionFound = curSection.find_xpath(xpath='./div[@id="experience"]')
                if experienceSectionFound is not None:
                    experience_section = curSection.find_xpath(xpath='.//ul')
                    break
    # experienceSection = squirrel.find_xpath(xpath='//ul[@class="experience__list"]')
    # squirrel.find_xpath(xpath='//ul[@class="experience__list"]').find_xpath("./li")

    if experience_section is not None:
        if unauthorized_page is True:
            # experienceSectionList = squirrel.find_xpath(xpath='//li[@class="experience-group experience-item"]')
            experienceSectionList = squirrel.finds_xpath(xpath='//li[@class="profile-section-card  experience-item"]')
        else:
            # experienceSectionList = [experienceSection]
            experienceSectionList = experience_section.finds_xpath(xpath='./li')
            # experienceSectionList = squirrel.find_xpath(xpath='//section[@class="artdeco-card ember-view relative break-words pb3 mt2 "]')

        for experience_section in experienceSectionList:
            if unauthorized_page is True:
                # expSection = experienceSection.find_XPATH(xpath='.//a[@class="experience-group-header__url"]')
                expSection = experience_section.find_xpath(xpath='.//a[@class="profile-section-card__image-link"]')
                # expSection = experienceSection.find_xpath(xpath='.//a')
            else:
                # expSection = experienceSection.find_xpath(xpath='.//div[@id="experience"]')
                expSection = experience_section.find_xpath(xpath='.//a')

            if expSection is not None:
                if unauthorized_page is True:
                    experienceList = experience_section.finds_xpath(
                        './/li[@class="profile-section-card  experience-group-position"]')
                    if len(experienceList) == 0:
                        # experienceList = experienceSection.find_xpath('./div')
                        experienceList = experience_section.finds_xpath(
                            xpath='.//div[@class="profile-section-card__contents"]'
                        )
                else:
                    calcInner = experience_section.finds_xpath(
                        xpath='.//div[@class="display-flex flex-row justify-space-between"]'
                    )
                    if len(calcInner) > 1:
                        experienceList = experience_section.finds_xpath(
                            xpath='.//li'
                        )
                        # Exception on experience list
                        if len(experienceList) > len(calcInner):
                            experienceList = experience_section.finds_xpath(
                                xpath='.//li[@class="pvs-list__paged-list-item  "]'
                            )
                        # ============================
                    else:
                        experienceList = [experience_section]

                    # experienceList = expSection.find_xpath(xpath='.//li[@class="artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column"]')

                for curExperience in experienceList:

                    experienceData = {
                        "companyIDENTIFICATOR": None,
                        "companyID": None,
                        "companyNICK": None,
                        "job_description": None,
                        "companyName": None,
                        "job_timing_type": None,
                        "companyURL": None
                    }

                    if unauthorized_page is True:
                        if unauthorized_page is True:
                            JobDiscriptionEl = curExperience.find_xpath(
                                xpath='.//h3[@class="profile-section-card__title"]'
                            )
                        else:
                            JobDiscriptionEl = curExperience.find_xpath(
                                xpath='.//div[@class="display-flex align-items-center"]//span[@aria-hidden="true"]'
                            )
                    else:
                        JobDiscriptionEl = curExperience.find_xpath(
                            xpath='.//div[@class="display-flex align-items-center"]//span[@aria-hidden="true"]'
                        )

                    if JobDiscriptionEl is not None:
                        experienceData["job_description"] = JobDiscriptionEl.text

                    if unauthorized_page is True:
                        JobUrlEl = expSection
                    else:
                        JobUrlEl = experience_section.find_xpath(
                            xpath='.//a[@data-field="experience_company_logo"]'
                        )
                        if JobUrlEl is None:
                            # Full list of experience
                            JobUrlEl = experience_section.find_xpath(
                                xpath='.//a'
                            )

                    if JobUrlEl is not None:
                        href = JobUrlEl.get_attribute('href')
                        href = linkedinGeneral.get_cleaned_url(href)

                        if href is not None:
                            experienceData["companyURL"] = href

                            splitedUrl = list(filter(None, href.split("/")))
                            experienceData["companyIDENTIFICATOR"] = splitedUrl[-1]
                            try:
                                experienceData["companyID"] = int(experienceData["companyIDENTIFICATOR"])
                            except:
                                experienceData["companyNICK"] = experienceData["companyIDENTIFICATOR"]

                    if unauthorized_page is True:
                        JobNameEl = experience_section.find_xpath('.//h4')
                    else:
                        JobNameEl = experience_section.find_xpath(
                            './/span[@class="mr1 hoverable-link-text t-bold"]/span[@aria-hidden="true"]')
                        if JobNameEl is None:
                            JobNameEl = curExperience.find_xpath(
                                './/span[@class="t-14 t-normal"]/span[@aria-hidden="true"]')

                    if JobNameEl is not None:
                        JobNameSplited = JobNameEl.text.split("·")
                        experienceData["companyName"] = JobNameSplited[0]

                        if len(JobNameSplited) > 1:
                            experienceData["job_timing_type"] = JobNameSplited[1];

                    # Not appeng uncreated organization
                    if experienceData["companyIDENTIFICATOR"] is None:
                        continue

                    resultData.append(experienceData)

    return resultData
