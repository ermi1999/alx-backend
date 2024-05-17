import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function for calculating a pagination.
    """
    return ((page_size * page) - page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        paginates the page and
        returns the appropriate page of the dataset.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        
        dataset = self.dataset()
        start, finish = index_range(page, page_size)

        if len(dataset) - 1 < finish:
            return []
        return [dataset[i] for i in range(start, finish)]
