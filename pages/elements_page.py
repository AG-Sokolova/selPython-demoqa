import time
from random import randint
from selenium.webdriver.common.by import By
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxLocators, RadioButtonLocators, WebTablesLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())

        full_name = f'{person_info.first_name} {person_info.first_name} {person_info.middle_name}'
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)

        for i in range(21):
            item = item_list[randint(1, len(item_list)-1)]
            self.go_to_element(item)
            item.click()

    def get_checked_checkbox(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []

        for box in checked_list:
            title_item: str = (box.find_element(By.XPATH, self.locators.TITLE_ITEM)).text
            title_item = title_item.replace('.doc', '').replace(' ', '').lower()
            data.append(title_item)
        return data

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []

        for item in result_list:
            item = str(item.text).lower()
            data.append(item)
        return data


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RB,
                  'impressive': self.locators.IMPRESSIVE_RB,
                  'no': self.locators.NO_RB}

        self.element_is_visible(choices[choice]).click()
        return choice

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text.lower()

class WebTablesPage(BasePage):
    locators = WebTablesLocators()

    def add_new_person(self, count=1):
        data = []
        for i in range(count):
            person_info = next(generated_person())

            firstname = person_info.first_name
            lastname = person_info.last_name
            email = person_info.email
            age = str(person_info.age)
            salary = str(person_info.salary)
            dapartment = person_info.department
            data.append([firstname, lastname, age, email, salary, dapartment])

            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(dapartment)
            self.element_is_visible(self.locators.SUBMIT).click()
            time.sleep(3)
        return data

    def check_person(self):
        data = []
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)

        for item in person_list:
            if len(item.text.replace(' ', '')) != 0:
                data.append(item.text.splitlines())
        return data

    def search_some_person(self, word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(word)
