import cove.lib.threesixtygiving as threesixtygiving

GRANTS = {
    'grants': [{'Co-applicant(s)': 'Mr Bentley Crudgington, Mr Gary Thomas ',
                'Full name of applicant': 'Miss Abigail Addison',
                'Grant number': '105177/Z/14/Z',
                'Grant type': 'Large Arts Awards bob@bop.com',
                'Sponsor(s)': ' ',
                'Surname of applicant': 'Addison',
                'amountAwarded': 152505,
                'awardDate': '24/07/2014',
                'currency': 'GBP',
                'dataSource': 'http://www.wellcome.ac.uk/Managing-a-grant/Grants-awarded/index.htm',
                'dateModified': '13-03-2015',
                'fundingOrganization': [{'id': 'XSFAFA',
                                         'name': 'The Wellcome Trust'}],
                'id': '360G-wellcometrust-105177/Z/14/Z',
                'plannedDates': [{'duration': '30'}],
                'recipientOrganization': [{'addressLocality': 'London ',
                                           'charityNumber': '12345',
                                           'companyNumber': 'AAA',
                                           'id': '360G-Blah',
                                           'name': 'Animate Project Limited'}],
                'title': 'Silent Signal.  ,moo@moo.com '},
               {'Co-applicant(s)': ' ',
                'Department': 'Department of Museum Studies',
                'Full name of applicant': 'Prof Richard Sandell',
                'Grant number': '105182/Z/14/Z',
                'Grant type': 'Large Arts Awards',
                'Sponsor(s)': ' ',
                'Surname of applicant': 'Sandell',
                'amountAwarded': 0,
                'awardDate': '24/07/2014',
                'currency': 'GBP',
                'dataSource': 'http://www.wellcome.ac.uk/Managing-a-grant/Grants-awarded/index.htm',
                'dateModified': '13-03-2015',
                'description': 'Exceptional and Extraordinary: unruly bodies and '
                               'minds in the medical museum. ',
                'fundingOrganization': [{'id': '360G-CHC-210183',
                                         'name': 'The Wellcome Trust'}],
                'grantProgramme': [{'code': 'AAC',
                                    'title': 'Arts Awards Funding Committee'}],
                'id': '360G-wellcometrust-105182/Z/14/Z',
                'plannedDates': [{'duration': '25'}],
                'recipientOrganization': [{'addressLocality': 'Leicester ',
                                           'charityNumber': '1234567',
                                           'companyNumber': 'RC000659',
                                           'id': 'GB-UNKNOW-RC000659',
                                           'name': 'UNIVERSITY OF LEICESTER'}],
                'title': 'Exceptional and Extraordinary: unruly bodies and minds '
                         'in the medical museum. '},
               {'Co-applicant(s)': ' ',
                'Department': 'Department of Museum Studies',
                'Full name of applicant': 'Prof Richard Sandell',
                'Grant number': '105183/Z/14/Z',
                'Grant type': 'Large Arts Awards',
                'Sponsor(s)': ' ',
                'Surname of applicant': 'Sandell',
                'amountAwarded': 0,
                'awardDate': '24/07/2014',
                'currency': 'GBP',
                'dataSource': 'http://www.wellcome.ac.uk/Managing-a-grant/Grants-awarded/index.htm',
                'dateModified': '13-03-2015',
                'description': 'Exceptional and Extraordinary: unruly bodies and '
                               'minds in the medical museum. ',
                'fundingOrganization': [{'id': 'GB-COH-A1065900',
                                         'name': 'The Wellcome Trust'}],
                'grantProgramme': [{'code': 'AAC',
                                    'title': 'Arts Awards Funding Committee'}],
                'id': '360G-wellcometrust-105183/Z/14/Z',
                'plannedDates': [{'duration': '25'}],
                'recipientOrganization': [{'addressLocality': 'Leicester ',
                                           'charityNumber': '1234567',
                                           'companyNumber': 'RC000659',
                                           'id': 'GB-CHC-10659',
                                           'name': 'UNIVERSITY OF LEICESTER'}],
                'title': 'Exceptional and Extraordinary: unruly bodies and minds '
                         'in the medical museum. '}]}

