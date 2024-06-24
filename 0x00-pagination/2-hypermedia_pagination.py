#!/usr/bin/env python3
"""Hypermedia pagination"""

import csv
import math
from typing import List, Dict, Any

class Server:
    def __init__(self):
        # Initialize an empty list to store the dataset
        self.dataset = []

        # Read the CSV file and populate the dataset list
        with open('0x00-pagination/user_data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.dataset.append(row)

    def get_page(self, page_number: int = 1, page_size: int = 10) -> List[List[str]]:
        # Ensure that page_number and page_size are positive integers
        if page_number <= 0 or page_size <= 0:
            return []

        # Calculate the start and end indices of the current page
        start = (page_number - 1) * page_size
        end = start + page_size
        # Return the data for the current page
        return self.dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        # Get the data for the current page
        data = self.get_page(page, page_size)
        # Calculate the total number of pages
        total_pages = math.ceil(len(self.dataset) / page_size)

        # Calculate the next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return a dictionary containing pagination information
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }

if __name__ == "__main__":
    # Create an instance of the Server class
    server = Server()

    # Test the get_hyper method with different parameters
    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))

