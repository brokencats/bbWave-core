import os.path
import logging


class TreeWalker:
    root_dir_path = ''
    files_path_list = []
    supported_extensions_list = [
        'mp3', 'wav', 'm4a', 'flac', 'ogg', 'wave', 'ogv', 'oga', 'ogx', 'ogm', 'spx', 'opus', 'webm', 'mp4', '3gp',
        'm4b', 'm4p', 'm4r', 'm4v'
    ]

    def __init__(self, root_dir_path):
        self.root_dir_path = os.path.expanduser(root_dir_path)

    def build_files_list(self):
        if not os.path.exists(self.root_dir_path) or not os.path.isdir(self.root_dir_path):
            logging.error('Directory "{}" does not exists!'.format(self.root_dir_path))
        else:
            logging.info('Found directory "{}"'.format(self.root_dir_path))

        self.__recursive_search(self.root_dir_path)
        logging.info('Found {} files'.format(len(self.files_path_list)))

    def __recursive_search(self, root_path):
        current_dir = os.listdir(root_path)
        for filename in current_dir:
            filepath = '{}/{}'.format(root_path, filename)

            if os.path.isdir(filepath):
                self.__recursive_search(filepath)
            else:
                if self.__is_valid_extension(filename):
                    self.files_path_list.append(filepath)

    def __is_valid_extension(self, filename):
        for ext in self.supported_extensions_list:
            if filename.find(ext, len(filename) - 5) > 0:
                return True

    def get_file_list(self):
        return self.files_path_list