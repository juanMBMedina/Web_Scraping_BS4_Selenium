class Normalizer:
    def normalize(self, data):
        return {
            "title": data["title_raw"].title() if data["title_raw"] else None,
            "length": data["page_length"],
        }
