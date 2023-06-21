# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'
user_login, user_password = 'шариковдом', 'шариковдом123'


try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(2)
    # Ищем поле ввода логина и вводим логин
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    sleep(2)
    # Ищем поле ввода пароля и вводим пароль
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    sleep(5)
    # Ищем контакты и переходим в реестр контактов
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    sleep(2)
    contacts.click()
    sleep(2)
    dialogs = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    dialogs.click()
    sleep(2)
    # Ищем кнопку нового диалога
    add_contact = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    add_contact.click()
    sleep(5)
    find_contact = driver.find_element(By.CSS_SELECTOR, '.addressee-selector-popup__browser '
                                                        '.controls-InputBase__nativeField_hideCustomPlaceholder')
    sleep(2)
    # Ищем своего пользователя в окне выбора адресата
    find_contact.send_keys('Шарик Кот', Keys.ENTER)
    sleep(5)
    address = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    address.click()
    sleep(5)
    # Ищем поле ввода пароля и вводим сообщение
    message = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    message_txt = 'Cообщение'
    message.send_keys(message_txt)
    # Ищем кнопку отправки сообщения и отправляем сообщение
    send_message = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    send_message.click()
    sleep(2)
    # Проверяем отправленное сообщение в реестре, берем последнее (самое новое) сообщение и сравниваем текст с
    # отправленным
    new_message = driver.find_elements(By.CSS_SELECTOR, '.controls-BaseControl .msg-dialogs-item__message-text')[0]
    assert new_message.text == message_txt, 'Неверное сообщение'
    sleep(2)
    # Наводимся на сообщение и ищем кнопку удаления
    action = ActionChains(driver)
    action.move_to_element(new_message).perform()
    sleep(2)
    delete_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action deleteToArchive"]')
    delete_button.click()
    sleep(2)
    # Ищем последнее сообщение в реестре и сравниваем его с удаленным
    last_messege = driver.find_elements(By.CSS_SELECTOR, '.controls-BaseControl .msg-dialogs-item__message-text')[0]
    assert last_messege != message_txt

finally:
    driver.quit()
