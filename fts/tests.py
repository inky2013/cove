import pytest
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os


PREFIX_OCDS = os.environ.get('PREFIX_OCDS', '')
PREFIX_360 = os.environ.get('PREFIX_360', '')
if not PREFIX_360 and not PREFIX_OCDS:
    PREFIX_OCDS = '/ocds/'
    PREFIX_360 = '/360/'

PREFIX_LIST = [prefix for prefix in (PREFIX_OCDS, PREFIX_360) if prefix]

BROWSER = os.environ.get('BROWSER', 'Firefox')


@pytest.fixture(scope="module")
def browser(request):
    browser = getattr(webdriver, BROWSER)()
    browser.implicitly_wait(3)
    request.addfinalizer(lambda: browser.quit())
    return browser


@pytest.fixture(scope="module")
def server_url(request, live_server):
    if 'CUSTOM_SERVER_URL' in os.environ:
        return os.environ['CUSTOM_SERVER_URL']
    else:
        return live_server.url
    

def test_index_page_banner(server_url, browser):
    if not PREFIX_360 or not PREFIX_OCDS:
        pytest.skip()
    browser.get(server_url)
    assert 'This tool is alpha. Please report any problems on GitHub issues.' in browser.find_element_by_tag_name('body').text
    if server_url == "http://dev.cove.opendataservices.coop/":
        assert 'This is a development site with experimental features. Do not rely on it.' in browser.find_element_by_tag_name('body').text
    

def test_index_page(server_url, browser):
    if not PREFIX_360 or not PREFIX_OCDS:
        pytest.skip()
    browser.get(server_url)
    assert 'CoVE' in browser.find_element_by_tag_name('body').text
    assert '360Giving Data Quality Tool' in browser.find_element_by_tag_name('body').text
    assert 'Open Contracting Data Tool' in browser.find_element_by_tag_name('body').text
    assert 'Creating and using Open Data is made easier when there are good tools to help.' in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize(('link_text', 'expected_text', 'css_selector', 'url'), [
    ('Open Contracting', 'We connect governments', 'h1', 'http://www.open-contracting.org/'),
    ('Open Contracting Data Standard', 'Open Contracting Data Standard: Documentation', '#open-contracting-data-standard-documentation', 'http://standard.open-contracting.org/'),
    ])
def test_footer_ocds(server_url, browser, link_text, expected_text, css_selector, url):
    if not PREFIX_OCDS:
        pytest.skip()
    browser.get(server_url + PREFIX_OCDS)
    footer = browser.find_element_by_id('footer')
    link = footer.find_element_by_link_text(link_text)
    href = link.get_attribute("href")
    assert url in href
    link.click()
    time.sleep(0.5)
    assert expected_text in browser.find_element_by_css_selector(css_selector).text


@pytest.mark.parametrize(('link_text', 'expected_text', 'css_selector', 'url'), [
    ('360Giving', '360Giving is a company limited by guarantee', 'body.home', 'http://www.threesixtygiving.org/'),
    ('360Giving Data Standard', 'Standard', 'h1.entry-title', 'http://www.threesixtygiving.org/standard/'),
    ])
def test_footer_360(server_url, browser, link_text, expected_text, css_selector, url):
    if not PREFIX_360:
        pytest.skip()
    browser.get(server_url + PREFIX_360)
    link = browser.find_element_by_link_text(link_text)
    href = link.get_attribute("href")
    assert url in href
    link.click()
    time.sleep(0.5)
    assert expected_text in browser.find_element_by_css_selector(css_selector).text


