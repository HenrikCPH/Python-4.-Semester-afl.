{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# opg. 1 - 8\n",
    "from concurrent.futures import ThreadPoolExecutor\n",
    "import requests\n",
    "\n",
    "class url_book_handler():\n",
    "    \n",
    "    def __init__(self, url_list=[]):\n",
    "        self.url_list = url_list\n",
    "    \n",
    "    def __iter__(self):\n",
    "        self.index = 0\n",
    "        return self   \n",
    "    \n",
    "    def __next__(self):\n",
    "        if self.index < len(self.filenames):\n",
    "            self.index += 1\n",
    "            return self.filename[self.index]\n",
    "        else:\n",
    "            raise StopIteration \n",
    "        \n",
    "    def download(url, filename):\n",
    "        if url.status_code == 404:\n",
    "             raise Exception(\"The page was not found\")\n",
    "        else:\n",
    "            self.url = url\n",
    "            self.filename = filename        \n",
    "    \n",
    "    def multi_download(func, args, worker=5): \n",
    "        with ThreadPoolExecutor(worker) as ex:\n",
    "            res = ex.map(func, args)\n",
    "        return list(res)\n",
    " "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
