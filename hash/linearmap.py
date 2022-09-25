class Map:
    def __init__(self):
        self._entryList = list()

    # Returns the number of entries in map
    def __len__(self):
        return len(self._entryList)

    # Determines if the map contains the give key
    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    # adds new value to the map
    def _add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:  # If key was found
            self._entryList[ndx].value = value
            return False
        else:   # If key was not found
            entry = _MapValue(key, value)
            self._entryList.append(entry)
            return True
    # Returns the value associated with the key

    def _valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key"
        return self._entryList[ndx].value

    # Remove the entry associated with the key
    def _remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalif map key"
        self._entryList.pop(ndx)

    # Helper method
    # If key is not found None is returned
    def _findPosition(self, key):
        # Itereate through each entry in the list
        for i in range(len(self)):
            # if the key is found return key index
            if self._entryList[i].key == key:
                return i
        # If key is not found return None
        return None


# Storage class for Holding key value pair
class _MapValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value


if __name__ == '__main__':
    mymap = Map()
    mymap._add('name', 'shailesh')
    mymap._add('age', 20)
    mymap._add('salary', 40000)

    print(mymap.__contains__('age'))
    print(mymap._valueOf('age'))
    mymap._remove('age')
    print(mymap._valueOf('age'))
