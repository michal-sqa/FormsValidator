import _environment
import manage_requests
import manage_xml
import requests

forms_to_be_checked = {("Publish When Ready", "Chemical Standalone"):["Custom publish date", "Web Channel", "Test1"],
                       ("Publish With Report", "Chemical Report Section"):["Domain(Taxonomy)", "Brand(Taxonomy)", "Published Date", "Test2"]
                       }

def get_form_for_given_workflow_and_content_type(env, workflow, content_type):

    request_specification = f"/rest/service/admin/forms?workflow={workflow}&contenttype={content_type}"
    request = manage_requests.prepare_get_request(env, request_specification)
    get_response = requests.get(request)

    forms_list_values = manage_xml.extract_xml_elements_by_path(get_response.content, './/name')
    forms_list_text_values = list(map(lambda x: x.text, forms_list_values))
    return forms_list_text_values

#print(get_form_for_given_workflow_and_content_type(_environment.uat, 'Publish When Ready', 'Chemical Standalone'))

def get_missing_form_attributes(env):

    missing_form_attributes = {}

    for form in forms_to_be_checked:
        form_values_on_platform = forms_to_be_checked[form]
        forms_expected = get_form_for_given_workflow_and_content_type(env, form[0], form[1])
        if len(get_attributes_absent_from_form(form_values_on_platform, forms_expected))!=0:
            missing_form_attributes[(form[0], form[1])] = get_attributes_absent_from_form(form_values_on_platform, forms_expected)

    return missing_form_attributes


def get_attributes_absent_from_form(attributes, form_attributes):
    absent_attributes = [attribute for attribute in attributes if attribute not in form_attributes]

    return absent_attributes


#print(get_missing_form_attributes(_environment.uat))