def test_index_page_ocds(server_url, browser):
    if not PREFIX_OCDS:
        pytest.skip()
    browser.get(server_url + PREFIX_OCDS)
    assert 'Data Standard Validator' in browser.find_element_by_tag_name('body').text
    assert 'Using the validator' in browser.find_element_by_tag_name('body').text
    assert "'release'" in browser.find_element_by_tag_name('body').text
    assert "'record'" in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize(('css_id', 'link_text', 'url'), [
    ('introduction', 'schema', 'http://standard.open-contracting.org/latest/en/schema/'),
    ('introduction', 'Open Contracting Data Standard (OCDS)', 'http://standard.open-contracting.org/'),
    ('how-to-use', "'release' and 'record'", 'http://standard.open-contracting.org/latest/en/getting_started/releases_and_records/'),
    ('how-to-use', 'flattened serialization of OCDS', 'http://standard.open-contracting.org/latest/en/implementation/serialization/'),
    ('how-to-use', 'Open Contracting Data Standard', 'http://standard.open-contracting.org/')
    ])
def test_index_page_ocds_links(server_url, browser, css_id, link_text, url):
    if not PREFIX_OCDS:
        pytest.skip()
    browser.get(server_url + PREFIX_OCDS)
    section = browser.find_element_by_id(css_id)
    link = section.find_element_by_link_text(link_text)
    href = link.get_attribute("href")
    assert url in href
    
    
def test_index_page_360(server_url, browser):
    if not PREFIX_360:
        pytest.skip()
    browser.get(server_url + PREFIX_360)
    assert 'Data Quality Tool' in browser.find_element_by_class_name('title360').text
    assert 'How to use the 360Giving Data Quality Tool' in browser.find_element_by_tag_name('body').text
    assert 'Summary Spreadsheet - Excel' in browser.find_element_by_tag_name('body').text
    assert 'JSON built to the 360Giving JSON schema' in browser.find_element_by_tag_name('body').text
    assert 'Multi-table data package - Excel' in browser.find_element_by_tag_name('body').text
    assert '360 Giving' not in browser.find_element_by_tag_name('body').text
  
  
@pytest.mark.parametrize(('link_text', 'url'), [
    ('360Giving Data Standard guidance', 'http://www.threesixtygiving.org/standard/'),
    ('Excel', 'https://github.com/ThreeSixtyGiving/standard/raw/master/schema/summary-table/360-giving-schema-titles.xlsx'),
    ('CSV', 'https://github.com/ThreeSixtyGiving/standard/raw/master/schema/summary-table/360-giving-schema-titles.csv/grants.csv'),
    ('360Giving JSON schema', 'http://www.threesixtygiving.org/standard/reference/#toc-360giving-json-schemas'),
    ('Multi-table data package - Excel', 'https://github.com/ThreeSixtyGiving/standard/raw/master/schema/multi-table/360-giving-schema-fields.xlsx')
    ])
def test_index_page_360_links(server_url, browser, link_text, url):
    if not PREFIX_360:
        pytest.skip()
    browser.get(server_url + PREFIX_360)
    link = browser.find_element_by_link_text(link_text)
    href = link.get_attribute("href")
    assert url in href


@pytest.mark.parametrize('prefix', PREFIX_LIST)
def test_common_index_elements(server_url, browser, prefix):
    if not PREFIX_360 or not PREFIX_OCDS:
        pytest.skip()
    browser.get(server_url + prefix)
    browser.find_element_by_css_selector('#more-information .panel-title').click()
    time.sleep(0.5)
    assert 'What happens to the data I provide to this site?' in browser.find_element_by_tag_name('body').text
    assert 'Why do you delete data after 7 days?' in browser.find_element_by_tag_name('body').text
    assert 'Why provide converted versions?' in browser.find_element_by_tag_name('body').text
    assert 'Terms & Conditions' in browser.find_element_by_tag_name('body').text
    assert 'Open Data Services' in browser.find_element_by_tag_name('body').text
    assert 'Open Data Services Co-operative' not in browser.find_element_by_tag_name('body').text
    assert '360 Giving' not in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize('prefix', PREFIX_LIST)
