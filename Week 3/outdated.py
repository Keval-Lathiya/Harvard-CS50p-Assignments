


def main():
    get_date("Date: ")


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def get_date(prompt):
    while True:
        try:
            me_date = input(prompt)

            if "/" in me_date:
                m, d, y = me_date.split("/")
                month = int(m)
                day = int(d)
                year = int(y)

            elif "," in me_date:
                m, d, y = me_date.split()
                month = int(months.index(m) + 1)
                day = int(d.rstrip(","))
                year = int(y)

            else:
                continue

            if (
               day < 1 or day > 31 or
               month < 1 or month > 12 or
               year < 0 or year > 9999
               ):
                continue

            month = str(month)
            day = str(day)
            if len(month) == 1:
                month = "0" + month
            if len(day) == 1:
                day = "0" + day

            print(f"{year}-{month}-{day}", end="")
            break

        except ValueError:
            pass


if __name__ == "__main__":
    main()