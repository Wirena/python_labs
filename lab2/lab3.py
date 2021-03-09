def format_table(table: list) -> list:
    formatted_table: list = []
    for i in range(0, len(table)):
        for j in range(i+1, len(table)):
            if table[i] is not None and table[j] is not None:
                if table[i][0] == table[j][0]:
                    table[j] = None
    for entity in table:
        if entity is None or entity[0] == "":
            continue
        else:
            mail = str(entity[0]).split("[")[0]
            phone = str(entity[0]).split(";")[1]
            phone = "(" + phone[2:5] + ") " + phone[6:9] + "-" + phone[9:14]
            date_to_format = str(entity[1]).split(".")
            date = date_to_format[2] + "/" + date_to_format[1] + "/" + date_to_format[0]
            formatted_table.append([mail, phone, date])
    return formatted_table


def main():
    print(format_table([
        ["tomuk47[at]mail.ru;+72312185167", "99.10.02", "99.10.02"],
        ["tomuk47[at]mail.ru;+72312185167", "99.10.02", "99.10.02"],
        None,
        ["cagman48[at]rambler.ru;+75006471973", "01.12.27", "01.12.27"],
        ["gumanz84[at]mail.ru;+79781483323", "01.04.27", "01.04.27"]
    ]))


if __name__ == "__main__":
    main()
