class Counter:
    def __init__(self, filename):
        self.filename = filename

    def increment(self):
        current_count = self._current_count()
        self._save_count(current_count + 1)
        
    def _current_count(self):
        try:
            file = open(self.filename, "r+")
            count = file.readline()
            file.close()
            if not count:
                return 0
            return int(count)
        except:
            return 0
    
    def _save_count(self, count):
        file = open(self.filename, "w+")
        file.write(str(count))
        file.close()
        