def test_terms_page(server_url, browser, prefix):
    browser.get(server_url + prefix + 'terms/')
    assert 'Open Data Services Co-operative Limited' in browser.find_element_by_tag_name('body').text
    assert 'Open Data Services Limited' not in browser.find_element_by_tag_name('body').text
    assert '360 Giving' not in browser.find_element_by_tag_name('body').text
    

@pytest.mark.parametrize('prefix', PREFIX_LIST)
def test_accordion(server_url, browser, prefix):
    browser.get(server_url + prefix)

    def buttons():
        return [b.is_displayed() for b in browser.find_elements_by_tag_name('button')]

    time.sleep(0.5)
    assert buttons() == [True, False, False]
    assert 'Upload a file (.json, .csv, .xlsx)' in browser.find_elements_by_tag_name('label')[0].text
    browser.find_element_by_partial_link_text('Link').click()
    browser.implicitly_wait(1)
    time.sleep(0.5)
    assert buttons() == [False, True, False]
    browser.find_element_by_partial_link_text('Paste').click()
    time.sleep(0.5)
    assert buttons() == [False, False, True]
    assert 'Paste (JSON only)' in browser.find_elements_by_tag_name('label')[2].text

    # Now test that the whole banner is clickable
    browser.find_element_by_id('headingOne').click()
    time.sleep(0.5)
    assert buttons() == [True, False, False]
    browser.find_element_by_id('headingTwo').click()
    time.sleep(0.5)
    assert buttons() == [False, True, False]
    browser.find_element_by_id('headingThree').click()
    time.sleep(0.5)
    assert buttons() == [False, False, True]


@pytest.mark.parametrize(('source_filename', 'expected_text', 'conversion_successful'), [
    ('tenders_releases_2_releases.json', ['Convert'], True),
    ('ocds_release_nulls.json', ['Convert', 'Save or Share these results'], True),
    # Conversion should still work for files that don't validate against the schema
    ('tenders_releases_2_releases_invalid.json', ['Convert',
                                                  'Validation Errors',
                                                  "'id' is missing but required",
                                                  "Invalid 'uri' found"], True),
    # Test UTF-8 support
    ('utf8.json', 'Convert', True),
    # But we expect to see an error message if a file is not well formed JSON at all
    ('tenders_releases_2_releases_not_json.json', 'not well formed JSON', False),
    ('tenders_releases_2_releases.xlsx', 'Convert', True),
    ('badfile.json', 'Statistics can not produced', True),
    # Test unconvertable JSON (main sheet "releases" is missing)
    ('unconvertable_json.json', 'could not be converted', False),
    ('full_record.json', ['Number of records', 'Validation Errors', 'compiledRelease', 'versionedRelease'], True),
    ])
def test_URL_input(server_url, browser, httpserver, source_filename, expected_text, conversion_successful):
    if PREFIX_360 and not PREFIX_OCDS:
        pytest.skip()
    prefix = PREFIX_OCDS
    with open(os.path.join('cove', 'fixtures', source_filename), 'rb') as fp:
        httpserver.serve_content(fp.read())
    if 'CUSTOM_SERVER_URL' in os.environ:
        # Use urls pointing to GitHub if we have a custom (probably non local) server URL
        source_url = 'https://raw.githubusercontent.com/OpenDataServices/cove/master/cove/fixtures/' + source_filename
    else:
        source_url = httpserver.url + '/' + source_filename

    browser.get(server_url + prefix)
    browser.find_element_by_partial_link_text('Link').click()
    time.sleep(0.5)
    browser.find_element_by_id('id_source_url').send_keys(source_url)
    browser.find_element_by_css_selector("#fetchURL > div.form-group > button.btn.btn-primary").click()
    check_url_input_result_page(server_url, browser, httpserver, source_filename, expected_text, conversion_successful)
    #refresh page to now check if tests still work after caching some data
    browser.get(browser.current_url)

    selected_examples = ['tenders_releases_2_releases_invalid.json', 'WellcomeTrust-grants_fixed_2_grants.xlsx', 'WellcomeTrust-grants_2_grants_cp1252.csv']

    if source_filename in selected_examples:
        check_url_input_result_page(server_url, browser, httpserver, source_filename, expected_text, conversion_successful)
        browser.get(server_url + prefix + '?source_url=' + source_url)
        check_url_input_result_page(server_url, browser, httpserver, source_filename, expected_text, conversion_successful)


