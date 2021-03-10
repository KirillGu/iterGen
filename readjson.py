import json
import wikipediaapi


class LinkPage:

    def __init__(self, path, start):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1
        self.wikiwiki = wikipediaapi.Wikipedia('en')

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['common']
        country_page = self.wikiwiki.page(country)
        country_link = country_page.fullurl

        return country, country_link



if __name__ == '__main__':
    results = open('results.txt', 'w', encoding='utf-8')
    print ("Поиск страницы из Википедии по каждой стране")
    print('Загрузка')
    for country, item in LinkPage('countries.json', 0):
        results.write(str(country) + '\t —- \t' + ' Ссылка' + '\t —> \t' + str(item) + '\n')
        print('/', end='', flush=True)#запись произойдет сразу

    results.close()
