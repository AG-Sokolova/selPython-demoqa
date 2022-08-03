from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage
import random
import time

class TestElements:

    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            input_full_name, input_email, input_current_address, input_permanent_address = text_box_page.fill_all_fields()
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert input_full_name == output_full_name, "the full name does not match"
            assert input_email == output_email, "the email does not match"
            assert input_current_address == output_current_address, "the current address does not match"
            assert input_permanent_address == output_permanent_address, "the permanent address does not match"

            # input_data = text_box_page.fill_all_fields()
            # output_data = text_box_page.check_filled_form()
            # assert input_data == output_data

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkbox()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()

            radio_buttons = ['yes', 'impressive', 'no']

            for i in radio_buttons:
                input = radio_button_page.click_on_the_radio_button(i)
                output = radio_button_page.get_output_result()
                assert output == input, f'"{i}" have not been selected'

    class TestWebTables:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()

            input = web_table_page.add_person(5)
            output = web_table_page.check_person()

            for items in input:
                assert items in output, f'{items} have not been selected'

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()

            # создаем нового пользователя
            new_person = web_table_page.add_person()[0]
            # поиск пользователя
            key_word = new_person[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            # получаем данные из таблицы
            table_result = web_table_page.check_person()
            # сравниваем, полностью строку, отображается ли новая строка при поиске
            assert new_person in table_result, f'the person {new_person} was not found in the table'
            # сравниваем, все ли строки содержат слово, которое указано в поиске
            for person in table_result:
                assert key_word in person, f'{key_word} have not been selected'

        def test_web_table_edit_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()

            # рандомный пользователь из таблицы
            # random_person = random.choice(web_table_page.check_person())
            # web_table_page.search_some_person(random_person[1])

            # создаем нового пользователя и ищем его по email через поиск
            # new_person = web_table_page.add_person()[0]
            # key_word = new_person[4]  # => получить email созданного пользователя

            web_table_page.search_some_person('Cierra')
            edit_person = web_table_page.edit_person()
            table_result = web_table_page.check_person()
            assert edit_person in table_result, f'the person card has not been change'

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()

            # создать нового пользователя
            new_person = web_table_page.add_person()[0]
            # поиск пользователя по email
            key_word = new_person[4]  # => получить email созданного пользователя
            web_table_page.search_some_person(new_person[4])
            # удалить пользователя
            web_table_page.delete_person()
            # проверить что пользователь удален, при поиске появится надпись 'No rows found' если пользователь удален
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_person()
            assert table_result == 'No rows found', f'Not delete {new_person}'