def check_url_input_result_page(server_url, browser, httpserver, source_filename, expected_text, conversion_successful):
    if source_filename.endswith('.json'):
        try:
            browser.find_element_by_name("flatten").click()
        except NoSuchElementException:
            pass
    body_text = browser.find_element_by_tag_name('body').text
    if isinstance(expected_text, str):
        expected_text = [expected_text]

    for text in expected_text:
        assert text in body_text

    assert 'Data Standard Validator' in browser.find_element_by_tag_name('body').text
    # assert 'Release Table' in browser.find_element_by_tag_name('body').text

    if conversion_successful:
        if source_filename.endswith('.json'):
            assert 'JSON (Original)' in body_text
            original_file = browser.find_element_by_link_text("JSON (Original)").get_attribute("href")
            if 'record' not in source_filename:
                converted_file = browser.find_element_by_link_text("Excel Spreadsheet (.xlsx) (Converted from Original)").get_attribute("href")
                assert "flattened.xlsx" in converted_file
        elif source_filename.endswith('.xlsx'):
            assert '(.xlsx) (Original)' in body_text
            original_file = browser.find_element_by_link_text("Excel Spreadsheet (.xlsx) (Original)").get_attribute("href")
            converted_file = browser.find_element_by_link_text("JSON (Converted from Original)").get_attribute("href")
            assert "unflattened.json" in converted_file
        elif source_filename.endswith('.csv'):
            assert '(.csv) (Original)' in body_text
            original_file = browser.find_element_by_link_text("CSV Spreadsheet (.csv) (Original)").get_attribute("href")
            converted_file = browser.find_element_by_link_text("JSON (Converted from Original)").get_attribute("href")
            assert "unflattened.json" in browser.find_element_by_link_text("JSON (Converted from Original)").get_attribute("href")

        assert source_filename in original_file
        assert '0 bytes' not in body_text
        # Test for Load New File button
        assert 'Load New File' in body_text

        original_file_response = requests.get(original_file)
        assert original_file_response.status_code == 200
        assert int(original_file_response.headers['content-length']) != 0

        if 'record' not in source_filename:
            converted_file_response = requests.get(converted_file)
            if source_filename == 'WellcomeTrust-grants_2_grants_titleswithoutrollup.xlsx':
                grant1 = converted_file_response.json()['grants'][1]
                assert grant1['recipientOrganization'][0]['department'] == 'Test data'
                assert grant1['classifications'][0]['title'] == 'Test'
            assert converted_file_response.status_code == 200
            assert int(converted_file_response.headers['content-length']) != 0


@pytest.mark.parametrize(('prefix', 'source_filename'), [
    (PREFIX_360, 'WellcomeTrust-grants_fixed_2_grants.json'),
    ])
def test_error_modal(server_url, browser, httpserver, source_filename, prefix):
    if not prefix:
        pytest.skip()
    with open(os.path.join('cove', 'fixtures', source_filename), 'rb') as fp:
        httpserver.serve_content(fp.read())
    if 'CUSTOM_SERVER_URL' in os.environ:
        # Use urls pointing to GitHub if we have a custom (probably non local) server URL
        source_url = 'https://raw.githubusercontent.com/OpenDataServices/cove/master/cove/fixtures/' + source_filename
    else:
        source_url = httpserver.url + '/' + source_filename

    browser.get(server_url + prefix)
    browser.find_element_by_partial_link_text('Link').click()
    time.sleep(0.5)
    browser.find_element_by_id('id_source_url').send_keys(source_url)
    browser.find_element_by_css_selector("#fetchURL > div.form-group > button.btn.btn-primary").click()

    # Click and un-collapse all explore sections
    all_sections = browser.find_elements_by_class_name('panel-heading')
    for section in all_sections:
        if section.get_attribute('data-toggle') == "collapse" and section.get_attribute('aria-expanded') != 'true':
            section.click()
        time.sleep(0.5)
    browser.find_element_by_css_selector('a[data-target=".validation-errors-1"]').click()

    modal = browser.find_element_by_css_selector('.validation-errors-1')
    assert "in" in modal.get_attribute("class").split()
    modal_text = modal.text
    assert "24/07/2014" in modal_text
    assert "grants/0/awardDate" in modal_text

    table_rows = browser.find_elements_by_css_selector('.validation-errors-1 tbody tr')
    assert len(table_rows) == 4


