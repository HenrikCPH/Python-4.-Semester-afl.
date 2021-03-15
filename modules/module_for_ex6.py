# opg. 1 - 8
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import requests

class url_book_handler():
    
    def __init__(self, url_list=[]):
        self.url_list = url_list
        self.filenames = []
    
    def __iter__(self):
        self.index = 0
        return self 

    def __next__(self):
        if self.index < len(self.filenames):
            current_index = self.index
            self.index += 1
            return self.filenames[1]
        else:
            raise StopIteration
        
    def download(self, url, filename):
        filename = str(filename) + ".txt"
        if requests.get(url).status_code == 404:
            raise NotFoundException()
            print("The page was not found")
        else:
            req = requests.get(url)
            with open(filename, 'w') as file:
                file.writelines((str(req.content))) # Får en int fejl, hvis ikke jeg bruger str(), gør det pænt?
        self.filenames.append(filename)        
    
    def multi_download(self):
        workers = len(self.url_list)
        with ThreadPoolExecutor(workers) as executor:
            executor.map(self.download, self.url_list, range(len(self.url_list))) 
    
    def urllist_generator(self):
        for url in self.url_list:
            yield url
                   
    def avg_vowels(self, filename):
        vowels = ["A", "E", "I", "O", "U", "Y"]

        with open(filename) as file:
            readFile = file.read()

        words = readFile.split()
        number_of_words = len(words)
        number_of_vowels = 0

        for word in words:
            for letter in word:
                if letter.upper() in vowels:
                    number_of_vowels += 1

        avg = round(number_of_vowels / number_of_words, 2)
        return avg, filename

    def hardest_read(self):
        workers = multiprocessing.cpu_count()
        
        with ProcessPoolExecutor(workers) as executor:
            results = executor.map(self.avg_vowels, self.filenames)
            
        highest_avg = None

        for result in results:
            if highest_avg is None or highest_avg[0] < result[0]:
                highest_avg = result

        return highest_avg[1]            