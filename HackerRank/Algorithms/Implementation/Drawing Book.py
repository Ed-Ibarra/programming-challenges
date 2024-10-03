def pageCount(last_page, page):
    pages_by_pair = (last_page//2) + 1
    page_found = (page//2) + 1

    inicio = page_found - 1
    final = pages_by_pair - page_found

    return inicio if inicio < final else final


if __name__ == '__main__':
    number_of_pages = int(input())
    page = int(input())

    result = pageCount(number_of_pages, page)
    print(result)