SOURCE_MAP = {
    'grants/0': [['grants', 2]],
    'grants/0/Co-applicant(s)': [['grants', 'E', 2, 'Co-applicant(s)']],
    'grants/0/Full name of applicant': [['grants',
                                         'D',
                                         2,
                                         'Full name of applicant']],
    'grants/0/Grant number': [['grants', 'B', 2, 'Grant number']],
    'grants/0/Grant type': [['grants', 'G', 2, 'Grant type']],
    'grants/0/Sponsor(s)': [['grants', 'F', 2, 'Sponsor(s)']],
    'grants/0/Surname of applicant': [['grants', 'C', 2, 'Surname of applicant']],
    'grants/0/amountAwarded': [['grants', 'Q', 2, 'Amount Awarded']],
    'grants/0/awardDate': [['grants', 'S', 2, 'Award Date']],
    'grants/0/currency': [['grants', 'R', 2, 'Currency']],
    'grants/0/dataSource': [['grants', 'Y', 2, 'Data source']],
    'grants/0/dateModified': [['grants', 'X', 2, 'Last modified']],
    'grants/0/fundingOrganization/0': [['grants', 2]],
    'grants/0/fundingOrganization/0/id': [['grants',
                                           'V',
                                           2,
                                           'Funding Org:Identifier']],
    'grants/0/fundingOrganization/0/name': [['grants',
                                             'W',
                                             2,
                                             'Funding Org:Name']],
    'grants/0/id': [['grants', 'A', 2, 'Identifier']],
    'grants/0/plannedDates/0': [['grants', 2]],
    'grants/0/plannedDates/0/duration': [['grants',
                                          'P',
                                          2,
                                          'Planned Dates:Duration (months)']],
    'grants/0/recipientOrganization/0': [['grants', 2]],
    'grants/0/recipientOrganization/0/addressLocality': [['grants',
                                                          'N',
                                                          2,
                                                          'Recipient Org:City']],
    'grants/0/recipientOrganization/0/charityNumber': [['grants',
                                                        'M',
                                                        2,
                                                        'Recipient Org:Charity '
                                                        'Number']],
    'grants/0/recipientOrganization/0/companyNumber': [['grants',
                                                        'L',
                                                        2,
                                                        'Recipient Org:Company '
                                                        'Number']],
    'grants/0/recipientOrganization/0/id': [['grants',
                                             'J',
                                             2,
                                             'Recipient Org:Identifier']],
    'grants/0/recipientOrganization/0/name': [['grants',
                                               'K',
                                               2,
                                               'Recipient Org:Name']],
    'grants/0/title': [['grants', 'O', 2, 'Title']],
    'grants/1': [['grants', 3]],
    'grants/1/Co-applicant(s)': [['grants', 'E', 3, 'Co-applicant(s)']],
    'grants/1/Department': [['grants', 'H', 3, 'Department']],
    'grants/1/Full name of applicant': [['grants',
                                         'D',
                                         3,
                                         'Full name of applicant']],
    'grants/1/Grant number': [['grants', 'B', 3, 'Grant number']],
    'grants/1/Grant type': [['grants', 'G', 3, 'Grant type']],
    'grants/1/Sponsor(s)': [['grants', 'F', 3, 'Sponsor(s)']],
    'grants/1/Surname of applicant': [['grants', 'C', 3, 'Surname of applicant']],
    'grants/1/amountAwarded': [['grants', 'Q', 3, 'Amount Awarded']],
    'grants/1/awardDate': [['grants', 'S', 3, 'Award Date']],
    'grants/1/currency': [['grants', 'R', 3, 'Currency']],
    'grants/1/dataSource': [['grants', 'Y', 3, 'Data source']],
    'grants/1/dateModified': [['grants', 'X', 3, 'Last modified']],
    'grants/1/description': [['grants', 'Z', 3, 'Description']],
    'grants/1/fundingOrganization/0': [['grants', 3]],
    'grants/1/fundingOrganization/0/id': [['grants',
                                           'V',
                                           3,
                                           'Funding Org:Identifier']],
    'grants/1/fundingOrganization/0/name': [['grants',
                                             'W',
                                             3,
                                             'Funding Org:Name']],
    'grants/1/grantProgramme/0': [['grants', 3]],
    'grants/1/grantProgramme/0/code': [['grants', 'T', 3, 'Grant Programme:Code']],
    'grants/1/grantProgramme/0/title': [['grants',
                                         'U',
                                         3,
                                         'Grant Programme:Title']],
    'grants/1/id': [['grants', 'A', 3, 'Identifier']],
    'grants/1/plannedDates/0': [['grants', 3]],
    'grants/1/plannedDates/0/duration': [['grants',
                                          'P',
                                          3,
                                          'Planned Dates:Duration (months)']],
    'grants/1/recipientOrganization/0': [['grants', 3]],
    'grants/1/recipientOrganization/0/addressLocality': [['grants',
                                                          'N',
                                                          3,
                                                          'Recipient Org:City']],
    'grants/1/recipientOrganization/0/charityNumber': [['grants',
                                                        'M',
                                                        3,
                                                        'Recipient Org:Charity '
                                                        'Number']],
    'grants/1/recipientOrganization/0/companyNumber': [['grants',
                                                        'L',
                                                        3,
                                                        'Recipient Org:Company '
                                                        'Number']],
    'grants/1/recipientOrganization/0/id': [['grants',
                                             'J',
                                             3,
                                             'Recipient Org:Identifier']],
    'grants/1/recipientOrganization/0/name': [['grants',
                                               'K',
                                               3,
                                               'Recipient Org:Name']],
    'grants/1/title': [['grants', 'O', 3, 'Title']],
    'grants/2': [['grants', 4]],
    'grants/2/Co-applicant(s)': [['grants', 'E', 4, 'Co-applicant(s)']],
    'grants/2/Department': [['grants', 'H', 4, 'Department']],
    'grants/2/Full name of applicant': [['grants',
                                         'D',
                                         4,
                                         'Full name of applicant']],
    'grants/2/Grant number': [['grants', 'B', 4, 'Grant number']],
    'grants/2/Grant type': [['grants', 'G', 4, 'Grant type']],
    'grants/2/Sponsor(s)': [['grants', 'F', 4, 'Sponsor(s)']],
    'grants/2/Surname of applicant': [['grants', 'C', 4, 'Surname of applicant']],
    'grants/2/amountAwarded': [['grants', 'Q', 4, 'Amount Awarded']],
    'grants/2/awardDate': [['grants', 'S', 4, 'Award Date']],
    'grants/2/currency': [['grants', 'R', 4, 'Currency']],
    'grants/2/dataSource': [['grants', 'Y', 4, 'Data source']],
    'grants/2/dateModified': [['grants', 'X', 4, 'Last modified']],
    'grants/2/description': [['grants', 'Z', 4, 'Description']],
    'grants/2/fundingOrganization/0': [['grants', 4]],
    'grants/2/fundingOrganization/0/id': [['grants',
                                           'V',
                                           4,
                                           'Funding Org:Identifier']],
    'grants/2/fundingOrganization/0/name': [['grants',
                                             'W',
                                             4,
                                             'Funding Org:Name']],
    'grants/2/grantProgramme/0': [['grants', 4]],
    'grants/2/grantProgramme/0/code': [['grants', 'T', 4, 'Grant Programme:Code']],
    'grants/2/grantProgramme/0/title': [['grants',
                                         'U',
                                         4,
                                         'Grant Programme:Title']],
    'grants/2/id': [['grants', 'A', 4, 'Identifier']],
    'grants/2/plannedDates/0': [['grants', 4]],
    'grants/2/plannedDates/0/duration': [['grants',
                                          'P',
                                          4,
                                          'Planned Dates:Duration (months)']],
    'grants/2/recipientOrganization/0': [['grants', 4]],
    'grants/2/recipientOrganization/0/addressLocality': [['grants',
                                                          'N',
                                                          4,
                                                          'Recipient Org:City']],
    'grants/2/recipientOrganization/0/charityNumber': [['grants',
                                                        'M',
                                                        4,
                                                        'Recipient Org:Charity '
                                                        'Number']],
    'grants/2/recipientOrganization/0/companyNumber': [['grants',
                                                        'L',
                                                        4,
                                                        'Recipient Org:Company '
                                                        'Number']],
    'grants/2/recipientOrganization/0/id': [['grants',
                                             'J',
                                             4,
                                             'Recipient Org:Identifier']],
    'grants/2/recipientOrganization/0/name': [['grants',
                                               'K',
                                               4,
                                               'Recipient Org:Name']],
    'grants/2/title': [['grants', 'O', 4, 'Title']]
}


