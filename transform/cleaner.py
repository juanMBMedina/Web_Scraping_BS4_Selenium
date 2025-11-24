class Cleaner:
    def clean(self, data):
        data["title_raw"] = data["title_raw"].strip() if data["title_raw"] else None
        return data