@pytest.mark.parametrize(('prefix', 'source_filename', 'expected_text'), [
    (PREFIX_360, 'WellcomeTrust-grants_fixed_2_grants.json', '360Giving JSON Package Schema')
    ])
def test_check_schema_link_on_result_page(server_url, browser, httpserver, source_filename, prefix, expected_text):
    if not prefix:
        pytest.skip()
    with open(os.path.join('cove', 'fixtures', source_filename), 'rb') as fp:
        httpserver.serve_content(fp.read())
    if 'CUSTOM_SERVER_URL' in os.environ:
        # Use urls pointing to GitHub if we have a custom (probably non local) server URL
        source_url = 'https://raw.githubusercontent.com/OpenDataServices/cove/master/cove/fixtures/' + source_filename
    else:
        source_url = httpserver.url + '/' + source_filename

    browser.get(server_url + prefix)
    browser.find_element_by_partial_link_text('Link').click()
    time.sleep(0.5)
    browser.find_element_by_id('id_source_url').send_keys(source_url)
    browser.find_element_by_css_selector("#fetchURL > div.form-group > button.btn.btn-primary").click()
    
    # We should still be in the correct app
    if prefix == PREFIX_360:
        # Click and un-collapse all explore sections
        all_sections = browser.find_elements_by_class_name('panel-heading')
        for section in all_sections:
            if section.get_attribute('data-toggle') == "collapse" and section.get_attribute('aria-expanded') != 'true':
                section.click()
            time.sleep(0.5)
        schema_link = browser.find_element_by_link_text(expected_text)
        schema_link.click()
        browser.find_element_by_id('toc-360giving-json-schemas')


@pytest.mark.parametrize('warning_texts', [[], ['Some warning']])
@pytest.mark.parametrize('flatten_or_unflatten', ['flatten', 'unflatten'])
def test_flattentool_warnings(server_url, browser, httpserver, monkeypatch, warning_texts, flatten_or_unflatten):
    """
    TODO: We need the same kind of test for 360 in test_360.py
    """
    # If we're testing a remove server then we can't run this test as we can't
    # set up the mocks
    if 'CUSTOM_SERVER_URL' in os.environ:
        pytest.skip()
    # Actual input file doesn't matter, as we override
    # flattentool behaviour with a mock below
    if flatten_or_unflatten == 'flatten':
        source_filename = 'tenders_releases_2_releases.json'
    else:
        source_filename = 'tenders_releases_2_releases.xlsx'

    import flattentool
    import warnings

    def mockunflatten(input_name, output_name, *args, **kwargs):
        with open(kwargs['cell_source_map'], 'w') as fp:
            fp.write('{}')
        with open(kwargs['heading_source_map'], 'w') as fp:
            fp.write('{}')
        with open(output_name, 'w') as fp:
            fp.write('{}')
            for warning_text in warning_texts:
                warnings.warn(warning_text)

    def mockflatten(input_name, output_name, *args, **kwargs):
        with open(output_name + '.xlsx', 'w') as fp:
            fp.write('{}')
            for warning_text in warning_texts:
                warnings.warn(warning_text)

    mocks = {
        'flatten': mockflatten,
        'unflatten': mockunflatten
    }
    monkeypatch.setattr(flattentool, flatten_or_unflatten, mocks[flatten_or_unflatten])

    with open(os.path.join('cove', 'fixtures', source_filename), 'rb') as fp:
        httpserver.serve_content(fp.read())
    if 'CUSTOM_SERVER_URL' in os.environ:
        # Use urls pointing to GitHub if we have a custom (probably non local) server URL
        source_url = 'https://raw.githubusercontent.com/OpenDataServices/cove/master/cove/fixtures/' + source_filename
    else:
        source_url = httpserver.url + '/' + source_filename

    browser.get(server_url + PREFIX_OCDS + '?source_url=' + source_url)

    if source_filename.endswith('.json'):
        try:
            browser.find_element_by_name("flatten").click()
        except NoSuchElementException:
            pass

    body_text = browser.find_element_by_tag_name('body').text
    if len(warning_texts) == 0:
        assert 'Conversion Warnings' not in body_text
        assert 'conversion errors' not in body_text
    else:
        assert warning_texts[0] in body_text
        assert 'Conversion Warnings' in body_text
        assert 'conversion errors' not in body_text


