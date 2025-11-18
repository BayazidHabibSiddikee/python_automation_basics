import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def send_email_via_kuku():
    """
    Automated email sender using Kuku.lu temporary email service
    All form inputs are collected at the beginning, then filled automatically
    """
    # Collect all inputs at the start
    print("=== Email Details ===")
    recipient_email = input("Enter recipient's email: ")
    subject_text = input("Enter email subject: ")
    message_text = input("Enter your message: ")
    
    # Set up Edge browser options
    edge_options = Options()
    # edge_options.add_argument("--headless")  # Uncomment to run in background
    
    browser = None
    try:
        # Initialize browser
        browser = webdriver.Edge(options=edge_options)
        browser.maximize_window()
        
        print("\n🌐 Opening Kuku.lu...")
        browser.get('https://m.kuku.lu/en.php')
        
        # Wait for page to load
        wait = WebDriverWait(browser, 20)
        
        # Step 1: Create address automatically
        print("📧 Creating temporary email address...")
        create_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create an address automatically']"))
        )
        create_button.click()
        
        # Step 2: Confirm creation
        print("✅ Confirming email creation...")
        confirm_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Yes']"))
        )
        confirm_button.click()
        
        # Step 3: Click "Create new message"
        print("✉️ Opening message composer...")
        new_message_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create new message']"))
        )
        new_message_button.click()
        
        # Step 4: Fill out the email form automatically
        print("📝 Filling out email form...")
        
        # Multiple ways to find the recipient field
        recipient_input = None
        try:
            # Method 1: Try by name attribute
            recipient_input = wait.until(EC.presence_of_element_located((By.NAME, "recipient")))
        except:
            try:
                # Method 2: Try by following the label
                recipient_input = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'Recipient')]/following-sibling::input")))
            except:
                try:
                    # Method 3: Try by input type and context
                    recipient_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email' or @type='text'][1]")))
                except:
                    # Method 4: Find any input field near "Recipient" text
                    recipient_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[preceding::text()[contains(., 'Recipient')] or following::text()[contains(., 'Recipient')]]")))
        
        recipient_input.clear()
        recipient_input.send_keys(recipient_email)
        print(f"✅ Recipient filled: {recipient_email}")
        
        # Find and fill subject field
        subject_input = None
        try:
            # Method 1: By name
            subject_input = browser.find_element(By.NAME, "subject")
        except:
            try:
                # Method 2: By label association
                subject_input = browser.find_element(By.XPATH, "//label[contains(text(), 'Subject')]/following-sibling::input")
            except:
                # Method 3: By input order (usually second input)
                subject_input = browser.find_element(By.XPATH, "//input[@type='text'][2]")
        
        subject_input.clear()
        subject_input.send_keys(subject_text)
        print(f"✅ Subject filled: {subject_text}")
        
        # Find and fill message field
        message_input = None
        try:
            # Method 1: By name
            message_input = browser.find_element(By.NAME, "message")
        except:
            try:
                # Method 2: By textarea tag
                message_input = browser.find_element(By.TAG_NAME, "textarea")
            except:
                # Method 3: By label association
                message_input = browser.find_element(By.XPATH, "//label[contains(text(), 'Message')]/following-sibling::textarea")
        
        message_input.clear()
        message_input.send_keys(message_text)
        print(f"✅ Message filled: {message_text[:50]}...")
        
        # Step 5: Send the email
        print("📤 Sending email...")
        send_button = None
        try:
            # Method 1: By value
            send_button = browser.find_element(By.XPATH, "//input[@type='submit' and @value='Send']")
        except:
            try:
                # Method 2: By submit type
                send_button = browser.find_element(By.XPATH, "//input[@type='submit']")
            except:
                try:
                    # Method 3: By button text
                    send_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
                except:
                    # Method 4: Any submit button
                    send_button = browser.find_element(By.XPATH, "//input[@type='submit'] | //button[@type='submit']")
        
        send_button.click()
        
        # Wait for confirmation
        time.sleep(3)
        
        # Check for success message
        try:
            success_indicators = [
                "//*[contains(text(), 'sent')]",
                "//*[contains(text(), 'Message sent')]",
                "//*[contains(text(), 'delivered')]",
                "//*[contains(text(), 'success')]"
            ]
            
            for indicator in success_indicators:
                try:
                    browser.find_element(By.XPATH, indicator)
                    print("✅ Email sent successfully!")
                    break
                except:
                    continue
            else:
                print("⚠️ Email may have been sent, but couldn't confirm.")
        except:
            print("⚠️ Email may have been sent, but couldn't confirm.")
        
        # Keep browser open for a moment to see result
        input("Press Enter to close the browser...")
        
    except TimeoutException:
        print("❌ Timeout: Page elements took too long to load")
    except NoSuchElementException as e:
        print(f"❌ Element not found: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        if browser:
            browser.quit()

def inspect_form_elements():
    """
    Helper function to inspect and find form elements
    Use this to debug and find the correct form field names
    """
    browser = None
    try:
        browser = webdriver.Edge()
        browser.maximize_window()
        
        print("🔍 Inspecting form elements...")
        browser.get('https://m.kuku.lu/en.php')
        
        wait = WebDriverWait(browser, 20)
        
        # Navigate to the form
        create_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create an address automatically']"))
        )
        create_button.click()
        
        confirm_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Yes']"))
        )
        confirm_button.click()
        
        new_message_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create new message']"))
        )
        new_message_button.click()
        
        # Wait for form to load
        time.sleep(3)
        
        # Find all forms
        forms = browser.find_elements(By.TAG_NAME, "form")
        print(f"Found {len(forms)} form(s)")
        
        for i, form in enumerate(forms):
            print(f"\n--- Form {i+1} ---")
            print(f"Action: {form.get_attribute('action')}")
            print(f"Method: {form.get_attribute('method')}")
            
            # Find all input elements
            inputs = form.find_elements(By.TAG_NAME, "input")
            textareas = form.find_elements(By.TAG_NAME, "textarea")
            
            print("Input fields:")
            for j, inp in enumerate(inputs):
                print(f"  Input {j+1}: name='{inp.get_attribute('name')}', type='{inp.get_attribute('type')}', placeholder='{inp.get_attribute('placeholder')}'")
            
            print("Textarea fields:")
            for j, textarea in enumerate(textareas):
                print(f"  Textarea {j+1}: name='{textarea.get_attribute('name')}', placeholder='{textarea.get_attribute('placeholder')}'")
        
        # Find all labels
        labels = browser.find_elements(By.TAG_NAME, "label")
        print(f"\nFound {len(labels)} label(s):")
        for i, label in enumerate(labels):
            print(f"  Label {i+1}: '{label.text}' -> for='{label.get_attribute('for')}'")
        
        input("\nPress Enter to close the browser and see the form structure...")
        
    except Exception as e:
        print(f"❌ Error during inspection: {e}")
    finally:
        if browser:
            browser.quit()

