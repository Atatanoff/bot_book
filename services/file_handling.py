BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}
simbol = ",.!:;?"

def _check_end(text, page_size):    
    if text[-3] in simbol and text[-2] != ".": return text[:-2]
    return _check_end(text[:-1], page_size)

# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    text = text[start:start+page_size+2]
    if len(text) <= page_size: return text, len(text)  
    text = _check_end(text, page_size)
    return text, len(text)



# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r') as file:
        text = "".join(file.readlines())
    
    stop = 0
    page = 1
    
    while stop < len(text):
        text_page, offset = _get_part_text(text, stop, PAGE_SIZE)
        book[page] = text_page.lstrip()
        page+=1
        stop += offset


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)