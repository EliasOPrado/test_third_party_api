class Services:

    SPECIAL_1 = {
        "minlon": -2.196998,
        "minlat": -46.361899,
        "maxlon": -15.411580,
        "maxlat": -34.276938
    }

    SPECIAL_2 = {
        "minlon": -19.766959,
        "minlat": -52.997614,
        "maxlon": -23.966413,
        "maxlat": -44.428305
    }

    NORMAL = {
        "minlon": -26.155681,
        "minlat": -54.777426,
        "maxlon": -34.016466,
        "maxlat": -46.603598
    }


    def is_between(a, x, b):
        return min(a, b) < x < max(a, b)

    # add max and min for both..
    SPECIAL = {}

    SPECIAL["minlon"] = min(SPECIAL_1["minlon"], SPECIAL_2["minlon"])
    SPECIAL["maxlon"] = max(SPECIAL_1["maxlon"], SPECIAL_2["maxlon"])

    SPECIAL["minlat"] = min(SPECIAL_1["minlat"], SPECIAL_2["minlat"])
    SPECIAL["maxlat"] = max(SPECIAL_1["maxlat"], SPECIAL_2["maxlat"])

    def check_user_type(self, coordinates):
        # add the coordination dictionary
        if self.is_between(self.SPECIAL["minlon"], float(coordinates["longitude"]), self.SPECIAL["maxlon"]):
            return "special"
            
        elif self.is_between(self.NORMAL["minlon"], float(coordinates["longitude"]), self.NORMAL["maxlon"]):
            return "normal"
        else:
            return "laborious"

    def to_e164_format(self, str_phone):
            phone = "".join(x for x in str_phone if x.isdigit() or x == "+")
            return f"+55{phone}"
