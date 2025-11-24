from extract.meli.meli_extractor import MeliExtractor
from navigation.browser import create_driver
from pages.meli.meli_page import MeliPage
from load.csv_loader import CSVLoader


def run():
    driver = create_driver()
    meli_page = MeliPage(driver)
    extractor = MeliExtractor()
    list_items = []
    list_instalments = []
    meli_page.go()
    meli_page.search("teclado gamer xtriker 7")
    is_busy = True
    while is_busy:
        items, instalments = extractor.parse(driver.page_source)
        list_items.extend(items)
        list_instalments.extend(instalments)
        is_busy = meli_page.go_to_next_page()

    items_df = MeliExtractor.to_dataframe(list_items)
    instalments_df = MeliExtractor.to_dataframe(list_instalments)

    CSVLoader.save(items_df, "./output_data/meli_items.csv")
    CSVLoader.save(instalments_df, "./output_data/meli_instalments.csv")

    driver.quit()


if __name__ == "__main__":
    run()
