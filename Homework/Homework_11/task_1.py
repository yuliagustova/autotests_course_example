# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
about_site = 'https://tensor.ru/about'
try:
    driver.get(sbis_site)
    sleep(2)
    # Ищем линк "Контакты" и переходим по в контакты
    contacts = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"]')
    contacts.click()
    sleep(2)
    # Ищем баннер тензор и кликаем на него
    tensor_banner = driver.find_element(By.CSS_SELECTOR, '[class="sbisru-Contacts__logo-tensor mb-8"]')
    tensor_banner.click()
    driver.switch_to.window(driver.window_handles[1])
    # Ищем блок "Сила в людях"
    people_news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    assert people_news.text == 'Сила в людях'
    assert people_news.is_displayed(), 'Новость "Сила в людях" не отображается'
    actions = ActionChains(driver)
    more = driver.find_element(By.CSS_SELECTOR, '[class="nl-LastCovers__header_newsLink"]')
    actions.move_to_element(more)
    actions.perform()
    sleep(2)
    # Ищем кнопку "Подробнее" и кликаем
    news_button = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-link')
    news_button.click()
    assert driver.current_url == about_site, 'Неверная ссылка'

finally:
    driver.quit()
