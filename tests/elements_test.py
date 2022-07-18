from pages.elements_page import TextBoxPage
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