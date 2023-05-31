newspaper_pages = [12, 10, 16, 8, 14]   # список количества страниц газет
magazine_pages = [30, 28, 42, 36]   # список количества страниц журналов

magazine_pages_total = sum(magazine_pages)   # суммируем количество страниц в журналах

for pages in newspaper_pages:   # перебираем количество страниц в газетах
    while pages > 16:   # пока количество страниц больше 16, мы будем удалять оттуда последние элементы, но в целом сохранять суммарное количество страниц.
        pages -= 1
        magazine_pages_total += 1

print(magazine_pages_total)