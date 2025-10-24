from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import logging
import time


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def automated_signin_and_create_group():
    """
    Complete automation: Sign-in, expenses, settlement, create group, group expense, settle up
    """
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")
        
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(60)
        
        logger.info("Navigating to Splitify...")
        driver.get("http://localhost:3000")
        
        wait = WebDriverWait(driver, 20)
        extended_wait = WebDriverWait(driver, 30)
        
        # ========== SIGN IN FLOW ==========
        
        logger.info("Step 1: Clicking sign-in button...")
        sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "test-signin")))
        sign_in_button.click()
        logger.info("✓ Sign-in button clicked")
        time.sleep(3)
        
        logger.info("Step 2: Entering email...")
        email_field = wait.until(EC.visibility_of_element_located((By.NAME, "identifier")))
        email_field.clear()
        TEST_EMAIL = "clerk.test+automation@example.com"
        email_field.send_keys(TEST_EMAIL)
        logger.info(f"✓ Entered test email")
        time.sleep(2)
        
        logger.info("Step 3: Clicking continue button after email...")
        try:
            continue_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/main/div/div/div/div[1]/div[2]/form/div[2]/button")
            ))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", continue_button)
            time.sleep(1)
            
            try:
                continue_button.click()
                logger.info("✓ Continue button clicked")
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].click();", continue_button)
                logger.info("✓ Continue button clicked (JavaScript)")
        except:
            email_field.send_keys(Keys.RETURN)
            logger.info("✓ Pressed ENTER to continue")
        
        time.sleep(4)
        
        logger.info("Step 4: Entering password...")
        password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        TEST_PASSWORD = "test@splitify1"
        password_field.clear()
        password_field.send_keys(TEST_PASSWORD)
        logger.info(f"✓ Password entered")
        time.sleep(2)
        
        logger.info("Step 5: Clicking continue button after password...")
        try:
            password_continue_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/main/div/div/div/div[1]/div[2]/form/button[2]")
            ))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", password_continue_button)
            time.sleep(1)
            
            try:
                password_continue_button.click()
                logger.info("✓ Password continue button clicked")
            except:
                driver.execute_script("arguments[0].click();", password_continue_button)
                logger.info("✓ Password continue button clicked (JavaScript)")
        except:
            password_field.send_keys(Keys.RETURN)
            logger.info("✓ Pressed ENTER after password")
        
        time.sleep(7)
        
        logger.info("Step 6: Clicking dashboard button...")
        dashboard_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/nav/div[2]/a/button[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", dashboard_button)
        time.sleep(1)
        dashboard_button.click()
        logger.info("✓ Dashboard button clicked!")
        time.sleep(5)
        
        # ========== INDIVIDUAL EXPENSE CREATION ==========
        
        logger.info("Step 7: Clicking Add Expense button...")
        add_expense_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[1]/a"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_expense_button)
        time.sleep(1)
        add_expense_button.click()
        logger.info("✓ Add Expense button clicked")
        time.sleep(3)
        
        logger.info("Step 8: Clicking Individual option...")
        individual_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[1]/button[1]"))
        )
        individual_button.click()
        logger.info("✓ Individual option selected")
        time.sleep(2)
        
        logger.info("Step 9: Filling description field...")
        description_field = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div[1]/input"))
        )
        description_field.clear()
        description_field.send_keys("dinner")
        logger.info("✓ Description entered: dinner")
        time.sleep(1)
        
        logger.info("Step 10: Filling amount field...")
        amount_field = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div[2]/input"))
        )
        amount_field.clear()
        amount_field.send_keys("6000")
        logger.info("✓ Amount entered: 6000")
        time.sleep(1)
        
        logger.info("Step 11: Clicking Add Person button...")
        add_person_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div/div/button"))
        )
        add_person_button.click()
        logger.info("✓ Add Person button clicked")
        time.sleep(2)
        
        logger.info("Step 12: Searching for participant...")
        search_input = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/input"))
        )
        search_input.clear()
        search_input.send_keys("noushad ramim")
        logger.info("✓ Searching for: noushad ramim")
        time.sleep(2)
        
        logger.info("Step 13: Selecting participant from results...")
        participant_result = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div[2]"))
        )
        participant_result.click()
        logger.info("✓ Participant selected")
        time.sleep(2)
        
        logger.info("Step 14: Clicking Paid By dropdown...")
        paid_by_dropdown = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[2]/form/div[1]/div[4]/select"))
        )
        paid_by_dropdown.click()
        logger.info("✓ Paid By dropdown opened")
        time.sleep(1)
        
        logger.info("Step 15: Selecting 'You' option...")
        you_option = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[2]/form/div[1]/div[4]/select/option[2]"))
        )
        you_option.click()
        logger.info("✓ 'You' option selected")
        time.sleep(1)
        
        logger.info("Step 16: Clicking Create Expense button...")
        create_expense_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[2]/form/div[2]/button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", create_expense_button)
        time.sleep(1)
        create_expense_button.click()
        logger.info("✓ Individual expense created")
        time.sleep(5)
        
        # ========== SETTLEMENT SECTION ==========
        
        logger.info("Step 17: Clicking Settlement tab...")
        settlement_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[3]/div[1]/button[2]"))
        )
        settlement_button.click()
        logger.info("✓ Settlement tab clicked")
        time.sleep(3)
        
        # ========== GO BACK TO DASHBOARD AND CREATE GROUP ==========
        
        logger.info("Step 18: Clicking dashboard button again...")
        dashboard_button2 = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/header/nav/div/a/button[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", dashboard_button2)
        time.sleep(1)
        dashboard_button2.click()
        logger.info("✓ Dashboard button clicked")
        time.sleep(5)
        
        logger.info("Step 19: Clicking Create New Group button...")
        create_group_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[3]/div[2]/div[2]/div[3]/a"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", create_group_button)
        time.sleep(1)
        try:
            create_group_button.click()
            logger.info("✓ Create New Group button clicked")
        except:
            driver.execute_script("arguments[0].click();", create_group_button)
            logger.info("✓ Create New Group button clicked (JavaScript)")
        time.sleep(3)
        
        logger.info("Step 20: Filling group name...")
        group_name_input = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/form/div[1]/input"))
        )
        group_name_input.clear()
        group_name_input.send_keys("testing_group")
        logger.info("✓ Group name entered: testing_group")
        time.sleep(1)
        
        # ========== ADD MEMBERS ==========
        
        logger.info("Step 21: Clicking Add Member button (first member)...")
        add_member_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/form/div[3]/div/button"))
        )
        add_member_button.click()
        logger.info("✓ Add Member button clicked")
        time.sleep(3)
        
        logger.info("Step 22: Searching for first member (noushad ramim)...")
        member_search_input = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div[1]/input"))
        )
        member_search_input.click()
        member_search_input.clear()
        time.sleep(0.5)
        member_search_input.send_keys(Keys.CONTROL + "a")
        member_search_input.send_keys(Keys.DELETE)
        time.sleep(0.5)
        member_search_input.send_keys("noushad ramim")
        logger.info("✓ Searching for: noushad ramim")
        time.sleep(3)
        
        logger.info("Step 23: Selecting noushad ramim...")
        noushad_ramim = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div[2]/div"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", noushad_ramim)
        time.sleep(1)
        try:
            noushad_ramim.click()
            logger.info("✓ noushad ramim selected")
        except:
            driver.execute_script("arguments[0].click();", noushad_ramim)
            logger.info("✓ noushad ramim selected (JavaScript)")
        
        time.sleep(3)
        
        logger.info("Step 24: Clicking Add Member button again (second member)...")
        try:
            add_member_button2 = extended_wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/form/div[3]/div/button"))
            )
            add_member_button2.click()
            logger.info("✓ Add Member button clicked again")
        except StaleElementReferenceException:
            logger.info("Stale element, re-locating button...")
            time.sleep(2)
            add_member_button2 = extended_wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/form/div[3]/div/button"))
            )
            add_member_button2.click()
            logger.info("✓ Add Member button clicked again (retry)")
        
        time.sleep(3)
        
        logger.info("Step 25: Searching for second member (md noushad)...")
        member_search_input2 = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div[1]/input"))
        )
        
        member_search_input2.click()
        time.sleep(0.5)
        member_search_input2.clear()
        time.sleep(0.5)
        member_search_input2.send_keys(Keys.CONTROL + "a")
        member_search_input2.send_keys(Keys.DELETE)
        time.sleep(0.5)
        member_search_input2.send_keys("md noushad")
        logger.info("✓ Searching for: md noushad")
        time.sleep(3)
        
        logger.info("Step 26: Selecting md noushad...")
        parent_div = extended_wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div[2]/div/div"))
        )
        
        md_noushad = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div[2]/div/div/div[2]/div/div/div"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", md_noushad)
        time.sleep(1)
        try:
            md_noushad.click()
            logger.info("✓ md noushad selected")
        except:
            driver.execute_script("arguments[0].click();", md_noushad)
            logger.info("✓ md noushad selected (JavaScript)")
        
        time.sleep(3)
        
        logger.info("Step 27: Clicking Create Group button...")
        create_group_submit = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/form/div[4]/button[2]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", create_group_submit)
        time.sleep(1)
        try:
            create_group_submit.click()
            logger.info("✓ Create Group button clicked")
        except:
            driver.execute_script("arguments[0].click();", create_group_submit)
            logger.info("✓ Create Group button clicked (JavaScript)")
        
        time.sleep(5)
        
        # ========== CREATE GROUP EXPENSE ==========
        
        logger.info("Step 28: Waiting for parent div...")
        parent_div_expense = extended_wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div[1]/div"))
        )
        time.sleep(2)
        
        logger.info("Step 28: Clicking Add Expense button...")
        add_expense_button_group = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[1]/div/div[2]/a[2]"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", add_expense_button_group)
        time.sleep(1)
        try:
            add_expense_button_group.click()
            logger.info("✓ Add Expense button clicked")
        except:
            driver.execute_script("arguments[0].click();", add_expense_button_group)
            logger.info("✓ Add Expense button clicked (JavaScript)")
        time.sleep(3)
        
        logger.info("Step 29: Clicking Group expense option...")
        group_expense_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[1]/button[2]"))
        )
        group_expense_button.click()
        logger.info("✓ Group expense option selected")
        time.sleep(2)
        
        logger.info("Step 30: Filling description field (food)...")
        description_field_group = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[3]/form/div[1]/div[1]/div[1]/input"))
        )
        description_field_group.clear()
        description_field_group.send_keys("food")
        logger.info("✓ Description entered: food")
        time.sleep(1)
        
        logger.info("Step 31: Filling amount field (10000)...")
        amount_field_group = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[3]/form/div[1]/div[1]/div[2]/input"))
        )
        amount_field_group.clear()
        amount_field_group.send_keys("10000")
        logger.info("✓ Amount entered: 10000")
        time.sleep(1)
        
        logger.info("Step 32: Clicking Group selector...")
        group_selector = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[3]/form/div[1]/div[3]/div/button"))
        )
        group_selector.click()
        logger.info("✓ Group selector clicked")
        time.sleep(3)
        
        logger.info("Step 33: Selecting any available group...")
        try:
            group_options = driver.find_elements(By.XPATH, "//div[contains(@class, 'group') or contains(@role, 'option')]")
            
            if not group_options:
                group_options = driver.find_elements(By.XPATH, "//*[contains(text(), 'group') or contains(text(), 'Group') or contains(text(), 'testing')]")
            
            if group_options:
                selected_group = group_options[0]
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selected_group)
                time.sleep(1)
                try:
                    selected_group.click()
                    group_name = selected_group.text or "Unknown"
                    logger.info(f"✓ Group selected: {group_name}")
                except:
                    driver.execute_script("arguments[0].click();", selected_group)
                    group_name = selected_group.text or "Unknown"
                    logger.info(f"✓ Group selected (JavaScript): {group_name}")
            else:
                any_group = extended_wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'testing_group') or contains(text(), 'foody')]"))
                )
                any_group.click()
                logger.info("✓ Group selected using fallback")
                
        except Exception as e:
            logger.warning(f"Error selecting group: {e}")
        
        time.sleep(2)
        
        logger.info("Step 34: Clicking Paid By dropdown...")
        paid_by_dropdown_group = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[3]/form/div[1]/div[4]/select"))
        )
        paid_by_dropdown_group.click()
        logger.info("✓ Paid By dropdown opened")
        time.sleep(1)
        
        logger.info("Step 35: Selecting 'You' option...")
        you_option_group = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[3]/form/div[1]/div[4]/select/option[4]"))
        )
        you_option_group.click()
        logger.info("✓ 'You' option selected")
        time.sleep(1)
        
        logger.info("Step 36: Clicking Create Expense button...")
        create_expense_button_group = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div/div[3]/form/div[2]/button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", create_expense_button_group)
        time.sleep(1)
        try:
            create_expense_button_group.click()
            logger.info("✓ Group expense created")
        except:
            driver.execute_script("arguments[0].click();", create_expense_button_group)
            logger.info("✓ Group expense created (JavaScript)")
        
        time.sleep(5)
        
        # ========== SETTLE UP FLOW ==========
        
        logger.info("Step 37: Waiting for Settle Up button parent div...")
        settle_parent_div = extended_wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div/div[1]/div/div[2]"))
        )
        logger.info("✓ Settle Up parent div found")
        time.sleep(2)
        
        logger.info("Step 37: Clicking Settle Up button...")
        settle_up_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[1]/div/div[2]/a[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", settle_up_button)
        time.sleep(1)
        try:
            settle_up_button.click()
            logger.info("✓ Settle Up button clicked")
        except:
            driver.execute_script("arguments[0].click();", settle_up_button)
            logger.info("✓ Settle Up button clicked (JavaScript)")
        
        time.sleep(3)
        
        logger.info("Step 38: Clicking 'Who are you settling with?'...")
        try:
            settling_with = extended_wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div[2]/form/div/div/div[1]/div/div[2]"))
            )
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", settling_with)
            time.sleep(1)
            try:
                settling_with.click()
                logger.info("✓ 'Who are you settling with?' clicked")
            except:
                driver.execute_script("arguments[0].click();", settling_with)
                logger.info("✓ 'Who are you settling with?' clicked (JavaScript)")
            time.sleep(2)
        except TimeoutException:
            logger.info("'Who are you settling with?' not found or not needed, continuing...")
        
        logger.info("Step 39: Selecting who paid (first option)...")
        who_paid_option = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div[2]/form/div[2]/div/div[1]/label/div"))
        )
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", who_paid_option)
        time.sleep(1)
        try:
            who_paid_option.click()
            logger.info("✓ Who paid option selected")
        except:
            driver.execute_script("arguments[0].click();", who_paid_option)
            logger.info("✓ Who paid option selected (JavaScript)")
        
        time.sleep(1)
        
        logger.info("Step 40: Entering settlement amount (1000)...")
        amount_input_settlement = extended_wait.until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/main/div/div/div[2]/div[2]/form/div[3]/div/input"))
        )
        amount_input_settlement.clear()
        amount_input_settlement.send_keys("1000")
        logger.info("✓ Settlement amount entered: 1000")
        time.sleep(1)
        
        logger.info("Step 41: Clicking Record Settlement button...")
        record_settlement_button = extended_wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div[2]/form/button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", record_settlement_button)
        time.sleep(1)
        try:
            record_settlement_button.click()
            logger.info("✓ Record Settlement button clicked")
        except:
            driver.execute_script("arguments[0].click();", record_settlement_button)
            logger.info("✓ Record Settlement button clicked (JavaScript)")
        
        time.sleep(5)
        
        print("\n" + "="*70)
        print("✅ AUTOMATION COMPLETED SUCCESSFULLY!")
        print("="*70)
        print("✓ Signed in successfully")
        print("✓ Created individual expense: dinner - 6000")
        print("✓ Viewed settlement tab")
        print("✓ Created group: testing_group")
        print("✓ Added members: noushad ramim, md noushad")
        print("✓ Created group expense: food - 10000")
        print("✓ Recorded settlement: 1000")
        print(f"Final URL: {driver.current_url}")
        print("="*70 + "\n")
        
        return True
        
    except TimeoutException as e:
        logger.error(f"Timeout Error: {e}")
        if driver:
            logger.error(f"Current URL: {driver.current_url}")
            logger.error(f"Page title: {driver.title}")
            try:
                driver.save_screenshot("error_screenshot.png")
                logger.info("Screenshot saved as error_screenshot.png")
            except:
                pass
        print("\n❌ Test failed due to timeout. Press ENTER to close...")
        input()
        return False
        
    except Exception as e:
        logger.error(f"Error: {type(e).__name__} - {e}")
        if driver:
            logger.error(f"Current URL: {driver.current_url}")
            logger.error(f"Page title: {driver.title}")
            try:
                driver.save_screenshot("error_screenshot.png")
                logger.info("Screenshot saved as error_screenshot.png")
            except:
                pass
        print("\n❌ Test failed. Press ENTER to close...")
        input()
        return False
        
    finally:
        if driver:
            logger.info("Closing browser...")
            driver.quit()


if __name__ == "__main__":
    print("\n" + "="*70)
    print("🚀 STARTING SPLITIFY COMPLETE AUTOMATION TEST")
    print("="*70 + "\n")
    
    success = automated_signin_and_create_group()
    
    if success:
        print("\n✅ Test PASSED")
    else:
        print("\n❌ Test FAILED")