def send_email_no_interaction():
    """
    Version that takes all inputs at once and fills everything automatically
    """
    # Get all user inputs first
    print("=== Automated Email Sender ===")
    recipient_email = input("Enter recipient's email: ")
    subject_text = input("Enter email subject: ")
    message_text = input("Enter your message: ")
    
    browser = None
    try:
        browser = webdriver.Edge()
        browser.maximize_window()
        
        print(f"\n🌐 Navigating to Kuku.lu...")
        browser.get('https://m.kuku.lu/en.php')
        
        wait = WebDriverWait(browser, 20)
        
        # Step 1: Create address automatically
        print("📧 Creating temporary email address...")
        create_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create an address automatically']"))
        )
        create_button.click()
        
        # Step 2: Confirm creation
        print("✅ Confirming email creation...")
        confirm_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Yes']"))
        )
        confirm_button.click()
        
        # Step 3: Click "Create new message"
        print("✉️ Opening message composer...")
        new_message_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create new message']"))
        )
        new_message_button.click()
        
        # Step 4: Fill all form fields automatically
        print("📝 Auto-filling form fields...")
        
        # Wait for form to be ready
        time.sleep(2)
        
        # Find and fill recipient field
        recipient_selectors = [
            "//input[@name='recipient']",
            "//input[@name='to']",
            "//input[@type='email']",
            "//input[contains(@placeholder, 'recipient')]",
            "//input[contains(@placeholder, 'email')]",
            "//input[1]"  # First input field
        ]
        
        recipient_filled = False
        for selector in recipient_selectors:
            try:
                recipient_input = browser.find_element(By.XPATH, selector)
                recipient_input.clear()
                recipient_input.send_keys(recipient_email)
                print(f"✅ Recipient filled: {recipient_email}")
                recipient_filled = True
                break
            except:
                continue
        
        if not recipient_filled:
            print("❌ Could not find recipient field")
            return
        
        # Find and fill subject field
        subject_selectors = [
            "//input[@name='subject']",
            "//input[@name='title']",
            "//input[contains(@placeholder, 'subject')]",
            "//input[@type='text'][2]"  # Second text input
        ]
        
        subject_filled = False
        for selector in subject_selectors:
            try:
                subject_input = browser.find_element(By.XPATH, selector)
                subject_input.clear()
                subject_input.send_keys(subject_text)
                print(f"✅ Subject filled: {subject_text}")
                subject_filled = True
                break
            except:
                continue
        
        if not subject_filled:
            print("❌ Could not find subject field")
            return
        
        # Find and fill message field
        message_selectors = [
            "//textarea[@name='message']",
            "//textarea[@name='body']",
            "//textarea[@name='content']",
            "//textarea"  # Any textarea
        ]
        
        message_filled = False
        for selector in message_selectors:
            try:
                message_input = browser.find_element(By.XPATH, selector)
                message_input.clear()
                message_input.send_keys(message_text)
                print(f"✅ Message filled: {message_text[:50]}...")
                message_filled = True
                break
            except:
                continue
        
        if not message_filled:
            print("❌ Could not find message field")
            return
        
        # Submit the form
        print("📤 Submitting form...")
        submit_selectors = [
            "//input[@type='submit']",
            "//button[@type='submit']",
            "//input[@value='Send']",
            "//button[contains(text(), 'Send')]"
        ]
        
        form_submitted = False
        for selector in submit_selectors:
            try:
                submit_button = browser.find_element(By.XPATH, selector)
                submit_button.click()
                print("✅ Form submitted!")
                form_submitted = True
                break
            except:
                continue
        
        if not form_submitted:
            print("❌ Could not find submit button")
            return
        
        # Wait for confirmation
        time.sleep(3)
        print("🎉 Process completed! Check if email was sent successfully.")
        
        # Keep browser open to see result
        input("Press Enter to close browser...")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if browser:
            browser.quit()

# Main execution
if __name__ == "__main__":
    print("=== Automated Email Sender for Kuku.lu ===")
    print("1. Send email (all inputs at start)")
    print("2. Inspect form elements (for debugging)")
    print("3. No-interaction version (fastest)")
    
    choice = input("Choose option (1, 2, or 3): ")
    
    if choice == "1":
        send_email_via_kuku()
    elif choice == "2":
        inspect_form_elements()
    elif choice == "3":
        send_email_no_interaction()
    else:
        print("Invalid choice. Running option 1...")
        send_email_via_kuku()
