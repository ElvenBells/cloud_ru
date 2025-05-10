import logging
from playwright.sync_api import sync_playwright

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('test_results.log', encoding='utf-8')
    ]
)

def test_example_website():
    logger = logging.getLogger(__name__)
    try:
        with sync_playwright() as p:
            logger.info("Запуск браузера")
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            logger.info("Открытие страницы https://example.com")
            page.goto("https://example.com")

            assert "Example" in page.title(), "Заголовок не содержит 'Example'"
            logger.info("Проверка заголовка: PASS")

            more_info_link = page.get_by_text("More information")
            if not more_info_link.is_visible():
                raise AssertionError("Ссылка 'More information' не найдена")
            more_info_link.click()
            logger.info("Клик по 'More information': PASS")

            expected_url = "https://www.iana.org/help/example-domains"
            assert page.url == expected_url, f"Ожидался URL {expected_url}, получен {page.url}"
            logger.info(f"Проверка URL ({expected_url}): PASS")

            logger.info("Все проверки успешно пройдены")
            browser.close()
            return True

    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        return False
    finally:
        logging.shutdown()

if __name__ == "__main__":
    if test_example_website():
        exit(0)
    else:
        exit(1)