RESULTS = [
    ('One or more of your grants have a value of £0. It’s worth taking a look at '
     'these grants and deciding if they should be published. It’s unusual to have '
     'grants of £0, but there may be a reasonable explanation. Additional '
     'information on why these grants are £0 might be useful to anyone using the '
     'data, so consider adding an explanation to the description of the grant.',
     ['grants/0/amountAwarded'],
     [['grants', 'Q', 2, 'Amount Awarded']]),
    ('One or more of your grants have a Recipient Org:Identifier that is has a '
     "prefix of '360G'. If the grant is from a recipient organisation that has an "
     'external identifier (such as a charity number, company number, or in the '
     'case of local authorities, geocodes), then this should be used instead. If '
     'no other identifier can be used, then this notice can be ignored.',
     ['grants/0/recipientOrganization/0/id'],
     [['grants', 'J', 2, 'Recipient Org:Identifier']]),
    ('One or more of your grants have a Funding Org:Identifier that is has a '
     "prefix of '360G'. If the grant is from a recipient organisation that has an "
     'external identifier (such as a charity number, company number, or in the '
     'case of local authorities, geocodes), then this should be used instead. If '
     'no other identifier can be used, then this notice can be ignored.',
     ['grants/1/fundingOrganization/0/id'],
     [['grants', 'V', 3, 'Funding Org:Identifier']]),
    ('33% of your grants have a Recipient Org:Identifier that doesn’t draw from '
     'an external identification body, e.g. a charity number or a company number. '
     'Using external identifiers helps people using your data to match it up '
     'against other data - for example to see who else has given grants to the '
     'same recipient, even if they’re known by a different name. If the data '
     'describes lots of grants to organisations that don’t have such identifiers '
     'or individuals then you can ignore this notice.',
     ['grants/1/recipientOrganization/0/id'],
     [['grants', 'J', 3, 'Recipient Org:Identifier']]),
    ('33% of your grants have a Funding Org:Identifier that doesn’t draw from an '
     'external identification body, e.g. a charity number or a company number. '
     'Using external identifiers helps people using your data to match it up '
     'against other data - for example to see who else has given grants to the '
     'same recipient, even if they’re known by a different name. If the data '
     'describes lots of grants to organisations that don’t have such identifiers '
     'or individuals then you can ignore this notice.',
     ['grants/0/fundingOrganization/0/id'],
     [['grants', 'V', 2, 'Funding Org:Identifier']]),
    ('1 grant(s) have a value provided in the Recipient Org: Charity Number '
     'column, but the value doesn’t look like a charity number. Common causes of '
     'this are missing leading digits, typos or incorrect values being entered '
     'into this field.',
     ['grants/0/recipientOrganization/0/charityNumber'],
     [['grants', 'M', 2, 'Recipient Org:Charity Number']]),
    ('1 grant(s) have a value provided in the Recipient Org: Company Number '
     'column, but the value doesn’t look like a company number. Common causes of '
     'this are missing leading digits, typos or incorrect values being entered '
     'into this field.',
     ['grants/0/recipientOrganization/0/companyNumber'],
     [['grants', 'L', 2, 'Recipient Org:Company Number']]),
    ('There are a total of 3 funding organisation IDs listed. If you are '
     'expecting to be publishing data for multiple funders then this notice can '
     'be ignored, however if you are only publishing for a single funder then you '
     'should review your Funder ID column to see where multiple IDs have '
     'occurred.',
     [],
     []),
    ('Some grants contain text that looks like an email address. This may '
     'indicate that the data contains personal data, use and distribution of '
     'which is restricted by the Data Protection Act. You should ensure that any '
     'personal data is included with the knowledge and consent of the person to '
     'whom it refers.',
     ['grants/0/Grant type', 'grants/0/title'],
     [['grants', 'G', 2, 'Grant type'], ['grants', 'O', 2, 'Title']]),
    ('1 of the grant(s) do not contain any Grant Programme fields. Although not '
     'required by the 360Giving Standard, providing Grant Programme data if '
     'available helps users to better understand your data.',
     ['grants/0/id'],
     [['grants', 'A', 2, 'Identifier']]),
    ('3 of the grants do not contain any beneficiary location fields. Although '
     'not required by the 360Giving Standard, providing beneficiary data if '
     'available helps users to understand your data and allows it to be used in '
     'tools that visualise grants geographically. ',
     ['grants/0/id', 'grants/1/id', 'grants/2/id'],
     [['grants', 'A', 2, 'Identifier'],
      ['grants', 'A', 3, 'Identifier'],
      ['grants', 'A', 4, 'Identifier']]),
    ('2 grants have a title and description that are the same. Users may find '
     'that the data is less useful as they are unable to discover more about the '
     'grants. Consider including a more detailed description if you have one.',
     ['grants/1/description', 'grants/2/description'],
     [['grants', 'Z', 3, 'Description'], ['grants', 'Z', 4, 'Description']]),
    ('Some grant(s) have funder or recipient organisation IDs that might not be '
     'valid for the registration agency that they refer to - for example, a '
     'GB-CHC ID that contains an invalid charity number. Common causes of this '
     'are missing leading digits, typos or incorrect values being entered into '
     'this field.',
     ['grants/2/fundingOrganization/0/id', 'grants/2/recipientOrganization/0/id'],
     [['grants', 'V', 4, 'Funding Org:Identifier'],
      ['grants', 'J', 4, 'Recipient Org:Identifier']])
]


def test_additional_checks():
    assert threesixtygiving.run_additional_checks(GRANTS, SOURCE_MAP) == RESULTS
