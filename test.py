from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def test_user_signup():
    driver.get("http://127.0.0.1:5000/signup")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password1").send_keys("Test1234")
    driver.find_element(By.NAME, "password2").send_keys("Test1234")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)
    assert "Welcome" in driver.page_source
    print("Sign-up test passed!")

def test_user_login():
    driver.get("http://127.0.0.1:5000/login")
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("Test1234")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)
    assert "My Notes" in driver.page_source
    print("Login test passed!")

def test_add_note():
    driver.get("http://127.0.0.1:5000/notes")
    driver.find_element(By.NAME, "note_content").send_keys("Test Note")
    driver.find_element(By.NAME, "add_note").click()
    time.sleep(2)
 assert "Test Note" in driver.page_source
    print("Add note test passed!")

def test_edit_note():
    driver.get("http://127.0.0.1:5000/notes")
    driver.find_element(By.CLASS_NAME, "edit_button").click()
    driver.find_element(By.NAME, "note_content").clear()
    driver.find_element(By.NAME, "note_content").send_keys("Updated Test Note")
    driver.find_element(By.NAME, "update_note").click()
    time.sleep(2)
    assert "Updated Test Note" in driver.page_source
    print("Edit note test passed!")

def test_delete_note():
    driver.get("http://127.0.0.1:5000/notes")
    driver.find_element(By.CLASS_NAME, "delete_button").click()
    time.sleep(2)
    assert "Test Note" not in driver.page_source
    print("Delete note test passed!")

def test_view_notes():
    driver.get("http://127.0.0.1:5000/notes")
    notes_list = driver.find_elements(By.CLASS_NAME, "note_item")
    assert len(notes_list) > 0
    print("View notes test passed!")

def test_create_task():
    driver.get("http://127.0.0.1:5000/todolist")
    driver.find_element(By.NAME, "task_description").send_keys("Test Task")
    driver.find_element(By.NAME, "add_task").click()
    time.sleep(2)
    assert "Test Task" in driver.page_source
    print("Create task test passed!")
def test_edit_task():
    driver.get("http://127.0.0.1:5000/todolist")
    driver.find_element(By.CLASS_NAME, "edit_task_button").click()
    driver.find_element(By.NAME, "task_description").clear()
    driver.find_element(By.NAME, "task_description").send_keys("Updated Test Task")
    driver.find_element(By.NAME, "update_task").click()
    time.sleep(2)
    assert "Updated Test Task" in driver.page_source
    print("Edit task test passed!")

def test_delete_task():
    driver.get("http://127.0.0.1:5000/todolist")
    driver.find_element(By.CLASS_NAME, "delete_task_button").click()
    time.sleep(2)
    assert "Test Task" not in driver.page_source
    print("Delete task test passed!")

def test_logout():
    driver.get("http://127.0.0.1:5000/logout")
    time.sleep(2)
    assert "Login" in driver.page_source
    print("Logout test passed!")

def run_tests():
    test_user_signup()
    test_user_login()
    test_add_note()
    test_edit_note()
    test_delete_note()
    test_view_notes()
    test_create_task()
    test_edit_task()
 test_delete_task()
    test_logout()
    driver.quit()

if _name_ == "_main_":
    run_tests()