@pytest.mark.parametrize(('prefix'), PREFIX_LIST)
def test_URL_invalid_dataset_request(server_url, browser, prefix):
    # Test a badly formed hexadecimal UUID string
    browser.get(server_url + prefix + 'data/0')
    assert "We don't seem to be able to find the data you requested." in browser.find_element_by_tag_name('body').text
    # Test for well formed UUID that doesn't identify any dataset that exists
    browser.get(server_url + prefix + 'data/38e267ce-d395-46ba-acbf-2540cdd0c810')
    assert "We don't seem to be able to find the data you requested." in browser.find_element_by_tag_name('body').text
    assert '360 Giving' not in browser.find_element_by_tag_name('body').text
    #363 - Tests there is padding round the 'go to home' button
    success_button = browser.find_element_by_class_name('success-button')
    assert success_button.value_of_css_property('padding-bottom') == '20px'


@pytest.mark.parametrize('prefix', PREFIX_LIST)
def test_500_error(server_url, browser, prefix):
    browser.get(server_url + prefix + 'test/500')
    # Check that our nice error message is there
    assert 'Something went wrong' in browser.find_element_by_tag_name('body').text
    # Check for the exclamation icon
    # This helps to check that the theme including the css has been loaded
    # properly
    icon_span = browser.find_element_by_class_name('panel-danger').find_element_by_tag_name('span')
    assert 'Glyphicons Halflings' in icon_span.value_of_css_property('font-family')
    if prefix == PREFIX_OCDS:
        assert icon_span.value_of_css_property('color') == 'rgba(169, 68, 66, 1)'
    elif prefix == PREFIX_360:
        assert icon_span.value_of_css_property('color') == 'rgba(255, 255, 255, 1)'


def test_common_errors_page(server_url, browser):
    if not PREFIX_360:
        pytest.skip()
    browser.get(server_url + PREFIX_360 + 'common_errors/')
    assert "Common Errors" in browser.find_element_by_tag_name('h2').text
    assert '360 Giving' not in browser.find_element_by_tag_name('body').text


@pytest.mark.parametrize(('anchor_text'), [
    ('uri'),
    ('date-time'),
    ('required'),
    ('enum'),
    ('string'),
    ('integer')
    ])
def test_common_errors_page_anchors(server_url, browser, anchor_text):
    if not PREFIX_360:
        pytest.skip()
    # Checks we have sections for each our error messages
    browser.get(server_url + PREFIX_360 + 'common_errors/')
    browser.find_element_by_id(anchor_text)


def test_favicon(server_url, browser):
    browser.get(server_url)
    # we should not have a favicon link just now
    with pytest.raises(NoSuchElementException):
        browser.find_element_by_xpath("//link[@rel='icon']")
